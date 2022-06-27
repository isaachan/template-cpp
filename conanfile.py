from conans import ConanFile, CMake, tools


class AppConan(ConanFile):
    name = "template-cpp"
    version = "0.0.2"
    license = "MIT"
    # url = "https://github.com/hello/hello.git"
    description = "Hello conan"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"


    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()
    #    cmake.install()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.install()


    def package_info(self):
        self.cpp_info.bindirs = ["bin"]
        self.cpp_info.srcdirs = ["src"]


    def deploy(self):
        # Deploy the executables from this eclipse/mosquitto package
        self.copy("*", src="bin", dst="bin")
        # Deploy the shared libs from this eclipse/mosquitto package
        self.copy("*.so*", src="lib", dst="bin")
        # Deploy all the shared libs from the transitive deps
        self.copy_deps("*.so*", src="lib", dst="bin")

