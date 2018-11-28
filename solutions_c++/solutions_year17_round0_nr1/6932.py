#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("b.txt","w",stdout);
	int t;
	cin >> t;
	for( int i = 1; i <= t; i++ ){
		string s;
		int k;
		cin >> s >> k;
		printf("Case #%d: ", i);
		int l = s.size();
		int ans = 0;
		for( int n = 0; n <= l - k; n++ ){
			if( s[n] == '-' ){
				int d = n;
				for( int j = 0; j < k; j++ ){
					if( s[d] == '+'){
						s[d] = '-';
					}
					else{
						s[d] = '+';
					}
					d++;
				}
				ans++;
			}
		}
		int mi = 0;
		for( int j = l - k; j < l; j++ ){
			if( s[j] == '-' ){
				mi++;
			}
		}
		if( mi != 0 && mi < k ){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if( mi == k ){
			ans++;
		}
		cout << ans << endl;
	}
}