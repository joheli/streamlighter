FROM python:3.13-slim

# change dir
WORKDIR /app

# copy files and folders
COPY streamlighter.py /app/streamlighter.py
COPY sl-apps /app/sl-apps
COPY requirements.txt /app/requirements.txt

# create non-root user app
RUN useradd -m -d /app -s /bin/bash app; \
    chown -R app:app /app
USER app

# install packages listed in requirements.xt
RUN pip install --user --no-cache-dir -r requirements.txt

# install wheels packages placed in directory /app/whl
RUN ls whl/*.whl 2>/dev/null && pip install --user --no-cache-dir whl/*.whl || echo "No wheels to install found."

# create convenience reload and install scripts
WORKDIR .local/bin
RUN printf '#!/bin/bash\npip install --user --no-cache-dir "$@"' > pippin; \
    chmod u+x pippin; \
    printf '#!/bin/bash\npython /app/streamlighter.py "$@"' > streamlighter; \
    chmod u+x streamlighter;

# add .local/bin to PATH
ENV PATH="/app/.local/bin:$PATH"

# cd back to /app
WORKDIR ../.. 

# default port 8501
EXPOSE 8501

# fire up
CMD ["streamlighter", "--sl-apps", "sl-apps", "--host", "0.0.0.0", "--port", "8501"]
