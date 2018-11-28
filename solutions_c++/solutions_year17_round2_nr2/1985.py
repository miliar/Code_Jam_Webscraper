#include <iostream>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <set>
using namespace std;
int map[128];
char arr[7] = "RYBGVO";
int possibleCnt[6] = { 3, 3, 3, 1, 1, 1 };
int nextIdx[6][3] = {
				{3, 1, 2},
				{4, 2, 0},
				{5, 0, 1},
				{0, -1, -1},
				{1, -1, -1},
				{2, -1, -1}
};
int impossibleCnt[6] = { 3, 3, 3, 5, 5, 5 };
int notnextIdx[6][5] = {
	{ 0, 4, 5, -1, -1 },
	{ 1, 3, 5, -1, -1 },
	{ 2, 3, 4, -1, -1 },
	{ 3, 4, 5, 1, 2 },
	{ 3, 4, 5, 0, 2 },
	{ 3, 4, 5, 0, 1 }
};
set<int> majorSet;
set<int> minorSet;
int startMajor[3] = { 3, 4, 5 };
int startMinor[3] = { 0, 1, 2 };
// input
int N;
int cnt[6];
int effect[6];

string Solve()
{
	majorSet.insert(3);
	majorSet.insert(4);
	majorSet.insert(5);
	minorSet.insert(0);
	minorSet.insert(1);
	minorSet.insert(2);
	map['R'] = 0;
	map['Y'] = 1;
	map['B'] = 2;
	map['G'] = 3;
	map['V'] = 4;
	map['O'] = 5;
	for (int i = 0; i < 6; i++) {
		effect[i] = 0;
	}
	// 시작할것 찾기
	// 시작할거 정하면 effect에 추가하기

	set<char> oo;
	stack<string> a;
	//거꾸로 넣기
	//if (cnt[0] > cnt[1]) {
	//	if (cnt[1] > cnt[2]) {
	//		if (cnt[2] > 0) {
	//			a.push(string(1, arr[2]));
	//		}
	//		if (cnt[1] > 0) {
	//			a.push(string(1, arr[1]));
	//		}
	//		if (cnt[0] > 0) {
	//			a.push(string(1, arr[0]));
	//		}
	//	}
	//	else {
	//		if (cnt[0] > cnt[2]) {
	//			if (cnt[1] > 0) {
	//				a.push(string(1, arr[1]));
	//			}
	//			if (cnt[2] > 0) {
	//				a.push(string(1, arr[2]));
	//			}
	//			if (cnt[0] > 0) {
	//				a.push(string(1, arr[0]));
	//			}
	//		}
	//		else {
	//			if (cnt[1] > 0) {
	//				a.push(string(1, arr[1]));
	//			}
	//			if (cnt[0] > 0) {
	//				a.push(string(1, arr[0]));
	//			}
	//			if (cnt[2] > 0) {
	//				a.push(string(1, arr[2]));
	//			}
	//		}
	//	}
	//}
	//else {

	//}

	// 채우기 ( 대충)
	int cmax = 0;
	int ci = -1;
	for (int i = 3; i < 6; i++) {
		if (cnt[i] > cmax) {
			cmax = cnt[i];
			ci = i;
		}
	}
	if (ci >= 0) {
		a.push(string(1, arr[ci]));
		//oo.insert(arr[ci]);
		//for (int i = 3; i < 6; i++) {
		//	if (cnt[i] > 0 && oo.find(arr[i]) == oo.end()) {
		//		a.push(string(1, arr[i]));
		//		oo.insert(arr[i]);
		//	}
		//}
	}

	if (a.empty()) {
		cmax = 0;
		ci = -1;
		for (int i = 0; i < 3; i++) {
			if (cnt[i] > cmax) {
				cmax = cnt[i];
				ci = i;
			}
		}
		if (ci >= 0) {
			a.push(string(1, arr[ci]));
			//oo.insert(arr[ci]);
			//for (int i = 3; i < 6; i++) {
			//	if (cnt[i] > 0 && oo.find(arr[i]) == oo.end()) {
			//		a.push(string(1, arr[i]));
			//		oo.insert(arr[i]);
			//	}
			//}
		}
	}

	while (a.size() > 0) {
		string sCur = a.top();
		a.pop();

		int nCurCnt[6];
		for(int i = 0; i < 6; i++) {
			nCurCnt[i] = cnt[i];
			effect[i] = 0;
		}
		for (int i = 0; i < sCur.length(); i++) {
			nCurCnt[map[sCur[i]]]--;
		}
		int n1st = map[sCur[0]];
		for (int i = 0; i < impossibleCnt[n1st]; i++) {
			int cur = notnextIdx[n1st][i];
			if (nCurCnt[cur] == 0) {
				continue;
			}
			effect[cur] = 1;
		}

		// go next
		char cLast = sCur[sCur.length() - 1];
		int nLast = map[cLast];
		int cmax = 0;
		int ci = -1;
		for (int i = 0; i < possibleCnt[nLast]; i++) {
			int cur = nextIdx[nLast][i];
			if (nCurCnt[cur] == 0) {
				continue;
			}
			if (majorSet.find(cur) != majorSet.end()) {
				continue;
			}
			if (nCurCnt[cur] + effect[cur] > cmax) {
				cmax = nCurCnt[cur] + effect[cur];
				ci = cur;
			}
		}
		if (ci < 0) {
			for (int i = 0; i < possibleCnt[nLast]; i++) {
				int cur = nextIdx[nLast][i];
				if (nCurCnt[cur] == 0) {
					continue;
				}
				if (nCurCnt[cur] + effect[cur] > cmax) {
					cmax = nCurCnt[cur] + effect[cur];
					ci = cur;
				}
			}
			if (ci < 0) {
				continue;
			}
		}

		string newStr(sCur + arr[ci]);
		if (newStr.length() == N) {
			// 검증
			for (int k = 0; k < possibleCnt[ci]; k++) {
				if (nextIdx[ci][k] != n1st) {
					continue;
				}
				return newStr;
			}
			continue;
		}
		a.push(newStr);
	}


	return "IMPOSSIBLE";
}


int main(void) {
	//string sFileBase("B-small-attempt1");
	//freopen((sFileBase + ".in").c_str(), "r", stdin);
	//freopen((sFileBase + ".txt").c_str(), "w", stdout);

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N >> cnt[0] >> cnt[5] >> cnt[1] >> cnt[3] >> cnt[2] >> cnt[4];
		printf("Case #%d: %s\n", tc, Solve().c_str());
	}
}