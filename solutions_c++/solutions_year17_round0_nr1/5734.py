#include<bits/stdc++.h>
using namespace std;

int t;
int n,k;
char arr[1005];

int main(){
	FILE *fout = fopen("output_a.txt","w");
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		for(int i=0;i<=1000;i++){
			arr[i]=' ';
		}
		scanf("%s %d",arr,&k);
		n=0; int cnt=0;
		while(arr[n]=='+' || arr[n]=='-') n++;
		for(int i=0;i<=n-k;i++){
			if(arr[i]=='-'){
				cnt++;
				for(int j=i;j<i+k;j++){
					if(arr[j]=='+') arr[j]='-';
					else arr[j]='+';
				}
			}
		}
		bool cek=false;
		for(int i=0;i<n;i++){
			if(arr[i]=='-') cek=true;
		}
		if(!cek){
			printf("Case #%d: %d\n",tc,cnt);
			fprintf(fout,"Case #%d: %d\n",tc,cnt);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n",tc);
			fprintf(fout,"Case #%d: IMPOSSIBLE\n",tc);
		}
	}
	return 0;
}
