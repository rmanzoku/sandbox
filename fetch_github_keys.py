#!/usr/bin/env python3
"""Fetch GitHub user's public SSH keys.

This script uses only the Python standard library to retrieve the
public SSH keys published by a GitHub user. The keys are available via
``https://github.com/<username>.keys``.

Usage:
    python fetch_github_keys.py <github_username>

This should work on macOS as well as other Unix-like systems.
"""

import sys
import urllib.request


def fetch_public_keys(username: str) -> str:
    """Fetch public keys for the given GitHub username.

    Args:
        username: GitHub username.

    Returns:
        A string containing the raw contents of the ``.keys`` endpoint.
    """
    url = f"https://github.com/{username}.keys"
    with urllib.request.urlopen(url) as response:
        return response.read().decode("utf-8")


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python fetch_github_keys.py <github_username>")
        return 1

    username = argv[0]
    try:
        keys = fetch_public_keys(username)
    except Exception as exc:  # pragma: no cover - simple example
        print(f"Error fetching keys: {exc}")
        return 1

    if not keys:
        print(f"No keys found for user '{username}'.")
    else:
        print(keys)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
