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
int N,C,M;

int main() {
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int tc;
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		cin>>N>>C>>M;
		int cont1[1004];
		int cont2[1004];
		
		memset(cont1,0,sizeof(cont1));
		memset(cont2,0,sizeof(cont2));
		
		for(int i=0;i<M;i++){
			int p,b;
			cin>>p>>b;
			if(b==1)cont1[p]++;
			if(b==2)cont2[p]++;
		}
		
		int maxi=0;
		int sum=0;
		
		for(int i=1;i<=N;i++)sum+=cont1[i];
		maxi=max(maxi,sum);
		sum=0;
		for(int i=1;i<=N;i++)sum+=cont2[i];
		maxi=max(maxi,sum);
		
		int mini=0;
		//maxi=max(maxi,cont1[1]+cont2[1]);
		while(true){
			int sum=0;
			bool triste=0;
			mini=0;
			
			for(int i=1;i<=N;i++){
				sum+=cont1[i]+cont2[i];
				if(sum>maxi*i ){
					triste=1;
					break;
				}
				
				if(cont1[i]+cont2[i]>maxi){
					mini+=cont1[i]+cont2[i]-maxi;
				}
				
			}
			
			if(triste){
				maxi++;
				continue;
			}else{
				break;
			}
			
		}
		
		cout<<maxi<<" "<<mini<<endl;
	}	
	
	return 0;
}
