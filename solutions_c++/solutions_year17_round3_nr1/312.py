#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;

typedef long long LL;

struct pancake{
	int r, h;
	bool operator <(const pancake& a)const{
		return (LL)r*h>(LL)a.r*a.h;
	}
} p[1010];
int Case, n, k;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&Case);
	for (int CASE=1; CASE<=Case; CASE++){
		scanf("%d%d",&n,&k);
		for (int i=0; i<n; i++)
			scanf("%d%d",&p[i].r,&p[i].h);
		sort(p, p+n);
		LL ans = 0;
		for (int i=0; i<n; i++){
			int t = 1;
			LL tmp = (LL)p[i].r*p[i].h*2LL;
			for (int j=0; (j<n)&&(t<k); j++)
			if (i!=j && p[i].r >= p[j].r){
				tmp += (LL)p[j].r*p[j].h*2LL;
				if (++t == k) break;
			}
			if (t < k) continue;
			tmp += (LL)p[i].r*p[i].r;
			if (tmp > ans) ans = tmp;
		}
		double ANS = ans*M_PI;
		printf("Case #%d: %.9lf\n",CASE, ANS);
	}
	return 0;
}
