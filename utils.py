import re


EXPECTED = {
    'protocol': 'http',
    'host': 'video.google.co.uk',
    'subdomain': 'video',
    'domain': 'google.co.uk',
    'top-level domain': 'uk',
    'second-level domain': 'co.uk',
    'port': '80',
    'path': '/videoplay',
    'parameters': '?docid=-7246927612831078230&hl=en',
    'fragment': '#00h02m30s'}


def findall(regex, text):
    """find all instances in string"""
    exp = re.compile(regex, re.X)
    return re.findall(exp, text)


def match(regex, text):
    """Find the first instance, starting at the beginning"""
    exp = re.compile(regex, re.X)
    return re.match(exp, text)


def search(regex, text):
    """Find the first instance, anywhere in the string"""
    exp = re.compile(regex, re.X)
    return re.search(exp, text)


class UnexpectedGroupError(Exception):
    pass


class MissingGroupError(Exception):
    pass


class IncorrectMatchError(Exception):
    pass


def check_matches(exp, text, group_labels):
    """Little helper function to better visualize the results. And check answers.."""
    m = search(exp, text)
    
    if not m:
        raise MissingGroupError("No groups found in match! Try again")
        
    group_hash = m.groupdict()
    
    try:
        assert len(group_hash) == len(group_labels)
        
    except AssertionError:
        print(f"{len(group_hash)} groups found.. Expected {len(group_labels)}")
        raise
        
    try:
        assert all([(key in EXPECTED and key in group_labels) for key in group_hash])
        
    except AssertionError:
        raise UnexpectedGroupError(f"""Unexpected group found.. 
        Please make sure your group name is in {list(EXPECTED.keys())}, and also {group_labels}""")
    
    for key, value in group_hash.items():
        try:
            assert value == EXPECTED[key]
        
        except AssertionError:
            raise IncorrectMatchError(f"""
                Sorry, but the match is incorrect. 
                Please try again.
                Got {value}, expected {EXPECTED[key]}""")
        
        print(f"{key + ':': <20} '{value}'") 
