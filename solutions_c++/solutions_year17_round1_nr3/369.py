#include <iostream>
#include <stdio.h>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;

typedef long long ll;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define sz(t) ((int)(t.size())) 


int t,q = 1;
int Hd,Ad,Hk,Ak,B,D;
int Hd1,Ad1,Hk1,Ak1,B1,D1;
int main(){
	scanf("%d", &t);
	while(t){
		printf("Case #%d: ", q);
		t--;
		q++;
		cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
		int Bc = 0, Dc = 0;
		int answ = -1;
		for(Bc = 0; Bc <= 100; Bc++)
			for(Dc = 0; Dc <= 100; Dc++){
				Hd1 = Hd; Ad1 = Ad; Hk1 = Hk; Ak1 = Ak; B1 = B; D1 = D;


				//////////////////////////////////////////////////////////
				int q = 0, s = 0;
				bool z = true;
				while(q < Dc){
					if((Ak-D) >= Hd) {Hd = Hd1; Hd-=Ak;}
					else {Ak-=D; Hd-=Ak;}
					q++;
					s++;
					if(Hd <=0 || s > 210) {z = false; break;} 
				}
				if(!z){
					Hd = Hd1; Ad = Ad1; Hk = Hk1; Ak = Ak1; B = B1; D = D1;
					continue;
				}
				if(Ak < 0) Ak = 0;
				//////////////////////////////////////////////////////////////////
				//if(Bc == 1 && Dc == 0) cout<<Hd<<" "<<Ad<<" "<<Hk<<" "<<Ak<<endl;
				//////////////////////////////////////////////////////////////////
				q = 0;
				while(q < Bc){
					if(Ak >= Hd) {Hd = Hd1; Hd-=Ak;}
					else {Ad+=B; Hd-=Ak;}
					q++;
					s++;
					if(Hd<=0 || s > 420) {z = false; break;} 
				}
				if(!z){
					Hd = Hd1; Ad = Ad1; Hk = Hk1; Ak = Ak1; B = B1; D = D1;
					continue;
				}
				///////////////////////////////////////////////////////////////////////////
				//if(Bc == 1 && Dc == 0) cout<<Hd<<" "<<Ad<<" "<<Hk<<" "<<Ak<<endl;
				/////////////////////////////////////////////////////////////////
				while(Hk > 0){
					if(Ad >= Hk) Hk = 0;
					else if(Ak >= Hd) {Hd = Hd1; Hd-=Ak;}
					else {Hk-=Ad; Hd-=Ak;}
					s++;
					if(Hd<=0 || s > 640) {z = false; break;} 
				}
				if(!z){
					Hd = Hd1; Ad = Ad1; Hk = Hk1; Ak = Ak1; B = B1; D = D1;
					continue;
				}
				///////////////////////////////////////////////////////////////
				if(answ == -1 || answ > s) answ = s;
				Hd = Hd1; Ad = Ad1; Hk = Hk1; Ak = Ak1; B = B1; D = D1;

			}
		if(answ == -1) cout<<"IMPOSSIBLE"<<endl;
		else cout<<answ<<endl;
	}
	return 0;
}