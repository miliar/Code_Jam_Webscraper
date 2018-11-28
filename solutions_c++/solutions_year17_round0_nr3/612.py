// Google Code Jam 
// GCJ2017QRC


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
	ll la, lb,lc,ld,le,lr,ls,lk,lm,lsom,lres,lln,lllf,llrg,lmin,lmax;
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
		cin >> la >> lk;
		
		// Exe
		lb=0;
		m=0;
		while (lk>lb+(((ll)1)<<m)) lb+=((ll)1)<<m++;
		ld=((ll)1)<<m;
		lm=la-lb;
		le=lm/ld;
		lr=lm-le*ld;
		//cout << lb << " " << m << " " << ld << " " << lm << " " << le << " " << lr << "\n";
		if((lk!=lb)&&((lk-lb)<=lr)) ls=le+1;
		else ls=le;
		if((ls%2)==1) lmin=ls/2, lmax=ls/2;
		else lmin=(ls-1)/2, lmax=ls/2;
		
		// Sortie
		cout << "Case #" << no <<  ": " << lmax << " " << lmin << "\n";
		
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