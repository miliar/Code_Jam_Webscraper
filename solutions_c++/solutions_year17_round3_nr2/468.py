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
int per[1501];
int ac,aj;

int memo[1500][1500][2][2];

int dp(int minuto,int cantc,int cantj,int first,int last){
	if(minuto==1440){
		if(cantc==720 && cantj==720){
			if(last==first)return 0;
			return 1;
		}
		return 1<<20;
	}
	
	if(memo[minuto][cantc][first][last]!=-1)return memo[minuto][cantc][first][last];
	int dev=1<<20;
	
	// escoger c
	if(per[minuto]!=0){
		if(last==0){
			dev=min(dev,dp(minuto+1,cantc+1,cantj,first,0) );
		}else{
			dev=min(dev,1+dp(minuto+1,cantc+1,cantj,first,0) );
		}
	}
	
	// escoger j
	if(per[minuto]!=1){
		if(last==1){
			dev=min(dev,dp(minuto+1,cantc,cantj+1,first,1) );
		}else{
			dev=min(dev,1+dp(minuto+1,cantc,cantj+1,first,1) );
		}
	}
	
	
	memo[minuto][cantc][first][last]=dev;
	return dev;
}

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int tc;
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		printf("Case #%d: ",caso);
		cin>>ac>>aj;
		memset(per,-1,sizeof(per));
		memset(memo,-1,sizeof(memo));
		
		//cout<<"ac "<<ac<<" "<<aj<<endl;
		
		for(int i=0;i<ac;i++){
			int a,b;
			cin>>a>>b;
			//cout<<a<<" "<<b<<endl;
			for(int j=a;j<b;j++)
				per[j]=0;
		}

		for(int i=0;i<aj;i++){
			int a,b;
			cin>>a>>b;
			//cout<<a<<" "<<b<<endl;
			for(int j=a;j<b;j++)
				per[j]=1;
		}		
		
		int dev=1<<30;
		if(per[0]==-1){
			dev=min(dp(1,1,0,0,0) , dp(1,0,1,1,1)  );
		}
		
		if(per[0]==0){
			dev=dp(1,0,1,1,1);
		}
		
		if(per[0]==1){
			dev=dp(1,1,0,0,0);
		}
		
		cout<<dev<<endl;
	}
		
	return 0;
}


