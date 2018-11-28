#include <cstdio>
#include <sstream>
#include <algorithm>
#include <map>
#include <cmath>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <stdio.h>
using namespace std;
#define forn(i,n) for(int i=0; i<(int)(n); i++)
#define forsn(i,s,n) for(int i=(int)(s); i<(int)(n); i++)
#define fore(i,n) forn(i,n.size())
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define all(n) n.begin(),n.end()
#define dbg(x) cout<<#x<<"="<<x<<endl
typedef pair<int,int> pii;
typedef long long tint;


int n, p;
tint r[100];
int pos[100];

int f(vector<tint> ing){
	tint ingmx=0;
	tint rmx=1;
	//int posmx;
	forn(i,n){
		if(ing[i]*rmx>ingmx*r[i]){
			//posmx=i;
			ingmx=ing[i];
			rmx=r[i];
		}		
	}
	tint ingmn=10000000;
	tint rmn=1;
	int posmn;
	forn(i,n){
		if(ing[i]*rmn<ingmn*r[i]){
			posmn=i;
			ingmn=ing[i];
			rmn=r[i];
		}		
	}
	tint mxpaq=floor(double(ingmn)*10/9/rmn);
	tint mnpaq=ceil(double(ingmx)*10/11/rmx);
	if(mxpaq>=mnpaq)return -1;
	return posmn;	
}

int main(){	
	int t;
	cin>>t;
	forn(caso,t){
		cin>>n>>p;
		forn(i,n)cin>>r[i];
		vector<vector<tint> > list;
		forn(i,n){
			vector<tint> aux(p);
			forn(j,p)cin>>aux[j];
			sort(all(aux));
			list.pb(aux);
		}
		int maxpos=0;
		forn(i,n)pos[i]=0;
		int res=0;
		while(maxpos<p){
			vector<tint> ing;
			forn(i,n)ing.pb(list[i][pos[i]]);
			int ff=f(ing);
			if(ff==-1){
				res++;
				forn(i,n)pos[i]++;
				maxpos++;
			}else{
				pos[ff]++;
				maxpos=max(maxpos,pos[ff]);
			}
		}
		cout<<"Case #"<<caso+1<<": "<<res<<endl;
	}
	return 0;
}
