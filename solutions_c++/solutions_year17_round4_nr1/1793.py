#include <bits/stdc++.h>
#define pi acos(-1.0)
using namespace std;
int n,m,l;
int a[1004];
int b[1004];
int ans1;
int check(int x,int y,int z){
	int need[5];
	need[1]=need[2]=need[3]=0;
	int tmp;
	if (l == 2) {
		need[1]+=2*x;
		tmp=x;
	}
	if (l == 3) {
		need[1]+=x*3+y;
		need[2]+=y+z*3;
		tmp=x+y+z;
	}
	if (l == 4) {
		need[1]+=x+2*z;
		need[2]=2*y+z;
		need[3]=x;
		tmp=x+y+z;
	}
	if (need[1]>b[1]) return 0;
	if (need[2]>b[2]) return 0;
	if (need[3]>b[3]) return 0;
	if (need[1]+need[2]+need[3]<b[1]+b[2]+b[3])
		tmp++;
	ans1 = max(ans1,tmp);
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while(T--){ 
		int ans = 0;
		ans1=0;
		scanf("%d%d",&n,&l);
		b[1]=b[2]=b[3]=0;
		for (int i=1;i<=n;i++){
			scanf("%d",&a[i]);
			a[i]=a[i]%l;
			if (!a[i]) ans++;
			b[a[i]]++;
		}
		for (int i=0;i<=100;i++)
			for (int j=0;j<=100;j++)
				for (int k=0;k<=100;k++)
					check(i,j,k);
		printf("Case #%d: %d\n",++ca,ans+ans1 );
	}
	return 0;
}