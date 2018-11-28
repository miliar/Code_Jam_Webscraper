#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

#define FOR(i,a,b) for(int i=int(a);i<=int(b);++i)
#define FORD(i,a,b) for(int i=int(a);i>=int(b);--i)
#define REP(i,n) FOR(i,0,(n)-1)

char cake[30][30];
int r, c;

int main() {
	int tN;
	scanf("%d", &tN);
	FOR(cN, 1, tN) {
		scanf("%d%d", &r, &c);
		REP(i, r) scanf("%s", cake[i]);
		REP(x, r)
		FOR(y, 1, c-1) if (cake[x][y] == '?' && cake[x][y-1] != '?') cake[x][y] = cake[x][y-1];
		REP(x, r)
		FORD(y, c-2, 0) if (cake[x][y] == '?' && cake[x][y+1] != '?') cake[x][y] = cake[x][y+1];
		REP(y, c)
		FOR(x, 1, r-1) if (cake[x][y] == '?' && cake[x-1][y] != '?') cake[x][y] = cake[x-1][y];
		REP(y, c)
		FORD(x, r-2, 0) if (cake[x][y] == '?' && cake[x+1][y] != '?') cake[x][y] = cake[x+1][y];
		printf("Case #%d:\n", cN);
		REP(i, r) printf("%s\n", cake[i]);
	}
}
