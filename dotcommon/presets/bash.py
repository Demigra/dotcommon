from dotcommon.util import lines_starting_with

paths = (".bashrc", "bashrc")

readline_macros = lines_starting_with("bind", "#"), paths
aliases = lines_starting_with("alias", "#"), paths