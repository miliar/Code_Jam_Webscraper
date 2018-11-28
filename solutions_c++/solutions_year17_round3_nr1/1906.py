#include <fstream>
#include <algorithm>
#include <iostream>
#include <vector>
#define PI 3.1415926535897932384626433832795028841971
using namespace std;
vector<pair<int, int> > pancakes;
long long d[1001][1001];
int N, K;
long long solve(int x, int k) {
	if (k == K) {
		return (2 * (long long)pancakes[x].first * pancakes[x].second);
	}
	long long &res = d[x][k];
	if (res != -1) {
		return res;
	}
	for (int i = x - 1; i >= 0; i--) {
		res = max(res, solve(i, k + 1) + (2 * (long long)pancakes[x].first * pancakes[x].second));
	}
	return res;
}

int main() {
	int C;
	ifstream in("input.in");
	ofstream out("output.out");
	int r, h, i,j;
	long long ans = -1;
	in >> C;
	out.precision(9);
	out.setf(ios::fixed);
	for (int c = 1; c <= C; c++) {
		in >> N >> K;
		pancakes.clear();
		for (i = 0; i < N; i++) {
			in >> r >> h;
			pancakes.push_back(make_pair(r, h));
			for (j = 0; j < N; j++) {
				d[i][j] = -1;
			}
		}
		sort(pancakes.begin(), pancakes.end());
		ans = -1;
		for (i = N - 1; i >= 0; i--) {
			ans = max(ans, solve(i, 1) + (long long)pancakes[i].first * pancakes[i].first);
		}
		out << "Case #" << c << ": " << PI * (double)ans << endl;
	}
	return 0;
}