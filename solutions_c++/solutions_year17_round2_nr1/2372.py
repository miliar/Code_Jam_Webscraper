//#include "../../stdc++.h"
#include <bits/stdc++.h>

#define forsn(i,s,n) for(int i=s; i<n; i++)
#define forn(i,n) forsn(i,0,n)
#define dforsn(i,s,n) for(int i=n-1; i>=s; i--)
#define dforn(i,n) dforsn(i,0,n)
#define pb push_back
#define snd second
#define fst first

using namespace std;




int main() {
	
	int t;
	cin>>t;
	
	forn(k,t){
		
		int d,n;
		cin>>d>>n;
		
		vector<double> init(n);
		vector<double> speed(n);
		
		forn(i,n){
			
			cin>>init[i]>>speed[i];
		}
		
		int last=0;
		double when=(d-init[0])/speed[0];
		
		forn(i,n){
			if (when<(d-init[i])/speed[i]){
				when=(d-init[i])/speed[i];
				last=i;
			}
			//cerr<<"when: "<<when<<endl;
		}
		
		
		
		
		
		cout<<"Case #"<<k+1<<": "<< fixed<<setprecision(6)<<((double)d)/when  <<endl;
	}
	

	return 0;
}
