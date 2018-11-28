
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
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

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int casen = 0;
	int t; cin >> t; while (t--) {
		casen++;
		string s;
		cin >> s;
		int n = s.length();
		bool exists;
		do {
			exists = false;
			forn(i, n - 1)
				if (s[i] > s[i + 1]) {
					exists = true;
					s[i]--;
					for (int j = i + 1; j < n; j++)
						s[j] = '9';
				}
		} while (exists);
		if (s[0] == '0')
			s = s.substr(1);
		cout << "Case #" << casen << ": ";
		cout << s;
		cout << '\n';
	}
}