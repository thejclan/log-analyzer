# Login Log Analyzer

A lightweight Python script that summarizes login events and flags repeated failed attempts by username and source IP address. This project is a basic security-log analysis exercise, not a production intrusion-detection system.

## Features

- Counts successful and failed login attempts.
- Counts distinct usernames and source IPs associated with failed logins.
- Flags usernames **and** IP addresses with at least **3 failed login attempts** (configurable via `FAILED_LOGIN_THRESHOLD`).

## Requirements

- Python 3 (standard library only; no third-party packages)

## Files

- `analyzer.py` — analyzes login events and prints a summary.
- `log.txt` — synthetic sample events used to demonstrate the script.

## Usage

Run from the repository directory:

```bash
python3 analyzer.py
```

The script reads `log.txt` from the current working directory.

## Actual Example Output

Running `python3 analyzer.py` against the included `log.txt` produces:

```text
Login success: 2
Login failed: 5
Unique failed users: 2
Unique failed IPs: 2

Warning - Users:
bob has 4 failed login attempts

Warning - IPs:
192.168.1.20 has 4 failed login attempts
```

## Detection Results

The sample log includes **7 events**: **2 successful** and **5 failed** logins. The account `bob` and source IP `192.168.1.20` each have **4 failed attempts**, exceeding the configured threshold of **3**. The script therefore prints warnings for both.

These warnings identify repeated failures for investigation; **they do not establish that a brute-force attack occurred**. The current script counts failures across the entire file and does not analyze time windows or correlate additional indicators.

## Limitations and Next Steps

- Add time-window-based thresholds and chronological correlation.
- Support other log formats and malformed-line handling.
- Add command-line arguments for input path and threshold, plus automated tests.

## Responsible Use

The example log uses synthetic, private-network addresses and does not contain real user credentials. Only analyze logs you are authorized to access.
