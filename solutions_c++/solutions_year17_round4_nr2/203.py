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


int ti[1000][1000];
int cant_ti[1000];
int main(){	
	int cant_casos;
	cin>>cant_casos;
	forn(caso,cant_casos){
		int n, c,m;
		cin>>n>>c>>m;
		int p,b;
		forn(i,c)forn(j,n)ti[i][j]=0;
		forn(i,c)cant_ti[i]=0;
		forn(i,m){
			cin>>p>>b;
			ti[b-1][p-1]++;			
			cant_ti[b-1]++;
		}
		int res=0;
		forn(i,c)res=max(res,cant_ti[i]);
		int sum=0;
		forn(j,n){
			forn(i,c)sum+=ti[i][j];
			res=max(res,(sum+j)/(j+1));
		}
		int prom=0;
		forn(j,n){
			int suma=0;
			forn(i,c)suma+=ti[i][j];
			prom+=max(0,suma-res);
		}
		cout<<"Case #"<<caso+1<<": "<<res<<" "<<prom<<endl;
	}

	return 0;
}
