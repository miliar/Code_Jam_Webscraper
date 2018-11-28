#include <iostream>
#include <string.h>
#include <vector>
#include <string>
#include <limits.h>
#include <stdint.h>
#include <algorithm>
#include <tuple>
#include <iomanip>
#include <set>
using namespace std;

struct H {
	int R; int O; int Y; int G; int B; int V;
	int size() const { return R + O + Y + G + B + V; }
};

bool operator<(const H& a, const H&b) {
	if (a.R < b.R) return true;
	if (a.R > b.R) return false;
	if (a.O < b.O) return true;
	if (a.O > b.O) return false;
	if (a.Y < b.Y) return true;
	if (a.Y > b.Y) return false;
	if (a.G < b.G) return true;
	if (a.G > b.G) return false;
	if (a.B < b.B) return true;
	if (a.B > b.B) return false;
	if (a.V < b.V) return true;
	if (a.V > b.V) return false;
	return false;
}

std::set<H> memo;

bool test(int T, int C, H h)
{
	if (memo.find(h) != memo.end()) return false;

	if (h.size() == 1) {
		if (T != 0 && C != 0 && h.R == 1) { cout << 'R'; return true; }
		if (T != 1 && C != 1 && h.O == 1) { cout << 'O'; return true; }
		if (T != 2 && C != 2 && h.Y == 1) { cout << 'Y'; return true; }
		if (T != 3 && C != 3 && h.G == 1) { cout << 'G'; return true; }
		if (T != 4 && C != 4 && h.B == 1) { cout << 'B'; return true; }
		if (T != 5 && C != 5 && h.V == 1) { cout << 'V'; return true; }
	} else {
		if (C != 0 && h.R > 0 && test(T, 0, {h.R-1, h.O, h.Y, h.G, h.B, h.V})) {
			cout << 'R';
			return true;
		} else if (C != 1 && h.O > 0 && test(T, 1, {h.R, h.O-1, h.Y, h.G, h.B, h.V})) {
			cout << 'O';
			return true;
		} else if (C != 2 && h.Y > 0 && test(T, 2, {h.R, h.O, h.Y-1, h.G, h.B, h.V})) {
			cout << 'Y';
			return true;
		} else if (C != 3 && h.G > 0 && test(T, 3, {h.R, h.O, h.Y, h.G-1, h.B, h.V})) {
			cout << 'G';
			return true;
		} else if (C != 4 && h.B > 0 && test(T, 4, {h.R, h.O, h.Y, h.G, h.B-1, h.V})) {
			cout << 'B';
			return true;
		} else if (C != 5 && h.V > 0 && test(T, 5, {h.R, h.O, h.Y, h.G, h.B, h.V-1})) {
			cout << 'V';
			return true;
		}
	}
	memo.insert(h);
	return false;
}

bool solve(int T, H h)
{
	memo.clear();
	if (h.size() == 0 || test(T, T, h)) {
		switch (T) {
		case 0: { cout << 'R'; return true; } break;
		case 1: { cout << 'O'; return true; } break;
		case 2: { cout << 'Y'; return true; } break;
		case 3: { cout << 'G'; return true; } break;
		case 4: { cout << 'B'; return true; } break;
		case 5: { cout << 'V'; return true; } break;
		}
	}
	return false;
}

int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		cout << "Case #" << i << ": ";
		if (R > 0 && solve(0, {R-1, O, Y, G, B, V})) {
		} else if (O > 0 && solve(1, {R, O-1, Y, G, B, V})) {
		} else if (Y > 0 && solve(2, {R, O, Y-1, G, B, V})) {
		} else if (G > 0 && solve(3, {R, O, Y, G-1, B, V})) {
		} else if (B > 0 && solve(4, {R, O, Y, G, B-1, V})) {
		} else if (V > 0 && solve(5, {R, O, Y, G, B, V-1})) {
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}

	return 0;
}
