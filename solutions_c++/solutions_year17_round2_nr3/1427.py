#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4146)

//#pragma comment(linker, "/STACK:268435456")
#ifdef _MSC_VER
#	include <intrin.h>
#	define __builtin_popcount(n) __popcnt(n)
#endif

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <list>
#include <functional>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <bitset>
#define reg register
#define ll long long
#define ld long double
#define uc unsigned char
#define ui unsigned int
#define ull unsigned ll
#define pll pair<ll, ll>
#define pii pair<int, int>
#define piii pair<pii, int>
#define pis pair<int, string>
#define pss pair<string, string>
#define pdd pair<double, double>
#define pldd pair<ld, ld>
#define vi vector<int>
#define vll vector<ll>
#define vpii vector<pii>
#define vpll vector<pll>
#define mii map<int, int>
#define mll map<ll, ll>
#define pb push_back
#define PI acos(-1.0L)
#define inf 0x3f3f3f3f
#define inf2 0x3f3f3f3f3f3f3f3f
#define P 1000000009
// [Note1: Use long double if necess]  // %Lf
// [Note2: buliltin]
// __builtin_ffs, __builtin_clz, __builtin_ctz, __builtin_clrsb, __builtin_popcount, __builtin_parity

using namespace std;

inline int gi(){
	char ch=getchar();
	while(!((ch>='0'&&ch<='9')||ch=='-')) ch=getchar();
	int x=0,p=1;
	if(ch=='-') p=-1, ch=getchar();
	while(ch>='0'&&ch<='9') x=x*10+ch-'0', ch=getchar();
	return x*p;
}

inline int inv(int x){
	if(x==1) return 1;
	return ((ll)-P/x*inv(P%x)%P+P)%P;
}

inline int cb32(reg ui x){
	x=x-((x>>1)&0x55555555);
	x=(x&0x33333333)+((x>>2)&0x33333333);
	return ((x+(x>>4)&0xF0F0F0F)*0x1010101)>>24;
}

inline int rb8(reg uc x){
	return ((x*0x80200802ULL)&0x0884422110ULL)*0x0101010101ULL>>32;
	//return (x*0x0202020202ULL&0x010884422010ULL)%1023;
}

inline int rb32(reg ui x){
	x=((x>>1)&0x55555555)|((x&0x55555555)<<1);
	x=((x>>2)&0x33333333)|((x&0x33333333)<<2);
	x=((x>>4)&0x0F0F0F0F)|((x&0x0F0F0F0F)<<4);
	x=((x>>8)&0x00FF00FF)|((x&0x00FF00FF)<<8);
	return (x>>16)|(x<<16);
}

inline int nb(reg ui x){  // lexico next permute
	//ui t=x|(x-1);
	//return (t+1)|(((~t&-~t)-1)>>(__builtin_ctz(x)+1));
	reg ui t=(x|(x-1))+1;
	return t|((((t&-t)/(x&-x))>>1)-1);
}

ll gcd(ll x, ll y){
	if(x==0) return y;
	return gcd(y%x, x);
}

struct Node{
	int k,s;
	bool operator<(const Node &rhs) const { return k>rhs.k; }
}node[1001];

int t,n,q,e[101],s[101],tt,len[101];

ld dp[101],dist[101];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	scanf("%d", &t);
	for(int z=1;z<=t;z++){
		scanf("%d %d", &n, &q);
		for(int i=1;i<=n;i++)
			scanf("%d %d", &e[i], &s[i]);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++){
				scanf("%d", &tt);
				if(i+1==j) len[i]=tt;
			}
		scanf("%d %d", &tt, &tt);
		
		dist[n]=0;
		for(int i=n-1;i>=1;i--)
			dist[i]=dist[i+1]+len[i];

		for(int i=1;i<=100;i++)
			dp[i]=1e25;
		
		dp[n]=0;
		for(int i=n;i>=1;i--)
			for(int j=i+1;j<=n;j++)
				if(dist[i]-dist[j]<=e[i])
					dp[i]=min(dp[i],dp[j]+(dist[i]-dist[j])/s[i]);
				else break;

		printf("Case #%d: %.7Lf\n", z, dp[1]+1e-12);
	}

	//fprintf(stderr, "solved.\n");
	//system("pause");
	return 0;
}