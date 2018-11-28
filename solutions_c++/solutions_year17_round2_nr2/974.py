#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdio>

using namespace std;

#define REP(i, a, b)		for(i = int(a); i <= int(b); i++)
#define FOR(i, N)			REP(i, 0, N-1)

#define REPI(it, a, b)		for(it = (a); it != (b); it++)
#define FORI(it, v)			REPI(it, All(v))

#define All(v)				v.begin(), v.end()

#define VI					vector<int>
#define VVI					vector<VI>

#define VD					vector<double>

#define St					pair<int, string>
#define num					first
#define val					second
#define VSt					vector<St>

string Two(int n, string str) {
	string ans = "";
	while (n--)
		ans += str;
	return ans;
}

int main() {
	ifstream cin("input2.txt");
	ofstream cout("output1a.txt");
	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i;
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		// Only two
		if (O + B == N || G + R == N || V + Y == N) {
			if (O != B || G != R || V != Y) {
				cout << "Case #" << t << ": IMPOSSIBLE" << endl;
				continue;
			}
			if (O > 0) {
				cout << "Case #" << t << ": " << Two(O, "OB") << endl;
				continue;
			}
			if (G > 0) {
				cout << "Case #" << t << ": " << Two(G, "GR") << endl;
				continue;
			}
			if (V > 0) {
				cout << "Case #" << t << ": " << Two(V, "VY") << endl;
				continue;
			}
		}

		// Mixed won't work
		if ((O >= B && O != 0) || (G >= R && G != 0) || (V >= Y && V != 0)) {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}

		// Remove mixed and keep going with unique
		B -= O;
		R -= G;
		Y -= V;

		VSt Colors;
		Colors.push_back(St(B, "B"));
		Colors.push_back(St(R, "R"));
		Colors.push_back(St(Y, "Y"));
		sort(All(Colors));
		reverse(All(Colors));

		if (Colors[0].num > Colors[1].num + Colors[2].num) {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}

		string ans = "";
		// Make Colors[1] at the same level as Colors[2]
		int diff = Colors[1].num - Colors[2].num;
		ans += Two(diff, Colors[0].val + Colors[1].val);
		Colors[0].num -= diff;
		Colors[1].num -= diff;

		// Make All Colors at the same level
		diff = Colors[0].num - Colors[1].num;
		ans += Two(diff, Colors[0].val + Colors[1].val + Colors[0].val + Colors[2].val);
		Colors[0].num -= 2*diff;
		Colors[1].num -= diff;
		Colors[2].num -= diff;

		// Add the remaining one by one
		ans += Two(Colors[0].num, Colors[0].val + Colors[1].val + Colors[2].val);

		// Replace first occurance of each character
		if (O != 0) {
			int pos = ans.find_first_of('B');
			ans.replace(pos, 1, Two(O, "BO") + "B");
		}
		if (G != 0) {
			int pos = ans.find_first_of('R');
			ans.replace(pos, 1, Two(G, "RG") + "R");
		}
		if (V != 0) {
			int pos = ans.find_first_of('Y');
			ans.replace(pos, 1, Two(V, "YV") + "Y");
		}

		cout << "Case #" << t << ": " << ans << endl;
	}
}