#include "bits/stdc++.h"

using namespace std;

const int N = 7e3 + 5;
const int M = 1e5 + 5;
const int LN = 17;
const int SQRTN = 325;
const double PI = acos(-1.0);
const double EPS = 1e-7;
const int INF = 1e9;

typedef long long ll;
typedef long double ld;

bool check(int m, string s, int n, int k){
	int flips = 0;
	for(int i = 0; i < n; i++){
		if(s[i] == '-'){
			if(i + k <= n){
				flips++;
				for(int j = i; j < i + k; j++){
					if(s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
	}
	for(int i = 0; i < n; i++) if(s[i] == '-') return 0;
	return (flips <= m);
}
int main(){
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++){
		string s;
		int k;
		cin >> s >> k;
		int n = s.size();
		int lo = 0, hi = n, poss = -1;
		while(lo < hi){
			int mid = (lo + hi)/2;
			if(check(mid,s,n,k)) hi = mid, poss = 1;
			else lo = mid + 1;
		}
		if(poss == -1) cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << tc << ": " << lo << endl;
	}
  return 0;
}