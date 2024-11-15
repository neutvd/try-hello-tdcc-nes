import pytest

import try_hello_tdcc_nes
import try_hello_tdcc_nes.hello

@pytest.mark.parametrize('thing, expected', [("TDCC-NES", "Hello TDCC-NES")])
def test_hello(thing: str, expected: str) -> None:
    result = try_hello_tdcc_nes.hello.hello(thing)
    assert result == expected