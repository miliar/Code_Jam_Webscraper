
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
string work() {
	string s; 
	cin >> s ;
	bool isDone = false ; 
	int sz = s.size(); 
	while ( !isDone ) {
		if ( sz == 1 ) {
			isDone = true; 
			continue;
		}
		int i = 0; 
		for ( ; i < sz - 1  ;  i ++ ) {
			if  ( s[i]  >  s[i+1]) {
				break;
			}
		}
        if ( i == sz -1  && s[sz - 2] <= s[sz-1] ) {
        	isDone = true;
        	continue;
        }

        for ( int k = i+1 ; k < sz ; k++ )
        { 
         	s[k] = '9';
        }
        s[i] = s[i] - 1;
	} // while

    
    int x = 0; 
    for ( ; x < s.size(); x ++ ) 
    {
    	if ( s[x] !='0' )
    		break;
    }

    return s.substr(x);
}

int main () {
    int T;
    int ret = 0 ; 
    cin >> T; 
    RE(i , T) {
    	cout << "Case #" << i<<": " << work();
    	cout << endl;
    } 
	return 0;
}