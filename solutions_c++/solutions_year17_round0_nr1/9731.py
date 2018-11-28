#include <iostream>
#include <math.h>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>
#include <string.h>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <limits>
#include <list>
#include <functional>
#include <bitset>
#include <numeric>
#include <iomanip>
#include <ctime>
#include <ctype.h>
#include <stdio.h>

using namespace std;
typedef long long ll;
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define sz size()

int t, k;
string s;
queue< string > q;
map< string, bool > used;
map< string, int > d;

int bfs(string f, int k) {
	q.push(f);
	used[f] = true;
	while(!q.empty()) {
		string cur = q.front();
		q.pop();
		int l = 0, r = k;
		for (int j = 0; j < f.sz - k + 1; j++) {
			string ns = cur;
			for (int i = l; i < r; i++) {
				if (ns[i] == '-') {
					ns[i] = '+';
				}
				else {
					ns[i] = '-';
				}
			}
			l++;
			r++;
			if (!used[ns]) {
				used[ns] = true;
				q.push(ns);
				d[ns] = d[cur] + 1;
			}
		}
	}
	string fans = "";
	for (int i = 0; i < f.sz; i++) {
		fans += '+';
	}

	if (fans == f) {
		return 0;
	}
	else if (d[fans] == 0) {
		return -1;
	}
	else {
		return d[fans];
	}
}


int main()
{	
	ios_base::sync_with_stdio(0);
    	cin.tie(NULL); 
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> s >> k;
		int ans = bfs(s, k);
		if (ans == -1) {
			cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl; 
		}
		else {
			cout << "Case #" << i + 1 << ": " << ans << endl;
		}
		used.clear();
		d.clear();
	}	


	
	return 0;
	//cerr << (double)clock() * 1.0 / CLOCKS_PER_SEC << endl;	                      	
}