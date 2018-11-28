// Google Code Jam 
// GCJ20171BA


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



void Run(int no) {
	int i, j, k, m,n,  a,b,d,t,z,tc,mn,nb,kmn,aa,bb,lg,lw,som,mx,lf,rg,x;
	int res;
	ll la, lb,lc,ld,le,lr,ls,lk,lm,lsom,lres,lln,lllf,llrg,lmin,lmax;
	double dres,dsom;
	double da,db,dc,dmn,dmx,dx,dxmn,dxmx;
	string s,st,s2,sres,S;
	char c,c1,c2;
	bool fg, fgpossible;
	
	double D,N;
	vector <double> vt;
	
	
		
	// Init
	res=0;
	dres=0;
	lres=0;
	sres="";
	
	
	// Entrees
	cin >> D >> N;
	for(i=0;i<N;i++) {
		cin >> da >> db;
		vt.pb((D-da)/db);
	}			
	
	// Exe
	sort(vt.begin(),vt.end());
	dres=D/vt[N-1];

	// Sortie
	cout << setprecision(15);
	cout << "Case #" << no <<  ": " << dres <<  "\n";
}




int main(int argc, char** argv) {
	std::ios::sync_with_stdio(false);
	int no,T;

	cin >> T;
	for(no=1;no<=T;no++) Run(no);


	return 0;
}