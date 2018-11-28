#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#define fi first
#define se second
#define rep(i,a,b) for (int i=(a);i<(b);i++)
#define per(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,a,b) for (int i=(a);i<=(b);i++)
#define PER(i,a,b) for (int i=(b);i>=(a);i--)
using namespace std;
typedef long long LL;

const int INF = 0x3f3f3f3f;

const int MAXN = 1000005; // 1e6;

int T;
int N,R,O,Y,G,B,V;
void go(int ty)
{
	if (ty==1) {
		printf("R"); 
		while (G>0) 
		{
			printf("G");G--;
			if (R>0) R--,printf("R");
		}
	}
	if (ty==2) 
	{
		printf("Y"); 
		while (V>0) 
		{
			printf("V");V--;
			if (Y>0)Y--,printf("Y");
		}
	}
	if (ty ==3)
	{
		printf("B"); 
		while (O>0) 
		{
			O--; printf("O");
			if (B>0)B--,printf("B");
		}
	}
}

int solve(int cas)
{
	cin>>N>>R>>O>>Y>>G>>B>>V;
	if (R - G < 0 || Y - V < 0 || B - O < 0) return 0*printf("Case #%d: IMPOSSIBLE\n",cas );
	if (R == G && R > 0 && O + Y + B + V != 0) return 0*printf("Case #%d: IMPOSSIBLE\n",cas );
	if (Y == V && Y > 0 &&O + R + B + G != 0) return 0*printf("Case #%d: IMPOSSIBLE\n",cas );
	if (B == O && B > 0 && Y + R + V + G != 0) return 0*printf("Case #%d: IMPOSSIBLE\n",cas );
	if (R-G > B-O+Y-V || B-O > R-G+Y-V || Y-V > B-O+R-G)  return 0*printf("Case #%d: IMPOSSIBLE\n",cas );
	printf("Case #%d: ",cas );
	if (R==G && R>0) 
	{
		rep(i,0,R)
		{
			printf("RG");
		}
		printf("\n");
		return 0;
	}
	else if (Y==V && Y > 0)
	{
		rep(i,0,Y)
		printf("YV");
		printf("\n");
		return 0 ;
	}
	else if (B==O && B > 0)
	{
		rep(i,0,B)
		printf("BO");
		printf("\n");
		return 0;
	}
	if (R > 0 && R-G >= B-O && R-G >= Y-V)
	{
		rep(i,0,R)
		{
			go(1);
			if (Y-V>0) Y--,go(2);
			if (O > 0 && i+B-O == R) B--,go(3);
			else if (O == 0 && i+B == R && B>0) B--,go(3);
		}
	}
	else if (B > 0 && B-O >= R-G && B-O >= Y-V)
	{

		rep(i,0,B)
		{
			go(3);
			if (R-G>0) R--,go(1);
			if (V>0 && i+Y-V==B) Y--,go(2);
			else if (V == 0 && i+Y == B && Y>0) Y--,go(2);
		}
	}
	else if (Y > 0 && Y-V >= R-G && Y-V >= B-O)
	{
		rep(i,0,Y)
		{
			go(2);
			if (R-G>0) R--,go(1);
			if (O > 0 && i+B-O == R) B--,go(3);
			else if (O == 0 && i+B == Y && B>0) B--,go(3);
		}
	}
	return 0*printf("\n");
}
int main()
{
	freopen("B-small-attempt0.in.txt","r",stdin);
	freopen("small.out","w",stdout);
	cin>>T;
	rep(cas,1,T+1)
	{
		solve(cas);

	}


}

