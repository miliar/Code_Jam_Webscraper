#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main(){

	int t,r,c,w=0;
	cin>>t;
	while(t--){
		cin>>r>>c;
		char arr[r][c];
		int b[c];
		for(int i=0;i<c;i++)
			b[i]=0;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cin>>arr[i][j];
				if(arr[i][j]!='?')
					b[j]++;
			}
		}
		int flag=0,flag1=0;
		for(int j=0;j<c;j++){
			if(b[j]==0 && flag1==0)
				continue;
			for(int i=0;i<r;i++){
				if(arr[i][j]=='?' && flag==0)
					continue;
				if(flag==0){
					for(int k=i-1;k>=0;k--)
						arr[k][j]=arr[i][j];
					flag=1;
				}
				if(arr[i][j]=='?')
					arr[i][j]=arr[i-1][j];
			}
			flag=0;
			if(flag1==0){
				for(int k=j-1;k>=0;k--){
					for(int i=0;i<r;i++)
						arr[i][k]=arr[i][k+1];
				}
				flag1=1;
			}
			if(b[j]==0){
					for(int i=0;i<r;i++)
						arr[i][j]=arr[i][j-1];
				
			}
		}
		w++;
		cout<<"Case #"<<w<<":"<<endl;
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<arr[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}