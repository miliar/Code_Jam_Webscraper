#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;

int n, m;
char str[33][33];

int main(){
	int t;
	cin >> t;
	for(int tt=1; tt<=t; tt++){
		cin >> n >> m;
		for(int i=0; i<n; i++){
			cin >> str[i];
			char cur = '?';
			for(int j=0; j<m; j++){
				if(str[i][j] != '?'){
					cur = str[i][j];
				}
				str[i][j] = cur;
			}
			for(int j=m-1; j>=0; j--){
				if(str[i][j] != '?'){
					cur = str[i][j];
				}
				str[i][j] = cur;
			}
		}
		for(int i=0; i<m; i++){
			char cur = '?';
			for(int j=0; j<n; j++){
				if(str[j][i] != '?'){
					cur = str[j][i];
				}
				str[j][i] = cur;
			}
			for(int j=n-1; j>=0; j--){
				if(str[j][i] != '?'){
					cur = str[j][i];
				}
				str[j][i] = cur;
			}
		}
		printf("Case #%d:\n", tt);
		for(int i=0; i<n; i++) cout << str[i] << endl;
	}
}

