#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
long long Case, n, K;
long long minx, maxx;
long long c1, c2, tmpc1, tmpc2;
long long tmpminx, tmpmaxx;
int vi;

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&Case);
	for (int CASE=1; CASE<=Case; CASE++){
		scanf("%I64d%I64d", &n, &K);
		printf("Case #%d: ", CASE);
		for (int i=1; i<70; i++)
			if ( (1ll<<i)-1 >= K ){
				vi = i;
				break;
			}
		maxx = n; c1 = 1;
		minx = n; c2 = 0;
		for (int i=1; i<vi; i++){
			tmpc1=0; tmpc2=0;
			if ((maxx-1)%2ll==0){
				tmpc1 += c1*2ll;
				tmpmaxx = (maxx-1)/2ll;
				if (minx == maxx){
					tmpc1 += c2*2ll;
					tmpminx = tmpmaxx;
				} else
				{
					tmpc1 += c2;
					tmpc2 += c2;
					tmpminx = (minx-1)/2ll;
				}
			} else
			{
				tmpc1 += c1;
				tmpmaxx = maxx-1-(maxx-1)/2ll;
				tmpc2 += c1;
				tmpminx = (maxx-1)/2ll;
				if (minx == maxx){
					tmpc1 += c2;
					tmpc2 += c2;
				} else
					tmpc2 += c2+c2;
			}
			c1 = tmpc1; c2 = tmpc2;
			maxx = tmpmaxx;
			minx = tmpminx;
		}
		if (K-(1ll<<(vi-1))+1 > c1){
			printf("%I64d %I64d\n", (minx-1)-(minx-1)/2ll, (minx-1)/2ll);
		} else
		{
			printf("%I64d %I64d\n", (maxx-1)-(maxx-1)/2ll, (maxx-1)/2ll);
		}
	}
	return 0;
}
