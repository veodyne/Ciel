# Ciel IDE

Ciel is a lightweight Python IDE focused on simplicity and speed. It includes built-in compilation support using [Nuitka](https://nuitka.net/) to build your Python programs.

<img width="1919" height="1079" alt="Screenshot 2025-08-03 221843" src="https://github.com/user-attachments/assets/874343e5-e0c5-4063-ae3b-5b481c667201" />

## Features

- **Built-in Compiler:** Integrated support for compiling Python scripts into fast executables
- **Build Options:** Supports `onefile` and `standalone` build types using the MinGW64 compiler backend.
## Usage

1. Open Ciel. 
2. Click **Compile** and select the file in your directory to compile.
3. Choose your desired build type (`onefile` or `standalone`).
4. A command prompt window will open, showing compilation progress and any errors. Nuitka will install the MinGW64 compiler for you.

## Notes

- Windows Defender will likely flag your compiled program due to false positives, so make sure to disable "Real Time Protection" in settings before compiling.
- You do not need to install Nuitka, it will install itself when compiling.

## Requirements

- Python 3.12 or any Python version compatible with Nuitka
- Windows OS (currently supports Windows builds)

## Future Plans

- Add more customizable build flags and plugin options.

## License
> 📜 Licensed under **CC BY-NC 4.0** – Non-commercial use only.

