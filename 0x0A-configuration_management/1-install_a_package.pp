#!/usr/bin/env pup
# install a package
package { 'flask':
  ensure   => 'installed',
  provider => 'pip3'
}
