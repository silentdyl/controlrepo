node default {
     file {'/root/README':
     ensure => file,
     content => 'This is a readme.',
     } 
}
#may need to change this name later

node 'puppetmasterdylan' {
    include role::master_server
}
