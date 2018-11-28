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

LL n, kk;

void sol()
{
	LL k = kk;
	map< LL, LL > Map;
	Map[n]=1;

	while (k > 0)
	{
		map< LL, LL >::iterator it = Map.end();
		it--;
		k--;
		LL L, R;
		L = R = (it->first-1)/2;
		if ((it->first-1)&1) R++;
		if (it->second==1) Map.erase(it);
		else Map[it->first]--;
		if (k==0)
		{
			cout << R << " " << L;
			return;
		}
		if (L>0) Map[L]++;
		if (R>0) Map[R]++;
	}
}

void sol2()
{
	LL k = kk;
	map< LL, LL > Map;
	Map[n]=1;

	while (k > 0)
	{
		map< LL, LL >::iterator it = Map.end();
		it--;
		LL delta = it->second;
		if (k<delta) delta=k;
		k-=delta;
		LL L, R;
		L = R = (it->first-1)/2;
		if ((it->first-1)&1) R++;

		if (it->second==delta) Map.erase(it);
		else Map[it->first]-=delta;

		if (k==0)
		{
			cout << R << " " << L;
			return;
		}
		if (L>0) Map[L]+=delta;
		if (R>0) Map[R]+=delta;
	}
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
		cin >> n >> kk;
		cout << "Case #" << z << ": ";
		//sol();
		//cout << "  ";
		sol2();
		cout << "\n";
	}

	return 0;
}
