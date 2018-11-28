// Google Code Jam 
// GCJ2017QRA


#include <istream>
#include <iostream>
#include <cstdio>
#include <vector>
#include <ctime>
#include <algorithm>
#include <string>
#include <fstream>
#include <sstream>
#include <iomanip>      // std::setprecision

#define pb(x) push_back(x)
#define ll long long

using namespace std;



void Run() {
	int i, j, k, m,n,  a,b,d,t,z,tc,mn,nb,kmn,aa,bb,lg,lw,som,mx,lf,rg,x;
	int res,N,no;
	ll la, lb,lc,lk,lsom,lres,lln,lllf,llrg;
	double dres,dsom;
	double da,db,dc,dmn,dmx,dx,dxmn,dxmx;
	string s,st,s2,sres,S;
	char c;
	bool fg, fgpossible;
	
	
	
	// Init Tout debut
	
	
	// Lecture début
	cin >> N;

	
	// Init éventuelle
	
	// do {
	for(no=1;no<=N;no++) {
		// Reset du tour precedent (dont vectors) !
		
		// Reserve
		
		// Init
		res=0;
		dres=0;
		lres=0;
		sres="";
		
		
		// Entrees
		cin >> s >> k;
		
		// Exe
		m=s.size();
		for(i=0;i<=m-k;i++) {
			if(s[i]=='-') {
				res++;
				for(j=i;j<i+k;j++) 
					if(s[j]=='-') s[j]='+'; else s[j]='-';
			}
		}
		for(i=0;i<m;i++) if(s[i]=='-') break;
		
		
		// Sortie
		if(i!=m) cout << "Case #" << no <<  ": " << "IMPOSSIBLE\n";
		else  cout << "Case #" << no <<  ": " << res << "\n";
		
		// Si une seule Exec
		// break;
	} 
	// } while (true);
	
}




int main(int argc, char** argv) {
	std::ios::sync_with_stdio(false);
	unsigned int i;

	//printf("Code Jam\n");
	Run();


	return 0;
}