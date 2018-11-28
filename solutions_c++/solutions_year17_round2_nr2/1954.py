#include <stdio.h>
#include <stack>
#include <map>
#include <string.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
//#define ld long double
const double sn = 1e-9;
int n;
int r, o, y, g, b, v;
int main() {
	freopen("B-small-attempt4.in","r",stdin);
	freopen("bsmall.out","w",stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		scanf("%d%d%d%d%d%d", &r, &o, &y, &g, &b, &v);
		printf("Case #%d: ", i+1);
		string s = "";
		bool v = false;
		while (true) {
			if (y <= 0 &&  b <= 0 && r <= 0)
				break;
			if (s == "") {
				s += r > y && r > b ? "R" : y > b ? "Y" : "B";
				if (s == "R")
					r--;
				else if (s == "Y")
					y--;
				else
					b--;
			}
			else {
				if (s[s.size() - 1] == 'R') {
					s += y > b ? "Y" : "B";
					if (s[s.size() - 1] == 'Y')
						y--;
					else
						b--;
				}
				else if (s[s.size() - 1] == 'Y') {
					s += r > b ? "R" : "B";
					if (s[s.size() - 1] == 'R')
						r--;
					else
						b--;
				}
				else {
					s += r > y ? "R" : "Y";
					if (s[s.size() - 1] == 'R')
						r--;
					else
						y--;
				}
			}
		}
		int ans = -1;
		int sz = s.size();
		if(s[s.size() - 1] == s[0]){
			for (int i = s.size() - 2; i >= 0; i--) {
				char temp = s[i];
				s[i] = s[sz - 1];
				s[sz - 1] = temp;
				int t = i == 0 ? sz - 1 : i - 1;
				if (s[i] != s[i + 1] && s[i] != s[t] && s[sz - 1] != s[0] && s[sz - 1] != s[sz - 2]) {
					v = true;
					break;
				}
				else {
					char temp = s[i];
					s[i] = s[sz - 1];
					s[sz - 1] = temp;
				}
			}
		}

		if (!v) {
			for (int i = 1; i < sz; i++) {
				char temp = s[i];
				s[i] = s[0];
				s[0] = temp;
				if (s[i] != s[(i + 1) % sz] && s[i] != s[i - 1] && s[0] != s[1] && s[sz-1] != s[0]) {
					v = true;
					break;
				}
				else {
					char temp = s[i];
					s[i] = s[0];
					s[0] = temp;
				}
			}
		}
		if (!v || !(b==0 && y==0 && r==0))
			printf("IMPOSSIBLE\n");
		else
			cout << s << endl;
	}
	return 0; 
}