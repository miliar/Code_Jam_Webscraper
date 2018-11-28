
#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
// #include <cinttypes> // C++11?
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <new>
#include <algorithm>
#include <iostream>
#include <iostream>
#include <sstream> 
using namespace std;
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define RE(i, n) FOR(i, 1, n)
typedef vector<int> Vint;
typedef vector<int>::iterator Vit;
template <class _T> inline string tostr(const _T &a) { stringstream os(""); os << a; return os.str(); }
bool work(int & ret ) {
	string s; 
	int k;
	cin >> s >> k;
    ret =0 ;
    
    while (1 ) {
	     int i =0;
	    for (  ; i < s.size() ; ++i ) {
	    	if( s[i] == '-' )
	    		break;
	    }
	    if ( i == s.size() ) 
	    {
	    	return true;
	    }
	    if ( i + k > s.size() ) {
	    	return false;
	    }
	   	    	ret ++;
	    for ( int q = 0; q < k ; q ++ ) {
	    	if ( s[q+i] == '-') {
	    	    s[q+i] = '+';	
	    	}  else {
	    		s[q+i] = '-';
	    	}

	    }  	
    }




	return false;
}

int main () {
    int T;
    int ret = 0 ; 
    cin >> T; 
    RE(i , T) {
    	cout << "Case #" << i<<": " << ( work(ret) ? tostr(ret) : "IMPOSSIBLE");
    	cout << endl;
    } 
	return 0;
}