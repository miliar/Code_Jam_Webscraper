#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<fstream>
using namespace std;

struct A {
	vector<int> v;
	bool operator <(const A &x) const {
		return v.size() > x.v.size();
	}
};
A a[1010];
int t[1010];
int main() {
	ofstream out("answer.txt");
	int T, kase;
	cin >> T;
	int N, C, M;
	int i, j, k, x, y;
	for (kase = 1; kase <= T; kase++) {
		out << "Case #" << kase << ": ";
		cin >> N >> C >> M;
		for (i = 1; i <= C; i++)
			a[i].v.clear();
		memset(t, 0, sizeof(t));

		for (i = 0; i < M; i++) {
			cin >> x >> y;
			t[x]++;
			a[y].v.push_back(x);
		}
		sort(a + 1, a + 1 + C);
		x = max((int) a[1].v.size(), t[1]);
		y = 0;
		for (i = 1; i <= N; i++) {
			y = max(y, t[i] - x);
		}
		out << x << ' ' << y << endl;
	}
	out.close();
	return 0;
}
