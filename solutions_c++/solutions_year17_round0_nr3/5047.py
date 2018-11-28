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
		
		multiset<unsigned long long> s;
		
		unsigned long long n,m;
		cin>>n>>m;
		
		s.insert(n);
		unsigned long long izq,der, mizq, mder;
		
		forn(i,m){
			auto it=s.end();
			
			
			it--;
			
			n=*it;
			
			izq=der=n>>1;
			if (!(n&1)) der--;
			
			if (i!=m-1){
				
				s.insert(it,izq);
				
				s.insert(it,der);
				s.erase(it);
				//if (s.size()%1000==0) cerr<<s.size()<<endl;
			}
			
		}
		
		
		
		
		
		
		cout<<"Case #"<<k+1<<": "<< izq <<' '<< der<<endl;
	}
	

	return 0;
}
