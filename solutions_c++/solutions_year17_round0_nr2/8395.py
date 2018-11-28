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

#define LL long long
#define INF 1e18
#define pb push_back
#define mp make_pair

#define max(a,b) (a) > (b) ? (a): (b)
#define min(a,b) (a) < (b) ? (a): (b)

using namespace std;

string solve(string n) {
	int SZ = n.size();
	int idx = SZ;
	for (int i = 0; i < SZ - 1; i++) {
	    if (n[i] > n[i + 1]) {
			idx = i;
			break;
		}
	}
	string res = "";
	for (int i = 0; i < idx; i++) {
	    res += n[i];
	}
	if (idx < SZ) {
	    res += (char)((int)(n[idx]) - 1);
	    for (int i = res.size(); i < SZ; i++) {
			res += '9';
	    }
	}
	while (res[0] == '0') {
	    res = res.substr(1);
	}
	return res;
}

int main() {
    int t, count = 1; cin >> t;
    while (t--) {
		string n; cin >> n;
		string temp = n, res = "";
		bool carry_on = true;
		while (carry_on) {
			res = solve(temp);
			int ok = 1;
			for (int i = 0; i < res.size() - 1; i++) {
				if (res[i] > res[i + 1]) {
					ok = 0;
				}
			}
			if(ok) carry_on = false;
			temp = res;
		}
		
		cout << "Case #" << count++ << ": ";
		cout << res << "\n";
    }
}
