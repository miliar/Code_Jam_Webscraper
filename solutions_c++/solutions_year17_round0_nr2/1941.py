#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O2")
#define eb emplace_back
#define pb push_back
#define pw(x) ((1LL)<<(x))
#define buli(x) (__builtin_popcountll(x))
typedef long long ll;
typedef double db;
inline void rd(long long &x){
	int sign=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');c=='-'?(sign=-1,x=0):(x=c-'0');
	while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';x*=sign;
}
inline void rd(double&x){scanf("%lf",&x);}
inline void rd(int &x){ll y=0;rd(y);x=y;}


const int inf=1e9;
const int md=1e9+7;
const int maxn=1e5+10;
const db eps=1e-6;
int n,m,T,x,y,z,nk,nq;
long long ans;
int a[maxn];
char s[maxn];
void check(){
	long long  s = 0;
	for(int i = 1; i <= n; ++i){
		if(a[i] < a[i - 1]) return;
		s = s * 10 + a[i];
	}
	ans = max (ans, s);
		
}
void task() {
	scanf("%s",s+1);
	n = strlen(s + 1);
	ans = 0;
	for(int i = 1; i <= n; ++i) a[i] = s[i] - '0';
	check();
	for (int i = 1; i <= n; ++i) if(s[i] > '0') {
		for(int j = 1; j <=n; ++j){
			if(j < i) a[j] = s[j] - '0';
			if(j == i) a[j] = s[j] - '0' - 1;
			if(j > i) a[j] = 9; 
		}
		check();
	}
	cout << ans << endl;
	
}

int main(){
	#ifdef GJY
		freopen("t.in","r",stdin);
		freopen("t.out","w",stdout);
	#endif
	rd(T);
	for(int ti = 1; ti <= T; ++ti){
		printf("Case #%d: ",ti);
		task();
	
	}

}





