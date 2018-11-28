
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
#define vii vector<pair<ll,ll> >
#define vvii vector<vector<pair<int,int> > >
#define pii pair<ll,ll>
#define vs vector<string>
ll s,c,i,k,j,n,m,z,b; 
ll t,cas,d,i1,a,i2,r,v;

string wex;
priority_queue<ll> pq;
vii vk1,vk2;
pii p1,p2;

int main() {  
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	
	//pi=2*acos(0.0); 
	//while(1){
	//vk.clear(); 
	//d=1000000007; 
	
		
	
	cin>>t;
	for(cas=1;cas<=t;cas++){
		
		cin>>n>>k; 
		/*
		while(!pq.empty())
			pq.pop();
		pq.push(n);
		for(i=0;i<k-1;i++){
			a=pq.top();
			pq.pop();
			pq.push(a/2);
			if(a%2==1)
				pq.push(a/2);
			else
				pq.push(a/2-1);
		}
		a=pq.top();
		if(a%2==1)
				cout<<"Case #"<<cas<<": "<<a/2<<" "<<a/2<<endl;
			else
				cout<<"Case #"<<cas<<": "<<a/2<<" "<<a/2-1<<endl;



		*/
		if(k==1){
			a=n;
			if(a%2==1)
				cout<<"Case #"<<cas<<": "<<a/2<<" "<<a/2<<endl;
			else
				cout<<"Case #"<<cas<<": "<<a/2<<" "<<a/2-1<<endl;
		}
		else {

			z=0;
			vk1.clear();
			vk2.clear();
			z=0;
			vk1.push_back(MP(n,1));
		
			while(k>z){
				if(vk1.size()==1){
					a=vk1[0].first;
					if(a%2==1)
						vk2.push_back(MP(a/2,2*vk1[0].second));
					else {
						vk2.push_back(MP(a/2,vk1[0].second));
						vk2.push_back(MP(a/2-1,vk1[0].second));
					}
					
				}
				else {
					a=vk1[0].first;
					if(a%2==1)
						vk2.push_back(MP(a/2,2*vk1[0].second));
					else {
						vk2.push_back(MP(a/2,vk1[0].second));
						vk2.push_back(MP(a/2-1,vk1[0].second));
					}
					
					a=vk1[1].first;
					if(a%2==1){
						if(vk2[0].first==a/2)
							vk2[0].second+=2*vk1[1].second;
						else
							vk2[1].second+=2*vk1[1].second;
					}
					else {
						vk2[0].second+=vk1[1].second;
						if(vk2.size()==1)
							vk2.push_back(MP(a/2-1,vk1[1].second));
						else
							vk2[1].second+=vk1[1].second;
					}
					
				}
				z=vk2[0].second;
				if(vk2.size()==2)
					z+=vk2[1].second;
				k-=vk1[0].second;
				if(vk1.size()==2)
					k-=vk1[1].second;
				vk1.swap(vk2);
				vk2.clear();
			}

			if(vk1.size()==1){
				a=vk1[0].first;
			
			}
			else {
				if(k<vk1[0].second+1)
					a=vk1[0].first;
				else
					a=vk1[1].first;
			}
			if(a%2==1)
					cout<<"Case #"<<cas<<": "<<a/2<<" "<<a/2<<endl;
			else
					cout<<"Case #"<<cas<<": "<<a/2<<" "<<a/2-1<<endl;		
		}
		
		
	}

	return 0;

} 


