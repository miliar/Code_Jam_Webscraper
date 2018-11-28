#include <bits/stdc++.h>
using namespace std;
#define maxn 2020

int ans[maxn];
char col[6]= {'R', 'O', 'Y', 'G', 'B', 'V'};
int s[6], t[6];
int n;

bool judge(){
	for (int i=0;i<n;i++)
		if (ans[i]==ans[(i+1)%n])
			return 0;
	return 1;
}

int main()
{
	freopen("B-small2.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d",&n);
		int mx=0, st;
		memset(s,0,sizeof(s));

		for (int i=0;i<6;i++){
			scanf("%d",&s[i]);
			if ((i%2)==0){
				if (s[i]>mx){
					mx=s[i];
					st=i;
				}
			}
		}

		// t[1]=s[1];
		// t[3]=s[3];
		// t[5]=s[5];
		// s[0]-=s[3];
		// s[2]-=s[5];
		// s[4]-=s[1];

		for (int i=0;i<n;i+=2){
			if (s[st]<=0) st=(st+2)%6;
			ans[i]=st;
			s[st]--;
		}
		for (int i=1;i<n;i+=2){
			if (s[st]<=0) st=(st+2)%6;
			ans[i]=st;
			s[st]--;
		}
		printf("Case #%d: ",o);
		if (!judge()){
			printf("IMPOSSIBLE\n");
		}
		else{
			for (int i=0;i<n;i++)
				printf("%c",col[ans[i]]);
			printf("\n");
		}
	}
	return 0;
}