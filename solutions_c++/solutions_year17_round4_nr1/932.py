#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<sstream>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
using namespace std;
int N,P;
int memo[101][101][101][5];

int dp(int uno,int dos,int tres,int residuo){
	if(uno+dos+tres<=1)return 0;
	if(memo[uno][dos][tres][residuo]!=-1)return memo[uno][dos][tres][residuo];
	int dev=1<<30;
	
	if(uno>0){
		if( (residuo+1)%P!=0){
			dev=min(dev,1+dp(uno-1,dos,tres,(residuo+1)%P ));
		}else{
			dev=min(dev,dp(uno-1,dos,tres,(residuo+1)%P ));
		}
	}
	
	if(dos>0){
		if( (residuo+2)%P!=0){
			dev=min(dev,1+dp(uno,dos-1,tres,(residuo+2)%P ));
		}else{
			dev=min(dev,dp(uno,dos-1,tres,(residuo+2)%P ));
		}
	}
	
	if(tres>0){
		if( (residuo+3)%P!=0){
			dev=min(dev,1+dp(uno,dos,tres-1,(residuo+3)%P ));
		}else{
			dev=min(dev,dp(uno,dos,tres-1,(residuo+3)%P ));
		}
	}
	
	
	
	memo[uno][dos][tres][residuo]=dev;
	return dev;
}

int main() {
	//ffreopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int tc;
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		cin>>N>>P;	
		memset(memo,-1,sizeof(memo));
		
		int uno=0;int dos=0;int tres=0;
		int c[101];
		
		for(int i=0;i<N;i++){
			cin>>c[i];
			c[i]=c[i]%P;
			if(c[i]==1)uno++;
			if(c[i]==2)dos++;
			if(c[i]==3)tres++;	
		}
		
		cout<<N-dp(uno,dos,tres,0)<<endl;
	}	
	
	return 0;
}
