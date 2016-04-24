class Config(object):
    def __init__(self):
        # file endings
        self.cpp_header_endings = ["h", "hh", "hpp"]
        self.python_file_ending = "py"
        self.pyx_file_ending = "pyx"
        self.pxd_file_ending = "pxd"

        # operator mapping TODO extend
        # http://docs.cython.org/src/reference/special_methods_table.html
        self.operators = {
            "operator()": "__call__",
            "operator[]": "__getitem__",
            "operator+": "__add__",
            "operator-": "__sub__",
            "operator*": "__mul__",
            "operator/": "__div__"
        }
        self.call_operators = {
            "operator()": "call",
            "operator[]": "getitem",
            "operator+": "add",
            "operator-": "sub",
            "operator*": "mul",
            "operator/": "div"
        }

        self.registered_converters = []

    def cpp_to_py_operator(self, name):
        if name.startswith("operator") and name not in self.operators:
            raise NotImplementedError("Cannot convert C++ operator '%s' to "
                                      "Python operator.")
        return self.operators.get(name, name)
