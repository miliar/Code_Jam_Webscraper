#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <string>
#include <map>
#include <set>
using namespace std;

void solve(int test) {
	int N;
	cin >> N;
	int R, O, Y, G, B, V;
	cin >> R >> O >> Y >> G >> B >> V;
	if (O > 0 || G > 0 || V > 0)
		throw 1;
	printf("Case #%d: ", test);
	if (R > N / 2 || Y > N / 2 || B > N / 2) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	string s = "";
	vector<char> res(N);
	int mas1[] = { R, Y, B };
	char mas2[] = { 'R', 'Y', 'B' };
	if (mas1[0] < mas1[1]) {
		swap(mas1[0], mas1[1]);
		swap(mas2[0], mas2[1]);
	}
	if (mas1[0] < mas1[2]) {
		swap(mas1[0], mas1[2]);
		swap(mas2[0], mas2[2]);
	}
	if (mas1[1] < mas1[2]) {
		swap(mas1[1], mas1[2]);
		swap(mas2[1], mas2[2]);
	}
	for (int tt = 0; tt < 3; ++tt) {
		for (int i = 0; i < mas1[tt]; ++i) {
			s += mas2[tt];
		}
	}
	int cur = 0;
	for (int i = 0; i < N; i += 2) {
		res[i] = s[cur++];
	}
	for (int i = 1; i < N; i += 2) {
		res[i] = s[cur++];
	}
	for (int i = 0; i < N; ++i) {
		if (res[i] == res[(i + 1) % N] || res[i] == res[(i + N - 1) % N]) {
			cerr << test << endl;
			throw 1;
		}
	}
	for (int i = 0; i < N; ++i)
		cout << res[i];
	cout << endl;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		solve(i + 1);
	}
	return 0;
}