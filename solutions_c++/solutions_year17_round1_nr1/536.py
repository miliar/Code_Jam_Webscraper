#include <bits/stdc++.h>
using namespace std;
char arr[30][30];
int main(){
	int t;
	cin>>t;
	for(int z=1;z<=t;++z){
		int n,m;
		cin>>n>>m;
		for(int i=0;i<n;++i){
			cin>>arr[i];
		}
		for(int i=0;i<n;++i){
			bool color=false;
			for(int j=0;j<m;++j){
				if(arr[i][j]!='?'){
					for(int k=j-1;k>=0&&arr[i][k]=='?';--k)
						arr[i][k]=arr[i][j];
					for(int k=j+1;k< m&&arr[i][k]=='?';++k)
						arr[i][k]=arr[i][j];
					color=true;
				}
			}
			if(color==false&&i>0){
				for(int j=0;j<m;++j)
					arr[i][j]=arr[i-1][j];
			}
		}
		for(int i=n-1;i>=0;--i){
			bool color=false;
			for(int j=0;j<m;++j)
				if(arr[i][j]!='?')
					color=true;
			if(color==false&&i!=n-1){
				for(int j=0;j<m;++j)
					arr[i][j]=arr[i+1][j];
			}
		}
		printf("Case #%d:\n",z);
		for(int i=0;i<n;++i)
			printf("%s\n",arr[i]);
	}
}