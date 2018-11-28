#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<math.h>

#define ll long long
using namespace std;

int n,m;
char c[1007];

void sol(){
	int i,j;
	scanf("%s %d",&c,&m);
	n=strlen(c);
	int ans=0;
	for(i=0;i<n-m+1;i++){
		if(c[i]=='-'){
			ans++;
			for(j=i;j<i+m;j++){
				if(c[j]=='-')c[j]='+';
				else c[j]='-';
			}
		}
	}
	for(i=n-m+1;i<n;i++){
		if(c[i]=='-'){
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n",ans);

}

int main(){
#pragma comment(linker, "/STACK:1073741824")
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#else
	//freopen("input_file.txt","r",stdin);
	//freopen("output_file.txt","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		//printf("Case #%d:\n",i+1);
		//silly();
		sol();
	}
	return 0;
}