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

void voltear(string &v, int desde, int tam){
	forn(i,tam){
		if (v[desde+i]=='+'){
			v[desde+i]='-';
		}else{
			v[desde+i]='+';
		}
	}
	return;
}

int main() {
	
	int t;
	cin>>t;
	
	forn(k,t){
		int ans=0;
		
		string vec;
		
		cin>>vec;
		
		
		int tam; 
		cin>>tam;
		
		
		forn (i, vec.size()-tam){
			if (vec[i]=='-'){
				ans++;
				voltear(vec, i, tam);			

			}
		}
		
		bool bans=true;
		forsn (i, vec.size()-tam, vec.size()){
			bans=bans && (vec[i]=='+');
		}
		
		bool bans2=true;
		forsn (i, vec.size()-tam, vec.size()){
			bans2=bans2 && (vec[i]=='-');
		}
		
		
		
		
		if (bans || bans2){
			if (!bans) ans++;
			cout<<"Case #"<<k+1<<": "<< ans  <<endl;
		}else{
			cout<<"Case #"<<k+1<<": "<< "IMPOSSIBLE" <<endl;
		}
		
	}
	

	return 0;
}
