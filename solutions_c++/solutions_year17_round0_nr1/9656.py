#include <bits/stdc++.h>

using namespace std;

char change(char c){
	if( c == '+' )
		return '-';
	else
		return '+';

}

int main(){
	int T, k;
	string s;

	scanf( "%d", &T );

	for(int n = 1; n <= T; n++){
		int count = 0;
		cin >> s;
		scanf( "%d", &k);
		///cout << s << " " << k << endl;

		for( string::iterator it = s.begin(); it != s.end(); it++ ){
			char c = *it;

			if( c == '-' ){
				//cout << distance(it, s.end()) << endl;
				if( distance(it, s.end()) < k ){
					count = -1;
					break;
				}

				*it = change(c);
				it++;
				for( int i = 0; i < k-1; i++ ){
					*it  = change(*it);
					it++;
					
				}
				//cout << s << endl;
				it = s.begin();
				count++;
			}
		}

		if( count == -1 )
			printf("Case #%d: IMPOSSIBLE\n", n);
		else
			printf("Case #%d: %d\n", n, count);

	}

}