/*
 * OversizedPancakeFlipper_GCJ.cpp
 *
 *  Created on: Apr 7, 2017
 *      Author: iNviNciBLe
 */

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <fstream>

using namespace std;

#include <bits/stdc++.h>
#define rep(i,n) for(size_t i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int, int> mii;
typedef map<st, int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
#define mx 0

int main() {
	read("A-large.in");
	rite("oA-Large");
	int tc,count = 0;
	string s_res;
	st s;
	int k;
	cin >> tc;
	while (tc--) {
		s = "";
		count++;
		int res = 0;
		cin >> s >> k;
		for (size_t i = 0; i <= s.size() - k; i++) {
			if (s[i] == '-') {
				res++;
				size_t j = i;
				while (j < i + k) {
					if (s[j] == '-')
						s[j++] = '+';
					else
						s[j++] = '-';
				}
			}
		}
		s_res = "Case #" + to_string(count) + ": " + to_string(res);
		for(auto i : s){
			if(i == '-'){
				s_res = "Case #" + to_string(count) + ": " + "IMPOSSIBLE";
				break;
			}
		}
		cout << s_res << endl;
	}
}

