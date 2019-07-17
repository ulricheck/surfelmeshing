from conans import ConanFile, CMake
from conans import tools
from conans.tools import os_info, SystemPackageTool
import os, sys
import sysconfig
from io import StringIO

class SurfelMeshingConan(ConanFile):
    name = "surfelmeshing"
    version = "0.1"

    description = "Surfel Meshing from rgbd-video"
    url = "https://github.com/ulricheck/surfelmeshing"
    license = "GPL"

    short_paths = True
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    requires = (
        "Boost/1.65.1@camposs/stable",
        "eigen/3.3.7@camposs/stable",
        "glew/2.1.0@camposs/stable",
        "cuda_dev_config/1.0@camposs/stable",
        "glog/0.3.5@bincrafters/stable",
        "gflags/2.2.1@bincrafters/stable",
        "qt/5.12.2-r1@ircad/testing",
        "zlib/1.2.11@camposs/stable",
        "pcl/1.9.1@camposs/stable",
        "gmp/6.1.2@bincrafters/stable",
    )

    options = {
        "shared": [True, False],
   }
    default_options = {
        "shared": False,
        "glew:shared": True,
    }

    # all sources are deployed with the package
    exports_sources = "applications/*", "cmake/*", "libvis/*", "LICENSE", "README.md", "screenshot.jpg", "CMakeLists.txt"

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()
        cmake.install()


    def imports(self):
        self.copy(src="bin", pattern="*.dll", dst="./bin") # Copies all dll files from packages bin folder to my "bin" folder
        self.copy(src="lib", pattern="*.dll", dst="./bin") # Copies all dll files from packages bin folder to my "bin" folder
        self.copy(src="lib", pattern="*.dylib*", dst="./lib") # Copies all dylib files from packages lib folder to my "lib" folder
        self.copy(src="lib", pattern="*.so*", dst="./lib") # Copies all so files from packages lib folder to my "lib" folder
        self.copy(src="lib", pattern="*.a", dst="./lib") # Copies all static libraries from packages lib folder to my "lib" folder
        self.copy(src="lib/qt5", pattern="*", dst="./lib/qt5", keep_path=True) # Copies all qt5 plugin libraries from packages lib folder to my "lib" folder
        self.copy(src="bin", pattern="*", dst="./bin") # Copies all applications
