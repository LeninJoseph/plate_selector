# Plate Selector Tool

## Overview
The Plate Selector Tool is a PySide2-based GUI application designed to simplify the process of selecting and opening plate files for visual effects or post-production workflows. It provides an intuitive interface to navigate through shows, shots, and plates, and integrates with RV for media playback.

## Features
- **Show Selection**: Autocomplete-enabled input field for selecting a show from a predefined directory.
- **Shot Listing**: Displays a list of shots available in the selected show.
- **Plate Navigation**: Allows users to navigate through plate folders and view available plate files.
- **RV Integration**: Double-clicking a plate file opens it in RV for playback.

## File Structure
- **`plate_select_tool.ui`**: The UI layout file created using Qt Designer.
- **`plate_selector.py`**: The main Python script that implements the application logic.

## Prerequisites
- Python 3.x
- PySide2 library
- RV media player installed (update the `rv_path` variable in `plate_selector.py` to match your RV installation path).

## Installation
1. Clone or download the repository.
2. Install the required Python libraries:
   ```bash
   pip install PySide2
   ```
3. Update the `shows_folder_path` and `rv_path` variables in `plate_selector.py` to match your environment.

## Usage
1. Run the application:
   ```bash
   python plate_selector.py
   ```
2. Enter the name of a show in the "Show" input field. Autocomplete suggestions will appear based on the available directories.
3. Select a shot from the list of shots displayed.
4. Navigate through the plate folders and double-click a plate file to open it in RV.

## Notes
- The application filters out specific folders (e.g., `Home`, `ingest`, `lib`, `bid`, `publish`) from the shot list.
- Ensure the directory structure under `shows_folder_path` matches the expected format:
  ```
  shows/
    ├── ShowName/
    │   ├── ShotName/
    │   │   ├── in/
    │   │   │   ├── plates/
    │   │   │   │   ├── PlateFolder/
    │   │   │   │   │   ├── plate_file.ext
  ```

## License
This project is for internal use and does not include a license. Please contact the author for permissions or inquiries.
