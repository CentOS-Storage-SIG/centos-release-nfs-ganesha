centos-release-nfs-ganesha28 provides the YUM repository file for packages
of the CentOS Storage SIG that are used with NFS-Ganeha 2.8.

This package needs to be built against the following targets so that the
packages land at the right tag for inclusion in CentOS Extras:

 - core6-extras-common-el6.centos (tag: core6-extras-common-candidate)
 - core7-extras-common-el7.centos (tag: core7-extras-common-candidate)

Build the package ike this:


    $ rpmbuild -bs \
               --define "_sourcedir $PWD" --define "_srcrpmdir $PWD" \
               --define "dist .el7.centos" \
               centos-release-nfs-ganehsha28.spec

    $ cbs \
           build core7-extras-common-el7.centos \
           centos-release-nfs-ganehsa28-1.0-1.el7.centos.src.rpm

