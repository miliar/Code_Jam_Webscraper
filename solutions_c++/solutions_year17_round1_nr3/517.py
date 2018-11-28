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
int visited[105][105][105][105];
struct nodo{
	int hd,ad,hk,ak;
	nodo(int _hd,int _ad,int _hk,int _ak){
		hd=_hd;
		ad=_ad;
		hk=_hk;
		ak=_ak;
	}
};


int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	
	int tc;
	cin>>tc;
	
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		
		memset(visited,-1,sizeof(visited));
		queue<nodo>Q;
		
		int _hd,_ad,_hk,_ak,b,d;
		cin>>_hd>>_ad>>_hk>>_ak>>b>>d;
		
		Q.push(nodo(_hd,_ad,_hk,_ak));
		visited[_hd][_ad][_hk][_ak]=0;
		int ans=-1;
		
		while(!Q.empty()){
			nodo P=Q.front();
			Q.pop();
			
			int hd=P.hd;
			int ad=P.ad;
			int hk=P.hk;
			int ak=P.ak;
			//cout<<"----- "<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<" "<<b<<" "<<d<<endl;
			if(hk==0){
				ans=visited[hd][ad][hk][ak];
				break;
			}
			
			int value=visited[hd][ad][hk][ak];
			
			if(ad>=hk){
				ans=value+1;
				break;
			}
			
			// atacar
			if(hd-ak>0){
				if(visited[hd-ak][ad][max(0,hk-ad)][ak] ==-1){
					visited[hd-ak][ad][max(0,hk-ad)][ak]=value+1;
					Q.push(nodo(hd-ak,ad,max(0,hk-ad),ak));
				}
			}
			
			//curar
			if(_hd-ak>0){
				if(visited[_hd-ak][ad][hk][ak] ==-1){
					visited[_hd-ak][ad][hk][ak]=value+1;
					Q.push(nodo(_hd-ak,ad,hk,ak));
				}
			}
			
			//buff
			if(hd-ak>0){
				if(visited[hd-ak][min(ad+b,hk) ][hk][ak] ==-1){
					visited[hd-ak][min(ad+b,hk)][hk][ak]=value+1;
					Q.push(nodo(hd-ak,min(ad+b,hk),hk,ak));
				}
			}
			
			//debuff
			int a2=max(0,ak-d);
			if(hd-a2>0){
				if(visited[hd-a2][ad][hk][a2] ==-1){
					visited[hd-a2][ad][hk][a2]=value+1;
					Q.push(nodo(hd-a2,ad,hk,a2));
				}
			}
			
		}
		
		if(ans!=-1)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	
	return 0;
}


