#include <bits/stdc++.h>

using namespace std;


typedef long long ll;

vector < int> dig;

void getdigits(ll num ) {
    dig.clear();
    while ( num ) {
        dig.push_back ( num % 10 );
        num /= 10;
    }
    reverse ( dig.begin(), dig.end() ) ;
}
int brute (int x) {
    while ( 1 ) {
        getdigits(x);
        int flg = 1;
        for ( int i = 1; i < dig.size(); i++ ) {
            if ( dig[i] < dig[i - 1 ] ) {
                flg = 0;
                break;
            }
        }
        if ( flg ) return x;
        x --;
    } 
}
int main() {
	// your code goes here

	int t;
	cin >> t;
	for  ( int cs = 1; cs <= t; cs ++ ) {
	    	cout <<"Case " <<"#" <<cs <<": ";
	    ll num;
	    cin >> num;
	    //cout << brute ( num ) << endl;
		//continue;
	    getdigits(num);
	    if ( num >= 1 and num <= 9 ) {
	        cout << num << endl;
	        continue;
	    }
	    int i = 1;
	    for ( i = 1; i < dig.size(); i++ ) {
	        if ( dig[i] < dig[i-1] ) break;
	    }
	    if ( i == dig.size() ) {
	        cout << num << endl;
	        continue;
	    }
	    //check if all ones 
	    int of = 1;
	    int tt = i;
	    for (int i = 0; i < tt; i++ ) {
	        if (dig[i] != 1  ) of = 0;
	    }
	    if ( of ) {
	        for ( int i = 1; i < dig.size(); i++ ) cout <<"9";
	        cout << endl;
	        continue;
	    }
	    else 
	    { 
	       dig[tt- 1] -= 1;
	       for ( int i = tt - 2; i >= 0; i -- ) {
	           if ( dig [i] > dig[i+1] ) { 
				   dig[i] -- ;
				   dig[i+1] = 9;
				 }
	       }
	       for ( int i = 0; i < tt; i ++ ) cout << dig[i];
	       for ( int i = tt; i < dig.size( ); i ++ ) cout << 9;
	       cout << endl;
	    }
	}
	return 0;
}
