#include <cstdio>
#include <sstream>
#include <algorithm>
#include <map>
#include <cmath>
#include <iostream>
#include <set>
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


char tab[100][100];
bool hor[100][100];
bool ver[100][100];
bool pintado[100][100];
bool libre[100][100];

pii up[100][100];
pii down[100][100];
pii le[100][100];
pii ri[100][100];

int r,c;
void pintar_hor(int i,int j){
	int auxj=j;
	while(auxj<c && tab[i][auxj]!='#'){
		pintado[i][auxj]=true;
		auxj++;
	}
	auxj=j;
	while(auxj>=0 && tab[i][auxj]!='#'){
		pintado[i][auxj]=true;
		auxj--;
	}					
}

void pintar_ver(int i, int j){
	int auxi=i;
	while(auxi<r && tab[auxi][j]!='#'){
		pintado[auxi][j]=true;
		auxi++;
	}
	auxi=i;
	while(auxi>=0 && tab[auxi][j]!='#'){
		pintado[auxi][j]=true;
		auxi--;
	}
}

bool f(){
	forn(i,r)forn(j,c)if(tab[i][j]=='.' && pintado[i][j]==false)
	if(up[i][j]==mp(-1,-1) || hor[up[i][j].f][up[i][j].s])
	if(down[i][j]==mp(-1,-1) || hor[down[i][j].f][down[i][j].s])
	if(le[i][j]==mp(-1,-1) || ver[le[i][j].f][le[i][j].s])
	if(ri[i][j]==mp(-1,-1) || ver[ri[i][j].f][ri[i][j].s])
	return false;
	return true;
}

bool g(){
	forn(i,r)forn(j,c)if(tab[i][j]=='.' && pintado[i][j]==false)
	if(up[i][j]==mp(-1,-1) || hor[up[i][j].f][up[i][j].s])
	if(down[i][j]==mp(-1,-1) || hor[down[i][j].f][down[i][j].s]){
		if(le[i][j]==mp(-1,-1) || ver[le[i][j].f][le[i][j].s]){
			pii l=ri[i][j];
			hor[l.f][l.s]=true;
			pintar_hor(l.f,l.s);
			return true;
		}
		if(ri[i][j]==mp(-1,-1) || ver[ri[i][j].f][ri[i][j].s]){
			pii l=le[i][j];
			hor[l.f][l.s]=true;
			pintar_hor(l.f,l.s);
			return true;
		}
	}
	return false;
}



int main(){	
	int cant_casos;
	cin>>cant_casos;
	forn(caso,cant_casos){
		cin>>r>>c;
		char a;
		forn(i,r)forn(j,c){
			cin>>a;
			if(a=='|' || a=='-')a='l';
			tab[i][j]=a;
		}
		forn(i,r)forn(j,c){
			hor[i][j]=false;
			ver[i][j]=false;
		}
		forn(i,r){
			bool flag=false;
			int last=0;
			forn(j,c){
				if(tab[i][j]=='#')flag=false;
				if(tab[i][j]=='l'){
					if(flag){
						ver[i][j]=true;
						ver[i][last]=true;
					}
					flag=true;
					last=j;
				}			
			}
		}
		forn(j,c){
			bool flag=false;
			int last=0;
			forn(i,r){
				if(tab[i][j]=='#')flag=false;
				if(tab[i][j]=='l'){
					if(flag){
						hor[i][j]=true;
						hor[last][j]=true;
					}
					flag=true;
					last=i;
				}			
			}
		}
		bool imposible=false;
		forn(i,r)forn(j,c)if(hor[i][j] && ver[i][j])imposible=true;
		if(imposible){
			cout<<"Case #"<<caso+1<<": IMPOSSIBLE"<<endl;
		}else{
			forn(i,r)forn(j,c)if(tab[i][j]=='.'){
				up[i][j]=mp(-1,-1);
				down[i][j]=mp(-1,-1);
				le[i][j]=mp(-1,-1);
				ri[i][j]=mp(-1,-1);
				int auxi=i;
				while(auxi>=0 && tab[auxi][j]!='#'){
					if(tab[auxi][j]=='l'){
						up[i][j]=mp(auxi,j);
						break;
					}
					auxi--;
				}
				auxi=i;
				while(auxi<r && tab[auxi][j]!='#'){
					if(tab[auxi][j]=='l'){
						down[i][j]=mp(auxi,j);
						break;
					}
					auxi++;
				}
				int auxj=j;
				while(auxj>=0 && tab[i][auxj]!='#'){
					if(tab[i][auxj]=='l'){
						le[i][j]=mp(i,auxj);
						break;
					}
					auxj--;
				}
				auxj=j;
				while(auxj<c && tab[i][auxj]!='#'){
					if(tab[i][auxj]=='l'){
						ri[i][j]=mp(i,auxj);
						break;
					}
					auxj++;
				}				
			}
			forn(i,r)forn(j,c)pintado[i][j]=false;
			forn(i,r)forn(j,c)libre[i][j]=false;
			forn(i,r)forn(j,c){
				if(ver[i][j]){
					pintar_ver(i,j);
				}
				if(hor[i][j]){
					pintar_hor(i,j);
				}
			}
			if(f()==false){
				cout<<"Case #"<<caso+1<<": IMPOSSIBLE"<<endl;
			}else{
				bool flag=true;
				while(g()){
					if(f()==false){
						cout<<"Case #"<<caso+1<<": IMPOSSIBLE"<<endl;
						flag=false;
						break;
					}
				}
				if(flag){
					forn(i,r)forn(j,c)if(tab[i][j]=='l')if(!hor[i][j])ver[i][j]=true;
					if(f()==false){
						cout<<"Case #"<<caso+1<<": IMPOSSIBLE"<<endl;
					}else{
						cout<<"Case #"<<caso+1<<": POSSIBLE"<<endl;
						forn(i,r){
							forn(j,c){
								if(tab[i][j]!='l'){
									cout<<tab[i][j];
								}else{
									if(ver[i][j])cout<<'|';
									if(hor[i][j])cout<<'-';
								}
							}
							cout<<endl;
						}
					}				
				}							
			}
		}
	}

	return 0;
}
