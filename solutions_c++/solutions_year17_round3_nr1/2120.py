// Google Code Jam 
// GCJ20171CA


#include <math.h>
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

class Pan {
	public :
	Pan(double ir, double ih) {r=ir,h=ih,pr2=M_PI*ir*ir,prh=2*M_PI*ir*ih;}
	double r,h,prh,pr2;
};

bool CPanR2(Pan a, Pan b) { return a.pr2<=b.pr2;}
bool CPanRH(Pan a, Pan b) { return a.prh<=b.prh;}


void Run(int no) {
	int i, j, k, m,n,  a,b,d,t,z,tc,mn,nb,kmn,aa,bb,lg,lw,som,mx,lf,rg,x;
	int res;
	ll la, lb,lc,ld,le,lr,ls,lk,lm,lsom,lres,lln,lllf,llrg,lmin,lmax;
	double dres,dsom;
	double da,db,dc,dmn,dmx,dx,dxmn,dxmx;
	string s,st,s2,sres,S;
	char c,c1,c2;
	bool fg, fgpossible;
	
	int N,K;
	vector <Pan> vp,vp2;
	
		
	// Init
	res=0;
	dres=0;
	lres=0;
	sres="";
	
	
	// Entrees
	cin >> N >> K;
	for(i=0;i<N;i++) {
		cin >> da >> db;
		vp.pb(Pan(da,db));
	}
	
	// Exe
	sort(vp.begin(),vp.end(),CPanR2);
	vp2=vp;
	for(i=0;i<N-K+1;i++) {
		vp=vp2;
		da=vp[N-1-i].pr2;
		sort(vp.begin(),vp.end()-i-1,CPanRH);
		for(j=0;j<K;j++) da+=vp[N-1-i-j].prh;
		if(dres<da) dres=da;
	}

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