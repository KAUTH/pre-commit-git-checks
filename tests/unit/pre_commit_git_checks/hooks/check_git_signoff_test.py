#!/usr/bin/env python3

from pre_commit_git_checks.hooks.check_git_signoff import (
    commit_message_is_valid,
    email_is_valid,
)


def test_email_is_valid_correct_email() -> None:
    """Test that valid emails are identified as such"""
    email = "myemail@gmail.com"

    assert True is email_is_valid(email)


def test_email_is_valid_incorrect_email() -> None:
    """Test that invalid emails are identified as such"""
    invalid_emails = [
        "myemailgmail.com",
        "@gmail.com",
        "myemail@gmail",
        "myemailgmailcom",
    ]

    for email in invalid_emails:
        assert False is email_is_valid(email)


def test_commit_message_is_valid_correct_message() -> None:
    """Test that valid commit messages are identified as such"""
    name = "Kostas Pap"
    email = "myemail@gmail.com"
    commit_message = """
    Add commit message title
    
    - Added tests
    - Wrote a commit message body
    
    Signed-off-by: Kostas Pap <myemail@gmail.com>
    """

    assert True is commit_message_is_valid(commit_message, name, email)


def test_commit_message_is_valid_missing_name() -> None:
    """
    Test that invalid commit messages are identified as such

    Scenario: missing name from signoff
    """
    name = "Kostas Pap"
    email = "myemail@gmail.com"
    commit_message = """
    Add commit message title

    - Added tests
    - Wrote a commit message body

    Signed-off-by: <myemail@gmail.com>
    """

    assert False is commit_message_is_valid(commit_message, name, email)


def test_commit_message_is_valid_missing_email() -> None:
    """
    Test that invalid commit messages are identified as such

    Scenario: missing email from signoff
    """
    name = "Kostas Pap"
    email = "myemail@gmail.com"
    commit_message = """
    Add commit message title

    - Added tests
    - Wrote a commit message body

    Signed-off-by: Kostas Pap
    """

    assert False is commit_message_is_valid(commit_message, name, email)
