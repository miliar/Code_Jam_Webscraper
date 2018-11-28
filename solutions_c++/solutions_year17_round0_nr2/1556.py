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

LL n;

bool tidy( LL x )
{
	char S[24];
	sprintf( S, "%lld", x );
	int sz = strlen( S );
	FOR(a,0,sz-2) if (S[a]>S[a+1]) return false;
	return true;
}

void sol()
{
	if (tidy(n))
	{
		cout << n;
		return;
	}

	for ( LL a=n; a>=n-100000; a-- )
		if (tidy(a))
		{
			cout << a;
			return;
		}
}

void sol2()
{
	if (tidy(n))
	{
		cout << n;
		return;
	}

	int digs = 0;

	while(n>0)
	{
		n/=10;
		digs++;
		int last = n%10;
		int pre = (n/10)%10;
		if (tidy(n) && pre < last)
		{
			if (n>=10) cout << n/10;
			if (n>=10 || last>1) cout << last-1;
			FOR(a,1,digs) cout << "9";
			return;
		}
	}

	ass( false );
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	FOR(z,1,T)
	{
		cin >> n;
		cout << "Case #" << z << ": ";
		//sol();
		//cout << " ";
		sol2();
		cout << "\n";
	}

	return 0;
}
