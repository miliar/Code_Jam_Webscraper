#include<bits\stdc++.h>
using namespace std;
main(){
	freopen("A-large.in","r",stdin);
	freopen("outputA.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		char cake[50][50];
		vector<char> name[30];
		int n,m,k,i,j;
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++){
			scanf("%s",cake[i]);
		}
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(cake[i][j]!='?'){
					name[i].push_back(cake[i][j]);
				}
			}
		}
		char ans[50][50];
		for(i=0;i<=n;i++){
			for(j=0;j<m;j++) ans[i][j]='0';
			ans[i][j]=0;
		}
		for(i=0;i<n;i++){
			if(name[i].size()==0){
				for(j=0;j<m;j++){
					ans[i+1][j]=ans[i][j];
				}
				continue;
			}
			k=0;
			for(j=0;j<m;j++){
				if(cake[i][j]!='?'&&cake[i][j]!=name[i][k]){
					k++;
				}
				ans[i+1][j]=name[i][k];
			}
		}
		/*for(i=1;i<=n;i++){
			for(j=0;j<m;j++){
				printf("%c",ans[i][j]);
			}
			printf("\n");
		}*/
		for(i=n;i>0;i--){
			if(ans[i][0]=='0'){
				for(j=0;j<m;j++){
					ans[i][j]=ans[i+1][j];
				}
			}
		}
		printf("Case #%d:\n",t);
		for(i=1;i<=n;i++){
			printf("%s\n",ans[i]);
		}
	}
} 
