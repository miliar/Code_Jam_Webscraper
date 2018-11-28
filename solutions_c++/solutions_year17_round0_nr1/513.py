#include <cstdio>
#include <sstream>
#include <algorithm>
#include <map>
#include <cmath>
#include <iostream>
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


char flip(char c){
	if(c=='-')return '+';
	return '-';	
}

int main(){	
	int t;
	cin>>t;
	forn(caso,t){
		string s;
		int k;
		cin>>s>>k;
		int res=0;
		forn(i,s.size()-k+1){
			if(s[i]=='-'){
				res++;
				forn(j,k)s[i+j]=flip(s[i+j]);
			}			
		}
		bool flag=true;
		forsn(i,s.size()-k,s.size())if(s[i]=='-')flag=false;				
		cout<<"Case #"<<caso+1<<": ";
		if(flag) cout<<res<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}

	return 0;
}
