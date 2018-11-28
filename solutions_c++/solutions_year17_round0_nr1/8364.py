/*
 *   Author: Sourav Chakraborty 
 *   <mail.souravchk@gmail.com>
 */

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>

#define LL long long
#define INF 1e18
#define pb push_back
#define mp make_pair

#define max(a,b) (a) > (b) ? (a): (b)
#define min(a,b) (a) < (b) ? (a): (b)

using namespace std;

string TARGET = "";

void setTarget(int n) {
    TARGET = "";
    for (int i = 0; i < n; i++) {
	TARGET += '+';
    }
}

string flip(string s, int b, int e) {
    string temp = s;
    for (int i = 0; i <= temp.size(); i++) {	
	if (i < b || i > e)
	    continue;
	if (s[i] == '+') {
	    temp[i] = '-';
	} else {
	    temp[i] = '+';
	}
    }
    return temp;
}

int BFS(string s, int k) {
    queue<string> q;
    q.push(s);
    
    map <string, int> vis, steps;

    vis[s] = 1;
    steps[s] = 0;

    while(!q.empty()) {
	string f = q.front();
	if (f == TARGET) 
	    return steps[f];

	int SZ = f.size();
	for (int i = 0; i + k - 1 < SZ; i++) {
	    string f1 = flip(f, i, i + k - 1);
	    if (!vis[f1]) {
		vis[f1] = 1;
		steps[f1] = steps[f] + 1;
		q.push(f1);
	    }
	}
	q.pop();
    }
    return -1;
}

int main() {
    int t, count = 1; cin >> t;
    while(t--) {
	string s; int k; 
	cin >> s >> k;
	setTarget((int)(s.size()));
	int res = BFS(s,k);
	if (res == -1) {
	    printf("Case #%d: IMPOSSIBLE\n", count++);
	} else {
	    printf("Case #%d: %d\n", count++, res);
	}
    }
    return 0;
}
