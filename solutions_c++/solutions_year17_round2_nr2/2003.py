#include <stdio.h>
#include <functional>
#include <vector>
#include <algorithm>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <queue>
#include <string>
#include <iostream>

using namespace std;
typedef long long ll;

string RYB(int R, int Y, int B) {
	string s;
	int N = R + Y + B;
	s.resize(N);
	vector<pair<int, char>> v;
	v.push_back({ R, 'R' });
	v.push_back({ Y, 'Y' });
	v.push_back({ B, 'B' });
	sort(v.begin(), v.end(), greater<pair<int, char>>());

	int two = 3 * v[0].first - N;
	int three = v[0].first - two;
	if (three < 0) return "IMPOSSIBLE";
	for (int i = 0; i < three; i++) {
		s[i * 3] = v[0].second;
		s[i * 3 + 1] = v[1].second;
		s[i * 3 + 2] = v[2].second;
	}
	for (int i = 0; i < two; i++) {
		s[3 * three + 2 * i] = v[0].second;
		if (three + i >= v[1].first) {
			s[3 * three + 2 * i + 1] = v[2].second;
		}
		else {
			s[3 * three + 2 * i + 1] = v[1].second;
		}
	}
	return s;
}
string ROYGBV(int R, int O, int Y, int G, int B, int V) {
	string ans;
	B -= O+1;
	G -= R+1;
	V -= Y+1;
	return "";
}


int main(void) {
	freopen("c:\\cdj\\B-small-2.in", "r", stdin);
	freopen("c:\\cdj\\B-small-2.txt", "w", stdout);
	int T; scanf("%d\n", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N; int R, O, Y, G, B, V; scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);
		string ans = RYB(R, Y, B);
		//cout << "Case #" << tc << " " << ans << endl;
		printf("Case #%d: %s\n", tc, ans.c_str());
	}

}