//Author:CookiC
//#include"stdafx.h"
#include<iostream>
#include<cstring>
#include<cmath>
#include<iomanip>
#define maxn 1010
//#pragma warning(disable : 4996)
using namespace std;

int maxj;
long double R,sum,maxd,d;
long double r[maxn],h[maxn];
bool vis[maxn];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	ios::sync_with_stdio(false);
	
	int T,M,N,K,i,j;
	cin>>M;
	for(T=1;T<=M;++T){
		memset(vis,0,sizeof(vis));
		cin>>N>>K;
		for(i=0;i<N;++i)
			cin>>r[i]>>h[i];
		
		R=0;
		sum=0;
		for(i=0;i<K;++i){
			maxd=0;
			for(j=0;j<N;++j)
				if(!vis[j]){
					d=2*r[j]*h[j]; 
					if(r[j]>R)
						d+=r[j]*r[j]-R*R;
					if(maxd<d){
						maxd=d;
						maxj=j;
					}
				}
			
			sum+=maxd;
			if(r[maxj]>R)
				R=r[maxj];
			vis[maxj]=1;
		}
		
		cout<<"Case #"<<T<<": "<<fixed<<setprecision(9)<<sum*M_PI<<endl;
	}
	return 0;
}

