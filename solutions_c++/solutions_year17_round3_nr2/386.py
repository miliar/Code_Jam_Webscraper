#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdio>
#include <limits>

using namespace std;

#define REP(i, a, b)		for(i = int(a); i <= int(b); i++)
#define FOR(i, N)			REP(i, 0, N-1)

#define REPI(it, a, b)		for(it = (a); it != (b); it++)
#define FORI(it, v)			REPI(it, All(v))

#define All(v)				v.begin(), v.end()

#define VI					vector<long long>
#define VVI					vector<VI>

#define VD					vector<double>
#define VVD					vector<VD>

#define II					pair<int, int>
#define St					pair<II, int>
#define VSt					vector<St>
#define st					first.first
#define en					first.second
#define val					second

const double INF = numeric_limits<double>::infinity();
const double PI = 3.14159265358979323846;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i, j;
		int Ac, Aj;
		cin >> Ac >> Aj;

		VSt V;
		int n1, n2;
		FOR(i, Ac) {
			cin >> n1 >> n2;
			V.push_back(St(II(n1, n2), 1));
		}
		FOR(i, Aj) {
			cin >> n1 >> n2;
			V.push_back(St(II(n1, n2), 0));
		}
		sort(All(V));

		VI tot(2, 720);
		FOR(i, V.size())
			tot[V[i].val] -= V[i].en - V[i].st;

		int ans = 0;
		VVI between(2, VI());
		FOR(i, V.size()) {
			int cur = i;
			int nxt = (i + 1) % V.size();
			if (V[i].val == V[nxt].val) {
				int Value = V[i].val;
				int curEnd = V[i].en;
				int nxtStart = nxt > cur ? V[nxt].st : V[nxt].st + 1440;
				between[Value].push_back(nxtStart - curEnd);
			}
			else
				ans++;
		}
		sort(All(between[0]));
		sort(All(between[1]));

		FOR(i, 2) {
			FOR(j, between[i].size()) {
				if (between[i][j] > tot[i]) break;
				tot[i] -= between[i][j];
			}
			ans += (between[i].size() - j) * 2;
		}
		
		char Ans[100];
		sprintf(Ans, "Case #%d: %d", t, ans);
		cout << Ans << endl;
	}
}