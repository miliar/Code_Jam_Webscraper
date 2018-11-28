
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
ll s,c,i,k,j,n,m,z,b; 
ll t,cas,d,i1,a,i2,r,w;
ll ta[10];
string we;
vi vk,vd;
double zx,ax;

int main() {  
//	freopen( "c:\\wojtek\\uva\\uva\\debug\\a0.in", "rt", stdin); 
	
	//pi=2*acos(0.0); 
	//while(1){
	//vk.clear(); 
	//d=1000000007; 
	
		
	
	cin>>t;
	
	for(cas=1;cas<=t;cas++){
		vk.clear();
		vd.clear();
		cin>>d>>n;
		for(int i=0;i<n;i++){
			cin>>a>>b;
			vk.push_back(a);
			vd.push_back(b);
		}
		zx=0.0;
		for(int i=0;i<n;i++){
			ax=(double)(d-vk[i])/vd[i];
			zx=max(zx,ax);
		}
		ax=(double)d/zx;
		
		
		
			cout<<setprecision(18)<<"Case #"<<cas<<": "<<ax<<endl;
		
		

	}
		
	return 0;

} 


