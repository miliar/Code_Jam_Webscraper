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
#include <stdlib.h> 
using namespace std;

int tam1=0;int tam2=0;int tam3=0;
int memo[38000000][3][3];

bool dp(int R,int Y,int B,int inicio,int last){
	if(R+Y+B==0)return 1;
	if(R+Y+B==1){
		if(R==1)return (0!=last &&  0!=inicio);
		if(Y==1)return (1!=last &&  1!=inicio);
		if(B==1)return (2!=last &&  2!=inicio);
	}
	
	//if(memo.find(nodo(R,Y,B,inicio,last))!=memo.end() )
	//	return memo[nodo(R,Y,B,inicio,last)];
		
	if(memo[R*tam1*tam2+Y*tam1 +B][inicio][last]!=-1)return memo[R*tam1*tam2+Y*tam1 +B][inicio][last];
	
	int dev=0;
	
	if(R>0 && last!=0){
		dev=dev|dp(R-1,Y,B,inicio,0);
	}
	
	if(Y>0 && last!=1){
		dev=dev|dp(R,Y-1,B,inicio,1);
	}
	
	if(B>0 && last!=2){
		dev=dev|dp(R,Y,B-1,inicio,2);
	}
	
	memo[R*tam1*tam2+Y*tam1 +B][inicio][last]=dev;
	return dev;
}

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int tc;
	cin>>tc;
		
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		int N;
		cin>>N;
		int R,O,Y,G,B,V;
		cin>>R>>O>>Y>>G>>B>>V;
		tam3=R;tam2=Y;tam1=B;
		memset(memo,-1,sizeof(memo));
		string ans="";
		int inicio=0;
		int last;
		int total=R+Y+B;
		bool ok=1;
		for(int i=0;i<total;i++){
			if(i==0){
				inicio=0;
				if(R>0 &&dp(R-1,Y,B,inicio,inicio) ){
					R--;
					inicio=0;
					last=inicio;
					ans+="R";
					continue;
				}
				
				inicio=1;
				if(Y>0 &&dp(R,Y-1,B,inicio,inicio) ){
					Y--;
					inicio=1;
					last=inicio;
					ans+="Y";
					continue;
				}
				
				inicio=2;
				if(B>0 &&dp(R,Y,B-1,inicio,inicio) ){
					B--;
					inicio=2;
					last=inicio;
					ans+="B";
					continue;
				}
				
				ok=0;
				break;
			}else{
				
				if(R>0 && last!=0 && dp(R-1,Y,B,inicio,0) ){
					R--;
					last=0;
					ans+="R";
					continue;
				}

				if(Y>0 && last!=1 &&dp(R,Y-1,B,inicio,1) ){
					Y--;
					last=1;
					ans+="Y";
					continue;
				}
				
				if(B>0 &&last!=2 && dp(R,Y,B-1,inicio,2) ){
					B--;
					last=2;
					ans+="B";
					continue;
				}
					
			}
		}
		
		
		if(ok==0)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}
	
	return 0;
}


