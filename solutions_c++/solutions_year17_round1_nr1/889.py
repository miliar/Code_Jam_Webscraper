#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int>vi;
typedef pair<int,int>ii;
int n,m;
string M[50];
map<char,int>L;
bool ver(int a, int b){
	for(int i=0;i<=a;i++)
		for(int j=0;j<=b;j++)
			if(M[i][j]!='?' and L[M[i][j]]==0)
				return 0;
	return 1;
}
int main(){
	int test;
	cin>>test;
	for(int te=1;te<=test;te++){
		cin>>n>>m;
		L.clear();
		for(int i=0;i<n;i++)
			cin>>M[i];
		
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				if(M[i][j]!='?' and L[M[i][j]]==0){
					L[M[i][j]]=1;
					int a=i,b=j;
					for(int k=i;k<n;k++)
						for(int l=j;l<m;l++){
							if(ver(k,l)){
								a=k;b=l;
							}
						}
					for(int k=0;k<=a;k++)
						for(int l=0;l<=b;l++){
							if(M[k][l]=='?')M[k][l]=M[i][j];
						}
				}
			}
		printf("Case #%d:\n",te);
		for(int i=0;i<n;i++)cout<<M[i]<<endl;
	}
	return 0;
}