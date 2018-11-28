#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <set>

#define IN_FILE "B-large.in"
#define OUT_FILE "outL.txt"

using namespace std;

typedef long long ll;
typedef long double ld;

int K[300][722];
int segcost[300];
int segval[300];
int intval[1445];

set< pair<pair<int, pair<int,int> >, pair<int, int>> > iset;

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int t;
	int tc = 1;
	cin >> t;
	while (t--) {
		iset.clear();
		int ct = 720, jt = 720;
		for (int i = 0; i <= 1440; i++)
			intval[i] = 0;
		int ac, aj;
		cin >> ac >> aj;
		for (int i = 0; i < ac; i++) {
			int c, d;
			cin >> c >> d;
			for (int j = c; j < d; j++)
				intval[j] = 1;
			ct -= d - c;
		}
		for (int i = 0; i < aj; i++) {
			int ji, ki;
			cin >> ji >> ki;
			for (int j = ji; j < ki; j++)
				intval[j] = 2;
			jt -= ki - ji;
		}
		int lastc = -1, lastj = -1;
		int start = -1,end = -1;
		for (int i = 0; i < 1440; i++) {
			if (intval[i]) {
				start = i;
				break;
			}
		}
		ll ans = 0;
		if (start == -1)
			ans = 2;
		else {
			for (int i = 1440 - 1; i >= 0; i--) {
				if (intval[i]) {
					end = i;
					break;
				}
			}
			int ocost = -1;
			if (intval[start] != intval[end])
				ocost = 1;
			else if (intval[start] == 1)
				ocost = 0;
			else
				ocost = 2;
			int len = end - start + 1;
			len = 1440 - len;
			int dir = -1;
			if (intval[end] == 1)
				dir = 1;
			iset.insert(make_pair(make_pair(ocost,make_pair(len,dir)), make_pair(end+1,1440+start-1)));
			int statechange = start;
			for (int i = start+1; i <= end; i++) {
				if (intval[i] != intval[statechange]) {
					if (!intval[statechange]) {
						int ilen = i - statechange;
						int icost = 1;
						int prev = intval[statechange - 1];
						int nxt = intval[i];
						if (prev == nxt) {
							if (prev == 1)
								icost = 0;
							else
								icost = 2;
						}
						int dir = 1;
						if (nxt == 1)
							dir = -1;
						pair<int,int> ival = make_pair(statechange, i - 1);
						iset.insert(make_pair(make_pair(icost, make_pair(ilen,dir)), ival));
						
					}
					statechange = i;
				}
			}
			if (!t)
				int adsfawfw = 1;
			while (ct&&iset.size()) {
				auto it = iset.begin();
				if (it->first.first == 2)
					break;
				if (it->first.second.first > ct) {
					int ist = it->second.first;
					int est = it->second.second;
					int dir = it->first.second.second;
					if (dir == -1)
						swap(ist, est);
					for (int i = 0; i < ct; i++) {
						int focus = ist + (i*dir);
						if (focus < 0)
							focus += 1440;
						intval[(focus) % 1440] = 1;
					}
					ct = 0;
					break;
				}
				else {
					int ist = it->second.first;
					int est = it->second.second;
					int dir = it->first.second.second;
					if (dir == -1)
						swap(ist, est);
					for (int i = 0; i < it->first.second.first; i++) {
						int focus = ist + (i*dir);
						if (focus < 0)
							focus += 1440;
						intval[(focus) % 1440] = 1;
					}
					ct -= it->first.second.first;
				}
				iset.erase(iset.begin());
			}
			if (ct) {
				while (ct&&iset.size()) {
					auto it = iset.end();
					it--;
					if (it->first.second.first > ct) {
						int ist = it->second.first;
						int est = it->second.second;
						int dir = it->first.second.second;
						if (dir == -1)
							swap(ist, est);
						for (int i = 0; i < ct; i++) {
							int focus = ist + (i*dir);
							if (focus < 0)
								focus += 1440;
							intval[(focus) % 1440] = 1;
						}
						ct = 0;
						break;
					}
					else {
						int ist = it->second.first;
						int est = it->second.second;
						int dir = it->first.second.second;
						if (dir == -1)
							swap(ist, est);
						for (int i = 0; i < it->first.second.first; i++) {
							int focus = ist + (i*dir);
							if (focus < 0)
								focus += 1440;
							intval[(focus) % 1440] = 1;
						}
						ct -= it->first.second.first;
					}
					iset.erase(it);
				}
			}
			for (int i = 0; i < 1440; i++)
				if (!intval[i])
					intval[i] = 2;
			ans = 0;
			for (int i = 0; i < 1440; i++) {
				if (intval[i] != intval[(i + 1) % 1440])
					ans++;
			}
		}
		cout << "Case #" << tc << ": " << ans << "\n";
		tc++;
	}
	system("pause");
	return 0;
}
