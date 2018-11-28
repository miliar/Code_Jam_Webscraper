
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long i8;
int n, p, g[105], os[5][105], co[5], su[5][105];

int hm(int a, int i, int j, int k) {
	int to=i+2*j+3*k;
	int pr=
		su[0][co[0]]-su[0][a] +
		su[1][co[1]]-su[1][i] +
		su[2][co[2]]-su[2][j] +
		su[3][co[3]]-su[3][k];
	if (pr>=to) {
		if (a+i+j+k>n)
			printf("  n=%d p=%d re=%d\n", n,p,a+i+j+k);
		return a+i+j+k;
	}
	return 0;
}

int solve() {
	scanf("%d%d",&n,&p);

	for (int o=0; o<4; o++)
		co[o]=0;

	for (int i=0; i<n; i++) {
		scanf("%d", g+i);
		int o=g[i]%p;
		os[o][co[o]++]=g[i];
	}
	
	for (int o=0; o<4; o++) {
		sort(os[o],os[o]+co[o]);
		for (int i=0; i<co[o]; i++)
			su[o][i+1]=su[o][i]+os[o][i];
	}
	
	int re=co[0], x;
	switch (p) {
		case 2:	
			re += (co[1]+1)/2; 
			break;
		case 3:
			x=min(co[1],co[2]);
			re += x;
			co[1]-=x; co[2]-=x;
			re += (co[1]+2)/3;
			re += (co[2]+2)/3;
			break;
		case 4:
			x=min(co[1],co[3]);
			re += x;
			co[1]-=x; co[3]-=x;
			re += co[2]/2;
			co[2]%=2;
			if (co[2]) {
				if (co[1]>1) {
					co[2]=0;
					re++;
					co[1]-=2;
				}
				if (co[3]>1) {
					co[2]=0;
					re++;
					co[2]-=2;
				}
			}
			re += (co[1]+3)/4;
			re += (co[2]+3)/4;
			re += (co[2]+3)/4;
	}
	return re;
}

main() {
	int ccnt;
	scanf("%d", &ccnt);
	for (int cs=1; cs<=ccnt; cs++) {
		printf("Case #%d: %d\n", cs, solve());
	}
}
