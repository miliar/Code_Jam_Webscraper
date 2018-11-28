#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#define LL long long
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T;
LL a0,a1,b0,b1,p0,p1,q0,q1,n,k;

void Output(LL num) {
	cout << num/2 << " " << (num-1)/2 << endl;
}

void Add(LL a, LL p) {
	if (b0==a/2) q0+=p;
	if (b0==(a-1)/2) q0+=p;
	if (b1==a/2) q1+=p;
	if (b1==(a-1)/2) q1+=p;
}

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ", T_T);
		cin >> n >> k;
		a0 = n, a1 = n+1;
		p0 = 1, p1 = 0;
		while (k) {
			b0 = (a0-1)/2;
			b1 = a1/2;
			q0 = q1 = 0;
			Add(a0,p0);
			Add(a1,p1);
			if (k>p1) k-=p1; else {Output(a1);break;}
			if (k>p0) k-=p0; else {Output(a0);break;}
			a0 = b0; a1 = b1;
			p0 = q0; p1 = q1;
		}
	}
}
