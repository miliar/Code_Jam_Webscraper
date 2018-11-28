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

#define uint8 unsigned char

int n, p, q[110];
map< vector< uint8 >, int > Map;

int to_int( vector< uint8 > & v )
{
	int re = 0;
	RFA(a,v) re = re*101+v[a];
	return re;
}

int dfs( vector< uint8 > & v )
{
	if (Map.find( v ) != Map.end()) return Map[v];

	int re = 0;
	bool z = (v[p]==0);
	for (int a=0; a<p; a++)
		if (v[a]>0)
		{
			v[a]--;
			v[p] = (v[p]-a+p)%p;
			re = max( re, dfs( v ) + (z ? 1 : 0) );
			v[p] = (v[p]+a)%p;
			v[a]++;
		}

	Map[v] = re;
	return re;
}

void sol()
{
	vector< uint8 > cnt;
	cnt.resize( p, 0 );
	FOR(a,1,n) cnt[q[a]%p]++;
	cnt.push_back( 0 );

	Map.clear();
	cout << dfs( cnt );
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
		cin >> n >> p;
		FOR(a,1,n) cin >> q[a];
		cout << "Case #" << z << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}
