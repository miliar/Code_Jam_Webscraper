
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
vii vk,vk2;
string we,wy,wx;


int main() {  
//	freopen( "c:\\wojtek\\uva\\uva\\debug\\a0.in", "rt", stdin); 
	
	//pi=2*acos(0.0); 
	//while(1){
	//vk.clear(); 
	//d=1000000007; 
	
		
	
	cin>>t;
	
	for(cas=1;cas<=t;cas++){
		
		cin>>we;
		wy.clear();
		n=we.size();
		k=-1;
		z=0;
		for(i=0;i<n-1;i++){
			if((we[i]==we[i+1])&&(k<0))
				k=i;
			else if(we[i]>we[i+1]){
				if(k<0){
					if((i>0)||(we[i]>'1')){
						wx.assign(n-i-1,'9');
						wy+=we[i]-1;
						wy+=wx;
						z=1;
						break;
					}
					else {
						wx.assign(n-i-1,'9');
						
						wy+=wx;
						z=1;
						break;
					}
				}
				else {
					if((k>0)||(we[i]>'1'))
						wy+=we[i]-1;
					wx.assign(n-k-1,'9');
					wy+=wx;
					z=1;
					break;
				}
			}
			else if (we[i]<we[i+1]){
				if(k>=0){
					wx.assign(i-k+1,we[i]);
					k=-1;
					wy+=wx;
				}
				else
					wy+=we[i];
			}
		}
		if(z==0){
			if(k>=0){
				wx.assign(i-k+1,we[i]);
				k=-1;
				wy+=wx;
			}
			else
				wy+=we[n-1];
		}
		cout<<"Case #"<<cas<<": "<<wy<<endl;
		

	}
		
	return 0;

} 


