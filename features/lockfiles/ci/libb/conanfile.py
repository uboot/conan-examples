from conans import ConanFile

required_conan_version = ">=1.28"

class LibBConan(ConanFile):
    name = "libb"
    version = "0.1"
    settings = "build_type"
    requires = "liba/[>0.0 <1.0]@user/testing"
