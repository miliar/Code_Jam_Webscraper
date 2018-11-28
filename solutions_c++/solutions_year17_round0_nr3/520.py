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
typedef long long tint;
typedef pair<tint,tint> pii;


pii f(tint n,tint k){
	if(k==1)return mp(n/2,(n-1)/2);
	k--; 
	if (k%2==0)return f((n-1)/2,k/2);
	else return f(n/2,(k+1)/2);
}

int main(){	
	int t;
	cin>>t;
	forn(caso,t){
		tint n,k;
		cin>>n>>k;
		pii res=f(n,k);
		cout<<"Case #"<<caso+1<<": "<<res.f<<" "<<res.s<<endl;
	}

	return 0;
}
