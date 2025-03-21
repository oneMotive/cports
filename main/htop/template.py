pkgname = "htop"
pkgver = "3.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-capabilities",
    "--enable-delayacct",
    "--enable-sensors",
    "--enable-unicode",
]
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "libcap-devel",
    "libnl-devel",
    "lm-sensors-devel",
    "ncurses-devel",
]
depends = [
    # dlopened
    "so:libnl-3.so!libnl",
    "so:libnl-genl-3.so!libnl",
    "so:libsensors.so.5!lm-sensors-libs",
]
pkgdesc = "Interactive process viewer"
license = "GPL-2.0-only"
url = "https://htop.dev"
source = f"https://github.com/htop-dev/htop/releases/download/{pkgver}/htop-{pkgver}.tar.xz"
sha256 = "feaabd2d31ca27c09c367a3b1b547ea9f96105fc41f4dfa799e2f49daad5de29"
# CFI cannot work with libsensors dlsym() stuff
hardening = ["vis", "!cfi"]
