#include <bits/stdc++.h>
using namespace std;

int q;
int n, p;
int c[42];

int main()
{
	scanf("%d", &q);
for(int x=1; x<=q; x++) {
	scanf("%d%d", &n, &p);
	for(int i=0; i<p; i++) c[i]=0;
	for(int i=0; i<n; i++) {
		int g;
		scanf("%d", &g);
		c[g%p]++;
	}
	int ans=1;
	ans+=min(c[0], n-1);
	if(p==2) {
		ans+=(c[1]-1)/2;
	} else if(p==3) {
		if(c[1]>c[2]) {
			ans+=c[2];
			c[1]-=c[2];
			ans+=(c[1]-1)/3;
		} else if(c[2]>c[1]) {
			ans+=c[1];
			c[2]-=c[1];
			ans+=(c[2]-1)/3;
		} else {
			if(c[1]>0) ans+=c[1]-1;
		}
	} else {
		if(c[1]>c[3]) {
			ans+=c[3];
			c[1]-=c[3];
			ans+=c[2]/2;
			c[2]%=2;
			if(c[2]>0) {
				if(c[1]>2) ans+=1+(c[1]-3)/4;
			} else {
				if(c[1]>4) {
					ans+=(c[1]-1)/4;
				}
			}
		} else if(c[1]<c[3]) {
			ans+=c[1];
			c[3]-=c[1];
			ans+=c[2]/2;
			c[2]%=2;
			if(c[2]>0) {
				if(c[3]>2) ans+=1+(c[3]-3)/4;
			} else {
				if(c[3]>4) {
					ans+=(c[3]-1)/4;
				}
			}
		} else {
			if(c[1]>0) {
				ans+=c[2]/2;
				c[2]%=2;
				if(c[2]>0) {
					ans+=c[1];
				} else {
					ans+=c[1]-1;
				}
			} else {
				if(c[2]>0) {
					ans+=(c[2]-1)/2;
				}
			}
		}
	}
	printf("Case #%d: %d\n", x, ans);
}

	return 0;
}
