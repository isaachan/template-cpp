from conans import ConanFile, CMake, tools


class AppConan(ConanFile):
    name = "app"
    version = "0.0.2"
    license = "MIT"
    # url = "https://github.com/hello/hello.git"
    description = "Hello conan"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone git@github.com:isaachan/template-cpp.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="template-cpp")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="template-cpp")
        # self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("app", dst="bin", keep_path=False)
        # self.copy("*.so", dst="lib", keep_path=False)
        # self.copy("*.dylib", dst="lib", keep_path=False)
        # self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["app"]

    def deploy(self):
        # Deploy the executables from this eclipse/mosquitto package
        self.copy("*", src="bin", dst="bin")
        # Deploy the shared libs from this eclipse/mosquitto package
        self.copy("*.so*", src="lib", dst="bin")
        # Deploy all the shared libs from the transitive deps
        self.copy_deps("*.so*", src="lib", dst="bin")

