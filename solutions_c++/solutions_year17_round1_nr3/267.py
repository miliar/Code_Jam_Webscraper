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
#define dbg(x) //cout<<#x<<"="<<x<<endl
typedef pair<int,int> pii;
typedef long long tint;


int main(){	
	int t;
	cin>>t;
	forn(caso,t){
		cout<<"Case #"<<caso+1<<": ";
		int hd,ad,hk,ak,b,d;
		cin>>hd>>ad>>hk>>ak>>b>>d;
		tint mn=1000000000;
		forn(cantd,101){
			tint res=cantd;
			int vida_dragon=hd;
			int ataque_knight=ak;
			bool ban=false;
			forn(i,cantd){
				if(vida_dragon-(ataque_knight-d)<=0){
					res++;
					vida_dragon=hd-ataque_knight;						
				}
				ataque_knight-=d;
				vida_dragon-=ataque_knight;
				if(vida_dragon<=0){
					ban=true;
					break;
				}
			}
			if(ban)continue;

			int sali_vida_dragon=vida_dragon;
			forn(x,101){
				vida_dragon=sali_vida_dragon;
				int y=ceil(double(hk)/double(x*b+ad));
				int z=x+y;
				tint resp=res+z;
				bool flag=false;
				forn(i,z-1){
					dbg(vida_dragon);
					if(vida_dragon-ataque_knight<=0){
						resp++;
						vida_dragon=hd-ataque_knight;						
					}
					dbg(vida_dragon);
					dbg(ataque_knight);
					vida_dragon=vida_dragon-ataque_knight;
					if(vida_dragon<=0)flag=true;		
				}
				if(resp<mn){
					dbg(cantd);
					dbg(x);
					dbg(y);
				}
				if(!flag)mn=min(mn,resp);
			}			
		}
		if(mn==1000000000){
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<mn<<endl;
		}
	}
	return 0;
}
