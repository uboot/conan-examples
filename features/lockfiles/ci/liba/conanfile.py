from conans import ConanFile, tools

required_conan_version = ">=1.28.0"

class PkgaConan(ConanFile):
    name = "liba"
    version = "0.1"
    settings = "build_type"
