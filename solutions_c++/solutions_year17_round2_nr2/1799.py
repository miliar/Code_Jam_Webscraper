#include <stdio.h>
#include <iostream>
#include <vector>
#include <assert.h>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <memory.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
typedef long long ll;
int n, f[6];
string idx = "012345";
string clr = "ROYGBV";
string bin = "101010";
vector<string> parts;
int was[6];
bool IMP;
void add(int ORANGE, int BLUE, string &parts) {
	if (f[ORANGE]) {
		if (f[ORANGE] > f[BLUE]) {
			IMP = true;
			return;
		}
		for (int i = 0; i < f[ORANGE]; ++i) {
			parts += clr[ORANGE];
			parts += clr[BLUE];
		}
		f[BLUE] -= f[ORANGE];
		f[ORANGE] = 0;
	}
}
void fix(int ORANGE, int BLUE, string &parts) {
	if (!was[ORANGE])
		return;
	if (!f[BLUE]) {
		IMP = true;
		return;
	}
	--f[BLUE];
	parts = clr[BLUE] + parts;
}
bool can(char a, char b) {
	if (a == b)
		return false;
	for (int it = 0; it < 2; ++it) {
		if (a != 'B' && b == 'O')
			return false;
		if (a != 'R' && b == 'G')
			return false;
		if (a != 'Y' && b == 'V')
			return false;
		swap(a, b);
	}
	return true;
}
bool check(const string &sol) {
	if (sol.size() != n)
		return false;
	for (int i = 0; i < sol.size(); ++i)
		if (!can(sol[i], sol[(i + 1) % n]))
			return false;
	return true;
}
int main()
{
	//freopen("src.txt", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/B-small-attempt1.in", "r", stdin);
	freopen("C:/Users/ASUS/Downloads/B-small-attempt1.out", "w", stdout);
#define RED 0
#define ORANGE 1
#define YELLOW 2
#define GREEN 3
#define BLUE 4
#define VIOLET 5
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt) {
		printf("Case #%d: ", tt);
		scanf("%d", &n);
		for (int i = 0; i < 6; ++i) {
			scanf("%d", f + i);
			was[i] = f[i];
		}
		parts.clear();
		parts.resize(3);
		IMP = false;
		add(ORANGE, BLUE, parts[0]);
		add(GREEN, RED, parts[1]);
		add(VIOLET, YELLOW, parts[2]);
		if (!parts[0].empty() + !parts[1].empty() + !parts[2].empty()>1) {
			fix(ORANGE, BLUE, parts[0]);
			fix(GREEN, RED, parts[1]);
			fix(VIOLET, YELLOW, parts[2]);
		}
		if (!IMP && (!parts[0].empty() + !parts[1].empty() + !parts[2].empty() == 1)) {
			fix(ORANGE, BLUE, parts[0]);
			fix(GREEN, RED, parts[1]);
			fix(VIOLET, YELLOW, parts[2]);
			IMP = false;
		}
		string sol = parts[0] + parts[1] + parts[2];
		if (sol.empty()) {
			int count = 0;
			for (int i = 0; i < 6; ++i)
				if (was[i])
					++count;
			if (count == 2) {
				while (sol.size() != n) {
					for (int i = 0; i < 6; ++i)
						if (f[i]) {
							--f[i];
							sol += clr[i];
						}
				}
			}
		}
		while (sol.size() != n && !IMP) {
			IMP = true;
			for (int i = 0; i < 6; ++i) {
				if (!f[i])
					continue;
				if (sol.empty()) {
					sol += clr[i];
					--f[i];
					IMP = false;
					break;
				}
				if (sol.size() == 1 && can(clr[i], sol[0])) {
					sol += clr[i];
					--f[i];
					IMP = false;
					break;
				}
				if (sol.size() == 1)
					continue;
				for (int j = 0; j < sol.size(); ++j) {
					if (can(sol[j], clr[i]) && can(sol[(j + 1) % sol.size()], clr[i])) {
						sol.insert(sol.begin() + j + 1, clr[i]);
						--f[i];
						IMP = false;
						break;
					}
				}
				if (!IMP)
					break;
			}
		}
		if (IMP || !check(sol))
			sol = "IMPOSSIBLE";
		puts(sol.c_str());
	}
	return 0;
}