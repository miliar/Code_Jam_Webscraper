#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	scanf("%d", &tc);
	for (int i=1; i<=tc; i++) {
		int n,p;
		scanf("%d%d", &n, &p);
		int arr[p];
		memset(arr,0,sizeof(arr));
		for (int j=0; j<n; j++) {
			int g;
			scanf("%d", &g);
			arr[g%p]++;
		}
		int tot=arr[0];
		//printf("%d\n", tot);
		//printf("%d %d %d\n", arr[0], arr[1], arr[2]);
		if (p==2) {
			tot+=(arr[1]+1)/2;
		}
		else if (p==3) {
			int mx=0;
			for (int j=0; j<=min(arr[1],arr[2]); j++) {
				int xt=((arr[1]-j)%3==0 && (arr[2]-j)%3==0) ? 0 : 1;
				mx=max(mx,j+(arr[1]-j)/3+(arr[2]-j)/3+xt);
				//printf("%d %d\n", j, mx);
			}
			tot+=mx;
		}
		else if (p==4) {
			//printf("%d %d %d %d\n", arr[0], arr[1], arr[2], arr[3]);
			tot+=arr[2]/2;
			int yt=arr[2]%2;
			int mx=0;
			for (int j=0; j<=min(arr[1],arr[3]); j++) {
				int xt=(yt==0 && (arr[1]-j)%4==0 && (arr[3]-j)%4==0) ? 0 : 1;
				mx=max(mx,j+(arr[1]-j)/4+(arr[3]-j)/4+xt);
				//printf("%d %d\n", j, mx);
			}
			//printf("%d!\n", tot);
			tot+=mx;
			//printf("%d!\n", tot);
		}
		//for (int i=0; i<p; i++) printf("%d ", arr[i]);
		//printf("\n");
		printf("Case #%d: %d\n", i, tot);
	}
}
