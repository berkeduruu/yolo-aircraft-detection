import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_python_sources_parse():
    for path in (ROOT / "codes").rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for path in (ROOT / "models").rglob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def test_included_model_and_demo_assets_exist():
    assert (ROOT / "models" / "N_new720p.pt").is_file()
    assert (ROOT / "models" / "S_new720p.pt").is_file()
    assert (ROOT / "assets" / "roi_video_poster.jpg").is_file()


def test_documented_dataset_tools_are_linked():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Video-Frame-Grabber" in readme
    assert "YOLO_Supported_Annotation_Tool" in readme
    assert "jetson-deepstream-yolo-pipelines" in readme
