
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>

#define PI 3.14159265358979323846 
#define PO << " " <<
#define P " "
#define ABS(x) (((x) > 0) ? (x) : (-(x)))
#define RND(x) ((int)( (x) + 0.5 ))
#define MAX(x, y) (( (x) > (y) ) ? (x) : (y))
#define MIN(x, y) (( (x) < (y) ) ? (x) : (y))
#define forn(i, ending) for (int i = 0; i < (ending); i++)
#define it(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define oo ((int)1e9)

using namespace std;

typedef long long int lint;
typedef unsigned long long int ulint;
typedef std::pair <int, int> pint;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <vvi> vvvi;

lint f(lint n, lint k) {
	if (k <= 1)
		return n;
	n--;
	k--;
	if (n % 2)
		if (k % 2)
			return f(n / 2 + 1, k / 2 + 1);
		else
			return f(n / 2, k / 2);
	else
		return f(n / 2, k / 2 + max((lint)0, k % 2));
		
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int casen = 0;
	int t; cin >> t; while (t--) {
		casen++;
		lint n, k; cin >> n >> k;
		lint t = f(n, k);
		t--;
		lint mx = t / 2 + max(t % 2, (lint)0);
		lint mn = t / 2;
		cout << "Case #" << casen << ": ";
		cout << mx << ' ' << mn;
		cout << '\n';
	}
}