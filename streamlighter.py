import os
import sys
import argparse
import logging
from streamlit.web import cli as stcli


def main():
    # configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)s | %(message)s", stream=sys.stdout
    )
    
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description="Launch Streamlit apps from a folder.")

    parser.add_argument(
        "--port",
        type=int,
        default=8501,
        help="Port number the app should run on (default: 8501)",
    )

    parser.add_argument(
        "--sl-apps",
        type=str,
        default="sl-apps",
        help="Path to the folder containing Streamlit app(s)",
    )

    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="server address, host",
    )

    args = parser.parse_args()

    if not os.path.isdir(args.sl_apps):
        logger.error(f"The specified folder does not exist: {args.sl_apps}")
        sys.exit(1)

    app_files = [f for f in os.listdir(args.sl_apps) if f.endswith(".py")]

    if len(app_files) < 1:
        logger.error(f"Folder {args.sl_apps} does not contain *.py files. Exiting.")
        sys.exit(1)

    app_file = os.path.join(args.sl_apps, app_files[0])

    logger.info(
        f"Preparing to launch {app_file} on host {args.host}, port {args.port}."
    )

    try:
        stcli.main_run([app_file, "--server.port", str(args.port)], "--server.address", str(args.host))
    except FileNotFoundError:
        logger.error(f"File not found: {app_file}!")
    except KeyboardInterrupt:
        logger.warning("Streamlit app interrupted by user (Ctrl + C).")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
