node default {
     file {'/root/README':
     ensure => file,
     content => 'This is a readme.',
     } 
}

node 'puppetmasterdylan' {
    include role::master_server
}