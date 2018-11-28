#include<iostream>
#include<string>

using namespace std;

int main(){
	int T; cin >> T;
	for( int kase = 1; kase <= T; kase++ ){
		string s;
		int k, res = 0;
		cin >> s >> k;
		bool imp = false;
		for( int i = 0; i < int(s.length()); i++ ){
			if( i + k > int(s.length()) ){
				if( s[ i ] == '-' ){
					imp = true; break;
				}
				continue;
			}
			if( s[ i ] == '-' ){
				for( int j = i; j < i + k; j++ ){
					s[ j ] = (s[ j ] == '-'?'+':'-');
				}
				res++;
			}
			//cout << s << " " << res << endl;
		}
		if( imp ) cout << "Case #" << kase<<": IMPOSSIBLE" << endl;
		else cout << "Case #" << kase << ": " << res << endl;
	}
}
