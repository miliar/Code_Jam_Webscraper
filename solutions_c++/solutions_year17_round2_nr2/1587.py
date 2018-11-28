
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h> 
#include <map>  
#include <string>
#include <vector>  
#include <list> 
#include <iostream>   
#include <sstream>  
#include <queue> 
#include <algorithm>
#include <fstream>
#include <iomanip>


using namespace std; 

#define INF 2000000000
#define FT first
#define SD second
#define PB push_back
#define ll long long
#define PB 		push_back
#define FOR(a,start,end) 	for(int a=int(start); a<int(end); a++)
//#define INF 		int_MAX
#define SORT(a) 	sort(a.begin(),a.end())
#define CL(a,x) 		memset(a,x,sizeof(a))
#define REP(a,x)	for(int a=0;a<x;a++)
#define REP1(a,x)	for(int a=1;a<=x;a++)
#define MP 		make_pair
#define vi vector<int>
#define vvi vector<vector<int> >
#define vii vector<pair<int,int> >
#define vvii vector<vector<pair<int,int> > >
#define pii pair<int,int>
#define vs vector<string>
ll s,c,i,k,j,n,m,z,b,o,y,g,v,r; 
ll t,cas,d,i1,a,i2,w;
ll ta[10];
vi vk,vk2;
string we,wy,wx;
priority_queue<pii> pq;
pii p1;
vii vp;

int main() {  
//	freopen( "c:\\wojtek\\uva\\uva\\debug\\a0.in", "rt", stdin); 
	
	//pi=2*acos(0.0); 
	//while(1){
	//vk.clear(); 
	//d=1000000007; 
	
		
	
	cin>>t;
	
	for(cas=1;cas<=t;cas++){
		vp.clear();
		cin>>n>>r>>o>>y>>g>>b>>v;

		


		while(!pq.empty())
			pq.pop();
		z=0;
		if(r>0){
			pq.push(MP(r,1));
			z=1;
		}
		if(y>0){
			pq.push(MP(y,2));
			z=2;
		}
		if(o>0){
			pq.push(MP(o,3));
			z=3;
		}
		if(b>0){
			pq.push(MP(b,4));
			z=4;
		}
		
		if(v>0){
			pq.push(MP(v,5));
			z=5;
		}
		if(g>0){
			pq.push(MP(g,6));
			z=6;
		}
		vp.clear();
		p1=pq.top();
		pq.pop();
		while(p1.second!=z){
			vp.push_back(p1);
			p1=pq.top();
			pq.pop();
		}

		vk.clear();
		
		vk.push_back(p1.second);
		p1.first--;
		if(p1.first>0)
			pq.push(p1);
		for(int i=0;i<vp.size();i++)
			pq.push(vp[i]);
		z=1;
		for(i=1;i<n;i++){
			vp.clear();
			
			while(!pq.empty()){
				p1=pq.top();
				pq.pop();
				if(((vk[i-1])&(p1.second))>0){
					vp.push_back(p1);
				}
				else {
					vk.push_back(p1.second);
					p1.first--;
					if(p1.first>0)
						pq.push(p1);
					for(int i=0;i<vp.size();i++)
						pq.push(vp[i]);
					break;
				}
			}
			
			if(pq.empty()&&(i<n-1)){
				z=0;
				break;
			}
			
		}
		if(vk.size()<n)
			z=0;
		if(z==1){
			if((vk[0]&(vk[n-1]))>0)
				z=0;
		}
		if(z==0)
			cout<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
		else {
			we.clear();
			for(int i=0;i<n;i++){
				if(vk[i]==1)
					we+='R';
				if(vk[i]==2)
					we+='Y';
				if(vk[i]==4)
					we+='B';
				if(vk[i]==3)
					we+='O';
				if(vk[i]==6)
					we+='G';
				if(vk[i]==5)
					we+='V';
			}
			cout<<"Case #"<<cas<<": "<<we<<endl;
		}

	}
		
	return 0;

} 


