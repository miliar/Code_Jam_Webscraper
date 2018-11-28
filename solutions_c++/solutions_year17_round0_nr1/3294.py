#include <bits/stdc++.h>
using namespace std;
int t,n;
char a[1005];
int main() {
	cin >> t;
	int no=0;
	while(t--) {
		scanf("%s %d",a,&n);
		int len = strlen(a);
		int ans=0;
		for(int i=0;i+n-1<len;i++) {
			if(a[i]=='-') {
				ans++;
				for(int j=0;j<n;j++) {
					if(a[i+j]=='-') a[i+j]='+';
					else a[i+j]='-';
				}
			}
		}
		int mark=0;
		for(int i=0;i<len;i++) {
			if(a[i]=='-') mark=1;
		}
		no++;
		printf("Case #%d: ",no); 
		if(mark) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
}