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

int n, R, O, Y, G, B, V;

void sol()
{
	if (O==B && O+B==n)
	{
		FOR(a,1,O) cout << "OB";
		return;
	}
	if (G==R && G+R==n)
	{
		FOR(a,1,G) cout << "GR";
		return;
	}
	if (V==Y && V+Y==n)
	{
		FOR(a,1,Y) cout << "VY";
		return;
	}

	if ( (O>0 && B<=O) || (G>0 && R<=G) || (V>0 && Y<=V) )
	{
		cout << "IMPOSSIBLE";
		return;
	}
	B-=O; R-=G; Y-=V;

	char **** dp;
	dp = new char *** [ R+1 ];
	FOR(a,0,R) dp[a] = new char ** [ Y+1 ];
	FOR(a,0,R) FOR(b,0,Y) dp[a][b] = new char * [ B+1 ];
	FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) dp[a][b][c] = new char [ 3 ];
	FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) FOR(d,0,2) dp[a][b][c][d] = 0;
	char **** pre;
	pre = new char *** [ R+1 ];
	FOR(a,0,R) pre[a] = new char ** [ Y+1 ];
	FOR(a,0,R) FOR(b,0,Y) pre[a][b] = new char * [ B+1 ];
	FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) pre[a][b][c] = new char [ 3 ];
	FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) FOR(d,0,2) pre[a][b][c][d] = 0;

	int first = -1;
	if (R>0) { dp[1][0][0][0] = true; first = 0; }
	else if (Y>0) { dp[0][1][0][1] = true; first = 1; }
	else if (B>0) { dp[0][0][1][2] = true; first = 2; }

	FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) FOR(d,0,2)
		if (dp[a][b][c][d])
		{
			if (a<R && d!=0) { dp[a+1][b][c][0] = true; pre[a+1][b][c][0] = d; }
			if (b<Y && d!=1) { dp[a][b+1][c][1] = true; pre[a][b+1][c][1] = d; }
			if (c<B && d!=2) { dp[a][b][c+1][2] = true; pre[a][b][c+1][2] = d; }
		}

	int last = -1;
	FOR(a,0,2) if (a!=first)
		if (dp[R][Y][B][a])
			last = a;

	if (last==-1)
	{
		cout << "IMPOSSIBLE";

		FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) delete [] dp[a][b][c];
		FOR(a,0,R) FOR(b,0,Y) delete [] dp[a][b];
		FOR(a,0,R) delete [] dp[a];
		delete [] dp;
		FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) delete [] pre[a][b][c];
		FOR(a,0,R) FOR(b,0,Y) delete [] pre[a][b];
		FOR(a,0,R) delete [] pre[a];
		delete [] pre;

		return;
	}

	string ans;
	int x=R, y=Y, z=B, w=last;
	while(x>0 || y>0 || z>0)
	{
		ans.push_back( "RYB"[ w ] );
		int ww = pre[x][y][z][w];
		if (w==0) x--;
		else if (w==1) y--;
		else z--;
		w = ww;
	}
	//cout << ans;
	FA(a,ans)
	{
		cout << ans[a];
		if (ans[a]=='R')
		{
			FOR(b,1,G) cout << "GR";
			G = 0;
		}
		if (ans[a]=='Y')
		{
			FOR(b,1,V) cout << "VY";
			V = 0;
		}
		if (ans[a]=='B')
		{
			FOR(b,1,O) cout << "OB";
			O = 0;
		}
	}

	FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) delete [] dp[a][b][c];
	FOR(a,0,R) FOR(b,0,Y) delete [] dp[a][b];
	FOR(a,0,R) delete [] dp[a];
	delete [] dp;
	FOR(a,0,R) FOR(b,0,Y) FOR(c,0,B) delete [] pre[a][b][c];
	FOR(a,0,R) FOR(b,0,Y) delete [] pre[a][b];
	FOR(a,0,R) delete [] pre[a];
	delete [] pre;
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

		cin >> n >> R >> O >> Y >> G >> B >> V;

		cout << "Case #" << z << ": ";
		sol();
		cout << "\n";
	}
	cerr << "time = " << clock() << "\n";
	return 0;
}
