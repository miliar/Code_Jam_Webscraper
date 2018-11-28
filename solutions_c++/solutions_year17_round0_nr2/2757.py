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


int main() {
	int T, K;
	cin >> T;
	string s;
	for (int i = 1; i <= T; i++) {
		cin >> s;
		LL initSize = s.size();
		for (int j = 0; j < initSize-1; j++) {
			if (s[j] == '1' && s[j+1] == '0') {
				while (j-1 >= 0 && s[j-1] == '1') j--;
				if (j == 0) { // && s[j] == '1') {
					s = "";
					for (j = 1; j < initSize; j++) {
						s += '9';
					}
					break;
				} else {
					while (j >= 0) {
						if (j-1 >= 0 && s[j-1] == s[j]) j--;
						else break;
					}
					s[j]--;
					for (j = j+1; j < s.size(); j++) {
						s[j] = '9';
					}
				}
			} else if (s[j] > s[j+1]) {
				while (j >=0) {
					if (j-1 >= 0 && s[j-1] == s[j]) j--;
					else break;
				}
				s[j]--;
				for (j = j+1; j < s.size(); j++) {
					s[j] = '9';
				}
			}
		}
		cout << "Case #" << i << ": " << s << endl;
	}
	return 0;
}
