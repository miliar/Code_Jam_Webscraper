#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#define LL long long
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T;
LL n,nn,ans,a[22],b[22],c[22];

bool check() {
	REP(i,a[0]) c[i]=max(c[i-1],b[i]);
	LL temp = 0;
	REP(i,a[0]) temp=temp*10+c[i];
	return temp<=n;
}

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ", T_T);
		cin >> n;
		nn = n;
		a[0] = 0;
		while (n) {
			a[++a[0]] = n % 10;
			n /= 10;
		}
		if (a[0] == 19) {
			cout<<999999999999999999<<endl;
			continue;
		}
		n=nn;
		REP(i,a[0]/2) swap(a[i], a[a[0]+1-i]);
		memset(b, 0, sizeof(b));
		REP(i,a[0])
			for (int j = 9; j >= 0; --j) {
				b[i]=j;
				if (check()) break;
			}
		ans=0;
		REP(i,a[0]) ans=ans*10+b[i];
		cout<<ans<<endl;
	}
}
