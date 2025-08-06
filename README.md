# NumberPy (Chudnovsky Pi Calculator)

This Python script calculates the value of π (pi) to a specified number of decimal places using the **Chudnovsky algorithm**, known for its fast convergence and high precision.

## Features

- High-precision π calculation using the Chudnovsky algorithm
- Efficient iterative factorial implementation
- Accepts input from terminal argument (`-n`) or via interactive prompt
- Built-in input validation and fallback modes
- Uses only Python 3 standard libraries

## Requirements

- Python 3.x
- No external dependencies

## Usage

You can run the script in two ways:

### 1. With Command-Line Argument

```bash
python NumberPy.py -n 50
```
This will print the value of π to 50 decimal places.

### 2. Interactive Mode
If no argument is provided, the script will ask for user input:
```bash
python NumberPy.py
```
You'll be prompted to enter the desired number of digits or type quit to exit.

## Example Output
```bash
$ python NumberPy.py -n 10
3.1415926535
```

## How It Works
* The script uses the [Chudnovsky algorithm](https://en.wikipedia.org/wiki/Chudnovsky_algorithm), which is a rapidly converging formula for π.
* The algorithm relies on computing large factorials and summing terms of a special series.
* Precision is managed using Python’s `decimal` module with rounding mode set to `ROUND_FLOOR`.

## Notes

- The number of iterations determines the number of accurate decimal places.
- For very large digit requests, performance may decrease due to high-precision arithmetic and large factorials.

## License
This project is open-source and free to use for educational or personal purposes.