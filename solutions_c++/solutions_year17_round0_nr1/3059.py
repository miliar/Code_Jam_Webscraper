#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
#define fs first
#define sc second
#define pb push_back
const int mod = 1000000007;
const int N = 400004;

string s;
void solve(){
	int k;
	cin >> s >> k;
	int n = s.size();
	int cnt = 0;
	for(int i = 0; i + k <= n; ++i){
		if(s[i] == '-'){
			for(int j = 0; j < k; ++j){
				s[i + j] = s[i + j] == '+' ? '-' : '+';
			}
			cnt++;
		}
	}
	for(int i = 0; i < n; ++i) if(s[i] == '-'){
		puts("IMPOSSIBLE");
		return;
	}
	cout << cnt << endl;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
}