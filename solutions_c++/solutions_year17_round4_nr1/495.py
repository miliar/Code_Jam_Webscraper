#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 100000

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

int n,p;

void solve2(int prim){
	int stl=0;
	FOR(i,n){
		int c;
		scanf("%d",&c);
		if(c&1)stl++;
	}
	printf("Case #%d: %d\n",prim,n-stl/2);
}

void solve3(int prim){
	int st1=0,st2=0;
	FOR(i,n){
		int c;
		scanf("%d",&c);
		if(c%3==1)st1++;
		if(c%3==2)st2++;
	}
	int rez=n-st1-st2;
	rez+=min(st1,st2);
	int diff=max(st1,st2)-min(st1,st2);
	rez+=(diff+2)/3;
	printf("Case #%d: %d\n",prim,rez);
}

void solve4(int prim){
	int st1=0,st2=0,st3=0;
	FOR(i,n){
		int c;
		scanf("%d",&c);
		if(c%4==1)st1++;
		if(c%4==2)st2++;
		if(c%4==3)st3++;
	}
	int rez=n-st1-st2-st3;
	rez+=st2/2;
	rez+=min(st1,st3);
	int diff=max(st1,st3)-min(st1,st3);
	if(st2&1){
		rez+=1;
		diff-=2;
	}
	if(diff>0){
		rez+=(diff+3)/4;
	}
	printf("Case #%d: %d\n",prim,rez);
}

void solve(int prim){
	scanf("%d%d",&n,&p);
	if(p==2)solve2(prim);
	if(p==3)solve3(prim);
	if(p==4)solve4(prim);
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
