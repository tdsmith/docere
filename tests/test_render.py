from docere.render import _get_reports, tmp_cd
import os


def compare_report_lists(this, that):
    return (
        all([report in this for report in that]) and
        all([report in that for report in this])
    )


def test_get_reports():
    actual = _get_reports('tests/data/kr')
    expected = [
        {
            "title": "Crash Count",
            "publish_date": "2018-01-01",
            "author": "Joseph Blowseph",
            "file": "not_index.html",
            "path": "tests/data/kr/crash_count/not_index.html",
            "dir": "tests/data/kr/crash_count",
        },
        {
            "title": "User Count",
            "publish_date": "2018-01-02",
            "author": "Joe Blow",
            "file": "index.html",
            "path": "tests/data/kr/user_count/index.html",
            "dir": "tests/data/kr/user_count",
        },
    ]

    assert compare_report_lists(actual, expected)


def test_tmp_cd():
    basewd = os.getcwd()
    with tmp_cd('tests'):
        assert os.getcwd() != basewd

    assert os.getcwd() == basewd
