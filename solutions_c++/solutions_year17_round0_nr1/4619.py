#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vii;

#define Pq priority_queue
#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d%d", &x, &y)
#define FOR(i,S,E) for(int i=S; i<E; i++)
#define pb push_back
#define fst first
#define snd second

int main () {
	int T; ri(T);
	FOR(t,1,T+1) {
		string str; int k;
		cin >> str >> k;
		int cnt=0;
		FOR(j,0,str.size()) {
			if (str[j] == '-' && j+k <= str.size()) {
				FOR(i,j,j+k) {
					if (str[i] == '+') str[i] = '-';
					else str[i] = '+';
				}
				cnt++;
			}
		}
		bool bad=0;
		FOR(i,0,str.size()) {
			if (str[i] == '-') {
				printf("Case #%d: IMPOSSIBLE\n", t);
				bad=1;
				break;
			}
		}
		if (!bad) {
			printf("Case #%d: %d\n", t, cnt);
		}
	}
}