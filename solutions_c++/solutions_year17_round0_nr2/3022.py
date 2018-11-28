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
	cin >> s;
	for(int i = 0; i < 20; ++i){
		for(int j = 0; j + 1 < (int)s.size(); ++j){
			if(s[j] > s[j + 1]){
				s[j]--;
				for(int k = j + 1; k < (int)s.size(); ++k){
					s[k] = '9';
				}
				break;
			}
		}
	}
	int k = 0;
	while(k < s.size() && s[k] == '0') k++;
	for(int i = k; i < (int)s.size(); ++i) putchar(s[i]);
	cout << endl;
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