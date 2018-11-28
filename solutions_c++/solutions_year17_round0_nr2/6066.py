#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
LL ori, x;
int a[50], b[50];
int n;

bool judge(int r, int p){
	LL y=0;
	for (int i=n;i>=r+1;i--)
		y=y*10+b[i];
	for (int i=r;i>=1;i--)
		y=y*10+p;
	//cout<<y<<endl;
	return y<=ori;
}

bool low(int *a, int n){
	for (int i=n;i>=1;i--)
		if (a[i]>1) return 0;
	return 1;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%I64d",&ori);
		if (ori<=1){
			printf("Case #%d: %d\n", o, ori);
			continue;
		}
		x=ori;
		n=0;
		while (x){
			a[++n]=x%10;
			x/=10;
		}
		if (low(a, n)){
			n--;
			ori=0;
			for (int i=1;i<=n;i++) a[i]=9, ori=ori*10+9;
		}
		//printf("%I64d\n", ori);
		for (int i=n;i>=1;i--){
			for (int k=9;k>=0;k--)
				if (judge(i, k)){
					b[i]=k;
					break;
				}
		}
		printf("Case #%d: ",o);
		for (int i=n;i>=1;i--)
			if (b[i]){
				for (int j=i;j>=1;j--)
					printf("%d", b[j]);
				printf("\n");
				break;
			}
	}
	return 0;
}