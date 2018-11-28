#include <bits/stdc++.h>
using namespace std;
int t,closed,opened;
long long line[100],b[100];
long long num[100],num0[100];
long long n,k,ans1,ans2;
bool flag;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for (int cas=1;cas<=t;cas++){
		scanf("%lld%lld",&n,&k);
		line[1]=n; closed=1;
		num0[1]=1;
		while (k>0){
			opened=0;
			for (int i=1;i<=closed;i++){
			if (k==0) break;
			for (int k0=1;k0<=num0[i];k0++){
				if (line[i]%2==1){
					flag=false;
					for (int j=1;j<=opened;j++) 
					if (b[j]==line[i]/2){
						flag=true;
						num[j]+=2;
					}
					if (!flag){
						opened++;
						b[opened]=line[i]/2;
						num[opened]=2;
					}
					k--;
					if (k==0){
					ans1=line[i]/2;
					ans2=line[i]/2;
					break;
				    }
				}
				else{
					flag=false;
					for (int j=1;j<=opened;j++) 
					if (b[j]==line[i]/2){
						flag=true;
						num[j]++;
					}
					if (!flag){
						opened++;
						b[opened]=line[i]/2;
						num[opened]=1;
					}
					flag=false;
					for (int j=1;j<=opened;j++) 
					if (b[j]==line[i]/2-1){
						flag=true;
						num[j]++;
					}
					if (!flag){
						opened++;
						b[opened]=line[i]/2-1;
						num[opened]=1;
					}
					k--;
					if (k==0){
					ans1=line[i]/2;
					ans2=line[i]/2-1;
					break;
				}
				}
				
			}
		}
		closed=opened;
		for (int i=1;i<=closed;i++) line[i]=b[i];
		for (int i=1;i<=closed;i++) num0[i]=num[i];
	}
	printf("Case #%d: %d %d\n",cas,ans1,ans2);
}
	fclose(stdin);
	fclose(stdout);
	return 0;
} 
