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


int tab[200][200];
int ini[200][200];

int main(){	
	int t;
	cin>>t;
	forn(caso,t){
		tint n,k;
		cin>>n>>k;
		forn(i,n)forn(j,n)tab[i][j]=0;
		forn(i,n)forn(j,n)ini[i][j]=0;
		int x,y;
		char c;
		int posx=0;
		int posy=0;
		forn(i,k){
			cin>>c>>x>>y;
			if(c=='+')ini[x-1][y-1]=1;
			if(c=='x')ini[x-1][y-1]=2;
			if(c=='o')ini[x-1][y-1]=3;
			if(c=='x' || c=='o'){
				posx=x-1;
				posy=y-1;
			}
		}
		forn(j,n)tab[0][j]=1;
		forsn(j,1,n-1)tab[n-1][j]=1;
		forn(k,n)tab[(posx+k)%n][(posy+k)%n]+=2;
		int score=3*n-2;
		if(n==1)score=2;
		int upgrade=0;
		forn(i,n)forn(j,n)if(tab[i][j]!=ini[i][j])upgrade++;
		cout<<"Case #"<<caso+1<<": "<<score<<" "<<upgrade<<endl;
		forn(i,n)forn(j,n){
			if(tab[i][j]!=ini[i][j]){
				if(tab[i][j]==1)cout<<'+';
				if(tab[i][j]==2)cout<<'x';
				if(tab[i][j]==3)cout<<'o';
				cout<<" "<<i+1<<" "<<j+1<<endl;
			}
		}
	}

	return 0;
}
