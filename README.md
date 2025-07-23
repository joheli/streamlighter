[![Build and Publish Docker Image](https://github.com/joheli/streamlighter/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/joheli/streamlighter/actions/workflows/docker-publish.yml)
# Streamlighter

`streamlighter` is a dockerized server for [Streamlit](https://streamlit.io/) apps.

## Just do it

Spin up a docker container using the image provided with a volume (folder) containing your streamlit script and you should be good to go. 
Please note that the volume should be mapped to `/app/sl-apps` in the container.

E.g.

```
docker run --name streamlighter -v /your/path/to/streamlit_script:/app/sl-apps -p 8501:8501 ghcr.io/joheli/streamlighter:latest
```

If you have entered above command on your own computer, you can now access the streamlit app under `http://localhost:8501`.

## Install python packages

You can either rebuild the image with a fresh `requirements.txt` file or add packages after build into the container.

To add packages into the container proceed as follows:

```
# Enter the container with user "app"
docker exec -it --user app streamlighter bash

# once inside the container, add package XXX by typing
pip install --user --no-cache-dir XXX

# alternatively, use convenience script "pippin"
pippin XXX
```

> [!TIP]
> If you don't wish to reinstall all python packages every time you restart the container, how about persisting `/app/.local` to a volume? How, you ask? Simple: just add `-v streamlighter_local:/app/.local` to above "docker run" command! Now all changes in `/app/.local` are persisted to named volume `streamlighter_local`. (You can obviously change the name of the named volume or mount an existing folder as well.)

Have fun!