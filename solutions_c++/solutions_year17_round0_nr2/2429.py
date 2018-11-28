#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef unsigned long long ll;

bool ok(ll a) {
	int last = 9;
	for(int i = 0; i < 20; ++i) {
		if(a%10 > last) return false;
		last = a%10;
		a/=10;
	}
	return true;
}

vi ans;

int main() {
	ios::sync_with_stdio(0); cin.tie();
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		ans.clear();
		ll n;
		cin >> n;
		while(!ok(n)) {
			ans.push_back(9);
			n = n/10-1;
		}
		while(n) {
			ans.push_back(n%10);
			n/=10;
		}
		cout << "Case #" << t << ": ";
		for(int i = ans.size()-1; i >=0; --i)
			cout << ans[i];
		cout << "\n";
	}
	return 0;
}