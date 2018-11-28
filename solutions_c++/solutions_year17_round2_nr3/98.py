#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000

void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int n, q;
int E[110], S[110];
LL D[110][110];
PAR que[110];

double D2[110][110];

void sol()
{
	FOR(a,1,n) FOR(b,1,n) FOR(c,1,n)
		D[b][c] = min( D[b][c], D[b][a] + D[a][c] );

	FOR(a,1,n) FOR(b,1,n)
		if (D[a][b] <= E[a])
			D2[a][b] = (double)D[a][b] / S[a];
		else D2[a][b] = (double)o_O * o_O;

	FOR(a,1,n) FOR(b,1,n) FOR(c,1,n)
		D2[b][c] = min( D2[b][c], D2[b][a] + D2[a][c] );

	FOR(a,1,q)
		WR(" %.10lf", D2[que[a].first][que[a].second] );
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	FOR(z,1,T)
	{
		cerr << z << "\n";

		cin >> n >> q;
		FOR(a,1,n) cin >> E[a] >> S[a];
		FOR(a,1,n) FOR(b,1,n)
		{
			cin >> D[a][b];
			if (D[a][b]==-1) D[a][b] = (LL)o_O * o_O;
		}
		FOR(a,1,q) cin >> que[a].first >> que[a].second;

		cout << "Case #" << z << ":";
		sol();
		cout << "\n";
	}
	return 0;
}
