#include <algorithm>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <memory.h>
#include <stdio.h>
#include <complex>
#include <cstdlib>
#include <sstream>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <vector>
#include <string>
#include <bitset>
#include <cstdio>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
#include<deque>
typedef long long ll;
using namespace std;
const int N = 1000 + 10;
int col[6];
int n;
char color[] = { 'R','B','Y','G','O','V' };
int main() {
#ifndef ONLINE_JUDGE
//	freopen("myfile.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas) {
		printf("Case #%d: ", cas);
		scanf("%d", &n);
		for (int i = 0; i < 6; ++i)
			scanf("%d", col + i);
		swap(col[1], col[4]);
		bool noSol = false;
		for (int i = 3; i < 6; i++)
			if (col[i] > col[i - 3])
				noSol = true;
		
		
		int sAt = -1;
		for (int i = 3; i < 6; i++)
			if (col[i]!=0 && col[i] == col[i - 3]) {
				if (col[i] + col[i - 3] != n)
					noSol = true;
				else
					sAt = i;
			}
		if (noSol) {
			puts("IMPOSSIBLE");
			continue;
		}
		if (sAt != -1) {
			string ans = "";
			for (int i = 0; i < col[sAt]; ++i) {
				ans += color[sAt];
				ans += color[sAt - 3];
			}
			printf("%s\n", ans.c_str());
			continue;
		}
		for (int i = 3; i < 6; i++)
			col[i - 3] -= col[i];
		vector<pair<int, int> > v;
		for (int i = 0; i < 3; ++i)
			v.push_back(make_pair(col[i], i));
		sort(v.begin(), v.end());
		if (v[2].first > v[0].first + v[1].first) {
			puts("IMPOSSIBLE");
			continue;
		}
		
		string ans ;
		ans.resize(v[0].first + v[1].first + v[2].first,'X');
		int at;
		for (int i = 0; i < ans.size(); i += 2) {
			ans[i] = color[v[2].second];
			--v[2].first;
			if (!v[2].first) {
				at = i + 1;
				break;
			}
		}
		
		for (int i = 1; i <= at; i += 2) {
			if (v[0].first > v[1].first) {
				ans[i] = color[v[0].second];
				--v[0].first;
			}
			else {
				ans[i] = color[v[1].second];
				--v[1].first;
			}
		}
		for (int i = at + 1; i < ans.size(); ++i) {
			if (v[0].first > v[1].first) {
				ans[i] = color[v[0].second];
				--v[0].first;
			}
			else {
				ans[i] = color[v[1].second];
				--v[1].first;
			}
		}
		string res = "";
		vector<string> add(3,"");
		map<char, int> mp;
		mp['R'] = 0;
		mp['B'] = 1;
		mp['Y'] = 2;
		for (int i = 3; i < 6; ++i) {
			if (col[i]) {
				string tmp = "";
				tmp += color[i - 3];
				while (col[i]--) {
					tmp += color[i];
					tmp += color[i - 3];
				}
				add[i-3] = tmp;
			}
		}
		for (int i = 0; i < ans.size(); ++i) {
			if (add[mp[ans[i]]] != "") {
				res += add[mp[ans[i]]];
				add[mp[ans[i]]] = "";
			}
			else
				res += ans[i];
		}
		printf("%s\n", res.c_str());
	}

	return 0;
}

