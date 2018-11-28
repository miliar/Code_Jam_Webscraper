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

#define maxn 1000

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

int n,c,m;
vector <pii> tick;
int nvoz[maxn+10];//st vozenj i-tega cloveka
int nvagon[maxn+10];//st vozenj v i-tem vagonu

bool poskus(int nvlak){
	memset(nvoz,0,sizeof(nvoz));
	memset(nvagon,0,sizeof(nvagon));
	FOR(i,m){
		nvagon[tick[i].fs]++;
		if(nvoz[tick[i].sec]++>=nvlak)return false;
	}
	int sum=0;
	FORR(i,1,n+1){
		sum+=nvagon[i];
		if(sum>i*nvlak)return false;
	}
	return true;
}

bool poskus2(int npromocij, int nvlak){
	int stvago=0;
	int stnavoljo=0;
	int stcurr=0;
	FOR(i,m){
		//printf("(%d,%d)\n",tick[i].fs,tick[i].sec);
		if(tick[i].fs>stvago){
			stnavoljo+=(tick[i].fs-stvago)*nvlak;
			stvago=tick[i].fs;
			stcurr=nvlak;
		}
		//printf("navoljo:%d stvago: %d stcurr: %d npromocij:%d\n",stnavoljo,stvago,stcurr,npromocij);
		if(stcurr>0){
			stcurr--;
			stnavoljo--;
			continue;
		}
		if(stnavoljo<=0 || npromocij<=0)return false;
		stnavoljo--;
		npromocij--;
	}
	return true;
}



void solve(int prim){
	scanf("%d%d%d",&n,&c,&m);
	int res=0;
	tick.clear();
	FOR(i,m){
		int a,b;
		scanf("%d%d",&a,&b);
		tick.pb(mp(a,b));
	}
	sort(tick.begin(),tick.end());
	int l=1,d=1001;
	while(l<d){
		int s=(l+d)/2;
		if(poskus(s))d=s;
		else l=s+1;
	}
	int stvlakov=l;
	l=0,d=1001;
	while(l<d){
		int s=(l+d)/2;
		if(poskus2(s,stvlakov))d=s;
		else l=s+1;
	}
	printf("Case #%d: %d %d\n",prim,stvlakov,l);
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
