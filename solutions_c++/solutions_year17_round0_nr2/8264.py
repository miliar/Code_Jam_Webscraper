#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <algorithm>
using namespace std;

#define dout(x) cerr << #x << " = " << x << endl;
template<typename T>
ostream& operator<< (ostream& out, const vector<T>& v) {
	out << "[";
	for (auto vi : v)
		out << vi << ", ";
	out << "]";
	return out;
}

#define ALL(x) (x).begin(), (x).end()
#define FOR(i, n) for(int i=0;i<(n);++i)
#define pb push_back
#define fr first
#define sc second
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector <int> vi;
int DX[] = {  0, +1,  0, -1,  0};
int DY[] = {  +1, 0, -1,  0,  0};

int readInt() {
	int temp;
	scanf("%d", &temp);
	return temp;
}


void solve(int t, ll n) {
	ll m = n;
	string s = to_string(n);
	for (int i = 1; i < s.length(); i++) {
		if (s[i-1] > s[i]) {
			// not tidy 
			i--;
			s[i]--;
			while (i > 0 && s[i-1] > s[i]) {
				i--;
				s[i]--;
			}
			for (int j = i+1; j < s.length(); j++) 
				s[j] = '9';
			break;
		}
	}
	m = stoll(s);
	printf("Case #%d: %lld\n", t, m);
}

void readData() {
	int t;
	cin >> t;
	FOR(i,t) {
		ll n;
		cin >> n;
		solve(i+1,n);
	}
}

int main() {
#ifdef LOCAL_TEST
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	readData();
	
	return 0;
}
