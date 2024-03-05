from mininet.topo import Topo

class myTopo( Topo ):

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        H1 = self.addHost( 'H1' )
        H2 = self.addHost( 'H2' )
        H3 = self.addHost( 'H3' )
        H4 = self.addHost( 'H4' )
        H5 = self.addHost( 'H5' )
        H6 = self.addHost( 'H6' )

        # Add switches
        S1 = self.addSwitch( 'S1' )
        S2 = self.addSwitch( 'S2' )

        # Add links
        self.addLink( H1, S1 )
        self.addLink( H2, S1 )
        self.addLink( H6, S1 )
        self.addLink( H3, S2 )
        self.addLink( H4, S2 )
        self.addLink( H5, S2 )

        self.addLink( S1, S2 )


topos = { 'mytopo': ( lambda: myTopo() ) }
