#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
typedef long long ll;

int main( int argc, char * argv[] ) {

    ifstream fin;
    ofstream fout;
    fin.open( argv[1] );
    fout.open( "output.txt" );
    


    

    ll t;
    fin >> t;

   
    for( ll i = 0; i < t; i++ ) {

	vector < bool > cake;
	string str;
	
	fin >> str;

	for( ll j = 0; j < str.length(); j++ ) {
	    if( str.substr(j,1) == "-" ) {
		cake.push_back( 0 );
	    }
	    if( str.substr(j,1) == "+" ) {
		cake.push_back( 1 );
	    }
	}


	ll k;
	fin >> k;
	ll flips = 0;
	
	for( ll t = 0; t < cake.size()-k+1; t++ ) {
	    if( cake[t] == 0 ) {		
	        flips += 1;
		for( ll e = 0; e < k; e++ ) {
		    if( cake[t+e] == 0 ) {
		        cake[t+e] = 1;
		    }
		    else {
			if( cake[t+e] == 1 ) {
			    cake[t+e] = 0;
			}
		    }
		}
	    }

	    /*	    for( ll e = 0; e < cake.size(); e++ ) {
		cout << cake[e];
	    }
	    cout << endl;
	    */

	    
	}


	// traversal
	bool is_zero = 0;
	for( ll t = 0; t < cake.size(); t++ ) {
	    if( cake[t] == 0 ) {
		is_zero = 1;
	    }
	}
	if( is_zero == 1 ) {
	    fout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
	}
	if( is_zero == 0 ) {
	    fout << "Case #" << i+1 << ": " << flips << endl;
	}	       

    }
    return 0;
}
