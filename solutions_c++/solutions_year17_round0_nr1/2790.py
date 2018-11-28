#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <stdlib.h>
#include <string.h>
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <ctype.h>
#include <math.h>
#define FOR(x,y,z) for(int x = (y); x < (z); x++)
#define FORD(x,y,z) for(int x = (y); x >= z; x--)
#define REP(r,n) for(int r = 0; r < (n); r++)
#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define MAXUS 100001
#define MAXUS2 9000005
#define PI 3.1415926
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); i++)
#define ALL(u) (u).begin(),(u).end()
#define epsilon 0.000001
using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PR;
LL global_top_number = 0;


void flip(string &s, int from, int size) {
	for (int i = from; i < from + size; i++) {
		s[i] = s[i] == '+' ? '-' : '+';
	}
}

int main() {
	int T, K;
	cin >> T;
	string s;
	for (int t = 1; t <= T; t++) {
		cin >> s;
		cin >> K;
		int flipCounter = 0; 
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-' && i + K <= s.size()) {
					flip(s, i, K);
					flipCounter++;
			}
		}
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '-') {
				flipCounter = -1;
				break;
			}
		}
		if (flipCounter >= 0) {
			cout << "Case #" << t << ": " << flipCounter << endl;
		} else {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;	
		}
	}
	return 0;
}
