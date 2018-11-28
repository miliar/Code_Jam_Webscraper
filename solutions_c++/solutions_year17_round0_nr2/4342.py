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

int gcd(int x, int y){
	if(x==0) return y;
	return gcd(y%x, x);
}

int t,m2,curr;
char s[101];

void f1(int x){
	curr='0';
	for(int i=1;i<=x;i++)
		if(s[i]>=curr) curr=s[i];
		else {
			m2=i;
			s[i-1]--;
			f1(i-1);
			break;
		}
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	scanf("%d", &t);
	for(int z=1;z<=t;z++){
		scanf("%s", s+1),m2=0;
		f1(strlen(s+1));
		if(m2)
			for(int i=m2;i<=strlen(s+1);i++)
				s[i]='9';
		printf("Case #%d: %s\n", z, s[1]=='0'?s+2:s+1);
	}
	
	//fprintf(stderr, "solved.\n");
	//system("pause");
	return 0;
}