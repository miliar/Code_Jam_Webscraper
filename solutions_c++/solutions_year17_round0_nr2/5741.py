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

bool check(int x){
	int last = 10;
	while(x > 0){
		int rem = x % 10;
		x /= 10;
		if(rem <= last){
			last = min(rem, last);
		}
		else{
			return 0;
		}
	}
	return 1;
}
int main(){
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++){
		int n, ans;
		cin >> n;
		for(int i = 1; i <= n; i++){
			if(check(i)) ans = i;
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
  return 0;
}