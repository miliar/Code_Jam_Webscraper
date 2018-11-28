#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int ans, Case;
long long n, nn, a[30];
int tot, vi;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&Case);
	for (int CASE=1; CASE<=Case; CASE++){
		printf("Case #%d: ", CASE);
		scanf("%I64d", &n);
		nn = n; tot = 0;
		while (nn>0){
			a[tot++] = nn%10ll;
			nn /= 10ll;
		}
		/*ex[0] = 1;
		for (int i=0; i<19; i++)
			ex[i] = ex[i-1]*10ll;
		ans = 0;
		for (int i=tot-1; i>=0; i--){
			long long dig = ans, p;
			if (i==tot-1 || a[i]>=last)
				p = a[i];
			else 
			for (int j=i; j>=0; j--)
				dig += a[i]*ex[j];
			if (dig <= n){
				ans += a[i]*ex[j];
				continue;
			}
		}*/
		a[tot] = 0; vi=-1;
		for (int i=tot-1; i>=0; i--){
			if (a[i]<a[i+1]){
				vi = i+1;
				break;
			}
		}
		if (vi>=0){
			for (int i=vi; i<tot; i++){
				if (a[i] > a[i+1]){
					a[i]--;
					for (int j=i-1; j>=0; j--)
						a[j] = 9;
					break;
				}
			}
		}
		long long ans = 0;
		for (int i=tot-1; i>=0; i--)
			ans = ans*10ll+a[i];
		printf("%I64d\n",ans);
	}
	return 0;
}
