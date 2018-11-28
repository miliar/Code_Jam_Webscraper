#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<queue>
#include<algorith>
#include<math.h>
#include<map>
#include<stack>
#include<string.h>
#define STOP system("pause")
#define bits(num) __builtin_popcount(num)
#define CASE int t;scanf("%d",&t);while(t--)
#define ll long long int
#define lu unsigned long long
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
using namespace std;
int main()
{
	CASE{
		int n,q,i,j,k,dis[102][102],a[104][104],d[104],s[105];
		cin>>n>>q;
		for(i=1;i<=n;i++){
			cin>>d[i]>>s[i];
		}
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				cin>>dis[i][j];
			}	
		}		
		double dp[102][102];
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				for(k=1;k<=n;k++){
					if(dis[i][k]==-1||dis[k][j]==-1)
					continue;
					if(dis[i][j]==-1)
					dis[i][j] = dis[i][k]+dis[k][j];
					else
					dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j]);
				}
				dp[i][j]=1e15;
			}
		}
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				for(k=1;k<=n;k++){
					if(dis[i][k]!=-1&&dis[k][j]!=-1){				
						if(d[i]>=dis[i][k]&&d[k]>=dis[k][j]){
							dp[i][j] = min(dp[i][j],(double)(dis[i][k]/s[i]+dis[k][j])/s[k]);
						}
					}
					if(dis[i][j]==-1)
					continue;
					if(d[i]>=dis[i][j]){
						dp[i][j] = min(dp[i][j],(double)dis[i][j]/s[i]);
					}
				}
			}
		}
		while(q--){
			cin>>temp1>>temp2;
			printf("%.6f\n",dp[temp1][temp2]);
		}
		cout<<endl;
	}
    return 0;
}

