# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cppzmq(CMakePackage):
    """C++ binding for 0MQ"""

    homepage = "http://www.zeromq.org"
    url      = "https://github.com/zeromq/cppzmq/archive/v4.2.2.tar.gz"
    git      = "https://github.com/zeromq/cppzmq.git"

    version('develop', branch='master')
    version('4.3.0', sha256='27d1f56406ba94ee779e639203218820975cf68174f92fbeae0f645df0fcada4')
    version('4.2.2', 'bd809b47296e77fe9f192bd9dafd5cc3')

    depends_on('cmake@3.0.0:', type='build')
    depends_on('zeromq@4.2.5', when='@4.3.0')
    depends_on('zeromq@4.2.2', when='@4.2.2')
