import json
from pathlib import Path


def test_report_exists():
    """Verify that the output file /app/report.json exists."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_total_requests():
    """Verify that total_requests equals 6."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("total_requests") == 6, "Incorrect total_requests value"


def test_unique_ips():
    """Verify that unique_ips equals 3."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("unique_ips") == 3, "Incorrect unique_ips value"


def test_top_path():
    """Verify that top_path equals /index.html."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("top_path") == "/index.html", "Incorrect top_path value"
