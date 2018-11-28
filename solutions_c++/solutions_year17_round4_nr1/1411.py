#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <bitset>
#include <memory.h>

using namespace std;

struct state {
	int *o;
	int p;
	int rest;

	int sum() {
		return o[0] + o[1] + o[2] + o[3];
	}

	bool operator <(const state &other) const {
		if (p < other.p || p == other.p && rest < other.rest) {
			return true;
		}
		else if (p == other.p && rest == other.rest) {
			for (int i = 0; i < 4; i++) {
				if (o[i] < other.o[i]) {
					return true; 
				}
				else if (o[i] > other.o[i]) {
					return false;
				}
			}
			return false;
		}
		else {
			return false;
		}

	}
};

const int maxn = 111;
map<state, int> ans;

int go(state st) {
	if (ans.find(st) != ans.end()) {
		return ans[st];
	}
	int cur = 0;

	if (st.sum() == 0) {
		return 0;
	}

	for (int i = 0; i < st.p; i++) {
		if (st.o[i] > 0) {
			int *nexto = new int[4];
			nexto[0] = st.o[0];
			nexto[1] = st.o[1];
			nexto[2] = st.o[2];
			nexto[3] = st.o[3];
			nexto[i]--;
			state next = {nexto, st.p, (st.rest - i + st.p) % st.p};
			cur = max(cur, go(next));
		}
	}

	if (st.rest == 0) {
		cur++;
	}
	ans[st] = cur;
	return cur;
}

int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int n, p;
		cin >> n >> p;
		int *o = new int[4];
		o[0] = o[1] = o[2] = o[3] = 0;
		for (int i = 0; i < n; i++) {
			int q;
			cin >> q;
			o[q % p]++;
		}
		state st = { o, p, 0 };
		cout << "Case #" << test << ": " << go(st) << endl;

	}



	//system("pause");
	return 0;
}