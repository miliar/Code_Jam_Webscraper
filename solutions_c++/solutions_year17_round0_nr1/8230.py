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


void solve(int t, string s, int k) {
	printf("Case #%d: ", t);
	int n = s.length();
	int answer = 0;
	for (int i = 0; i < n; i++) {
		if (s[i] == '-') {
			//dout(i);
			//dout(s);
			if (i+k <= n) {
				for (int j = i; j < i+k; j++) {
					s[j] = (s[j] == '-' ? '+' : '-');
				}
				answer++;
			} else {
				printf("IMPOSSIBLE\n");
				return;
			}
			//dout(s);
		}
	}
	printf("%d\n", answer);
}

void readData() {
	int t; cin >> t;
	FOR(i,t) {
		string s;
		int k;
		cin >> s >> k;
		solve(i+1, s, k);
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
