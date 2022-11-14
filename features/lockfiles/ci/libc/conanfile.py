from conans import ConanFile

required_conan_version = ">=1.28"

class LibCConan(ConanFile):
    name = "libc"
    version = "0.1"
    settings = "build_type"
    requires = "liba/[>0.0 <1.0]@user/testing"
