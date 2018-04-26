from conans import ConanFile, CMake, tools

class OpenIGTLinkConan(ConanFile):
    name = "OpenIGTLink"
    version = "3.0"
    description = "Open IGT Link"
    url = "https://github.com/openigtlink/OpenIGTLink.git"
    license = ""
    exports = []
    source_subfolder = "source_subfolder"
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = ""
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/openigtlink/OpenIGTLink.git")
        self.run("cd OpenIGTLink && git checkout v3.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["USE_GTEST"] = "OFF"
        cmake.definitions["BUILD_SHARED_LIBS"] = "ON"
        cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["CMAKE_INSTALL_PREFIX"] = "install"
        cmake.configure(source_folder="OpenIGTLink")
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("*.h", dst="include", src="install/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["OpenIGTLink"]
