from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        H1 = self.addHost( 'h1' )
        H2 = self.addHost( 'h2' )
        H3 = self.addHost( 'h3' )
        H4 = self.addHost( 'h4' )
        H5 = self.addHost( 'h5' )
        H6 = self.addHost( 'h6' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )


topos = { 'mytopo': ( lambda: MyTopo() ) }
