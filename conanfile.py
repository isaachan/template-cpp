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
        # self.run("git clone git@github.com:isaachan/template-cpp.git")
        self.run("git clone https://github.com/isaachan/template-cpp.git template")
        # Output to "source" folder
 
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="template")
        cmake.definitions["CMAKE_C_FLAGS"] = "-s"
        cmake.definitions["CMAKE_CXX_FLAGS"] = "-s"
        cmake.build()

    def package(self):
        #self.copy("app", dst="bin")
        #self.copy("template-cpp", dst="src")
        
        # General speaking, if CMake defines installation, it is better to reuse.
        cmake = CMake(self)
        cmake.configure(source_folder="template")
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

