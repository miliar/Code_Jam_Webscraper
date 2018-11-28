#include <cstdio>
#include <sstream>
#include <algorithm>
#include <map>
#include <cmath>
#include <iostream>
#include <set>
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


int main(){	
	int cant_casos;
	cin>>cant_casos;
	forn(caso,cant_casos){
		int n, p;
		int res;
		cin>>n>>p;
		vector<int> cant(p);
		int aux;
		forn(i,n){
			cin>>aux;
			cant[aux%p]++;
		}
		if(p==2){
			res=cant[0]+(cant[1]+1)/2;			
		}
		if(p==3){
			int mn=min(cant[1],cant[2]);
			int mx=max(cant[1],cant[2]);
			res=cant[0]+mn+(mx-mn+2)/3;
		}
		if(p==4){
			res=cant[0]+cant[2]/2;
			int mn=min(cant[1],cant[3]);
			int mx=max(cant[1],cant[3]);
			res+=mn;
			int quedan=mx-mn;
			if(cant[2]%2==0){
				res+=(quedan+3)/4;				
			}else{
				res++;
				if(quedan>2){
					res+=(quedan-2+3)/4;					
				}
			}
		}
		cout<<"Case #"<<caso+1<<": "<<res<<endl;
	}

	return 0;
}
