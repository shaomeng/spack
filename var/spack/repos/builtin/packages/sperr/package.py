# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Sperr(CMakePackage):
    """SPERR is a lossy scientific (floating-point) data compressor that can
    perform either error-bounded or size-bounded data compression"""

    # Package info
    homepage = "https://github.com/NCAR/SPERR"
    url = "https://github.com/NCAR/SPERR/archive/refs/tags/v0.7.1.tar.gz"
    git = "https://github.com/NCAR/SPERR.git"
    maintainers("shaomeng", "robertu94")

    # Versions
    version("main", branch="main")
    version("0.7.1", sha256="1c3f46200be365427d1f57f5873f1b0b6dbcd297de4603a47a7fa3f41b273d79")
    version("0.6.2", sha256="d986997e2d79a1f27146ad02c623359976a1e72a1ab0d957e128d430cda3782d")
    version("0.5", sha256="20ad48c0e7599d3e5866e024d0c49648eb817f72ad5459f5468122cf14a97171")

    depends_on("git", type="build")
    depends_on("pkgconfig", type=("build"))

    variant("shared", description="build shared libaries", default=True)
    variant("openmp", description="use openmp in 3D inputs", default=True)
    variant("utilities", description="build SPERR CLI utilities", default=True)

    def cmake_args(self):
        # ensure the compiler supports OpenMP if it is used
        if "+openmp" in self.spec:
            self.compiler.openmp_flag

        args = [
            self.define_from_variant("BUILD_SHARED_LIBS", "shared"),
            self.define_from_variant("USE_OMP", "openmp"),
            self.define_from_variant("BUILD_CLI_UTILITIES", "utilities"),
            "-DSPERR_PREFER_RPATH=OFF",
            "-DBUILD_UNIT_TESTS=OFF",
        ]
        return args
