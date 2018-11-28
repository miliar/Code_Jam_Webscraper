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


int main(){	
	int t;
	cin>>t;
	forn(caso,t){
		int r,c;
		cin>>r>>c;
		int cont=0;
		bool ini=true;
		string res="";
		cout<<"Case #"<<caso+1<<":"<<endl;
		forn(i,r){
			bool flag=false;
			string s;
			cin>>s;
			char letra;
			forn(j,c)if(s[j]!='?'){
				flag=true;
				letra=s[j];
				break;
			}
			if (flag){
				res="";
				forn(j,c){
					if(s[j]!='?')letra=s[j];
					res+=letra;
				}
				cout<<res<<endl;
				if(ini){
					ini=false;
					forn(j,cont)cout<<res<<endl;
				}
			}else{
				if(ini){
					cont++;
				}else{
					cout<<res<<endl;
				}
			}
			
		}
	}
	return 0;
}
