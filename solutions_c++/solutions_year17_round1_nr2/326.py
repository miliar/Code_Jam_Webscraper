#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int T,N,P;
int w[50],m[50][50];

int low[50][50],high[50][50];
bool used[50][50];
int start[50];
int idx[50];

 bool comp(int a, int b){
	return (a>b);
 }

 
 
 bool dfs(int I,int m, int M){
	 if(m>M)
		 return false;
	 if(I==N)
		 return true;
	 for(int j=start[I];j<P;j++){
		 if(low[I][j]<=M && m<=high[I][j]){
			 idx[I]=j;

			 if(dfs(I+1,max(m,low[I][j]),min(M,high[I][j])))
				 return true;
		 }
	 }
	 return false;
 }
int main(){
	cin>>T;
	
	for(int cn=1;cn<=T;cn++){
		cin>>N>>P;
		for(int i=0;i<N;i++){
			cin>>w[i];
		}
		for(int i=0;i<N;i++){
			for(int j=0;j<P;j++){
				cin>>m[i][j];
			}
			idx[i]=0;
			sort(m[i],m[i]+P);
		}

		for(int i=0;i<N;i++){
			for(int j=0;j<P;j++){
				low[i][j]=ceil(double(m[i][j])/double(w[i])/1.1);
				high[i][j]=floor(double(m[i][j])/double(w[i])/0.9);
				used[i][j]=0;
			}
		}

		
		int result = 0;
		for(int i=0;i<N;i++)
			idx[i]=start[i]=0;
		while(dfs(0,0,1<<30)){
			result++;
			for(int i=0;i<N;i++)
				start[i]=idx[i]+1;
		}
		
		cout<<"Case #"<<cn<<": "<<result<<'\n';
	}
	
	return 0;
}