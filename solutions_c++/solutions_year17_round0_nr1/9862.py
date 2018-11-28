#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;

const int MAX_N = 1e3 + 6;

int pre[MAX_N];
bool a[MAX_N];
char c[MAX_N];

int main () {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cases=0;
	while (T--) {
		getchar();
		scanf("%s",c);
//		cout<<"c = "<<c<<endl;
		int n=strlen(c);
		for (int i=1;n>=i;i++) {
			a[i] = (c[i-1]=='+');
		}
		int k;
		scanf("%d",&k);
		memset(pre,0,sizeof(pre));
		int cnt=0;
		for (int i=1;n-k+1>=i;i++) {
			pre[i] = pre[i-1];
			int last=max(1,i-k+1);
			int times=(pre[i-1]-pre[last-1]);
			times%=2;
//			cout<<"a[i] = "<<a[i]<<" , times = "<<times<<endl;
			if ((a[i]^times)==0) {
//				cout<<"i = "<<i<<endl;
				cnt++;
				pre[i]+=1;
			}
		}
//		cout<<"cnt = "<<cnt<<endl;
		bool can=true;
		for (int i=n-k+2;n>=i;i++) {
			pre[i] = pre[i-1];
			int last=max(1,i-k+1);
			int times=(pre[i-1]-pre[last-1]);
			times%=2;
			if ((a[i]^times)==0) {
				can=false;
			}
		}
		printf("Case #%d: ",++cases);
		if (can) printf("%d\n",cnt);
		else puts("IMPOSSIBLE");
	}
}

