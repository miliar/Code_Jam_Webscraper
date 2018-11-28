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
		
		string s;
		cin>>s;
		
		int desde=0;
		bool baja=false;
		
		forn (i, s.size()-1){
			
			if (s[i]!=s[desde]) desde=i;
			
			baja=baja || (s[i]>s[i+1]);
			
			if (baja) break;
			
		}
		
		cout<<"Case #"<<k+1<<": ";
		
		if (!baja){
			cout<<s;
		}else{
			s[desde]--;
			
			forn(i, desde+1){
				if (i!=0 || s[i]!='0'){
					
					cout<<s[i];
					
					
				}
			}
			
			forsn(i, desde+1, s.size()){
				cout<<9;
			}
			
		}
		cout<<endl;
	}
	

	return 0;
}
