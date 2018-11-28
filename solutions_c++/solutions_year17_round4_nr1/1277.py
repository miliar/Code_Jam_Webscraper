#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(v) ((int)v.size())

typedef long long ll;
typedef long double ld;

int t, q = 0;

int n, p;
int g[102];
int dd = 0;
int answ = 0;
int mk = 0, erku = 0;

int a,b,c,d;
int main(){
	cin>>t;
	while(t){
		t--;
		q++;
		cout<<"Case #"<<q<<": ";
		cin>>n>>p;
		dd = 0;
		mk = 0; erku = 0;
		a = b = c = d = 0;
		for(int i = 0; i < n; ++i){
			cin>>g[i];
			if(g[i] % 2 == 1) dd++;
			if(g[i] % 3 == 1) mk++;
			if(g[i] % 3 == 2) erku++;

			if(g[i] % 4 == 0) a++;
			if(g[i] % 4 == 1) b++;
			if(g[i] % 4 == 2) c++;
			if(g[i] % 4 == 3) d++;
		}
		answ = 0;
		if(p == 2){
			answ = n - dd / 2;
		}
		else{
			if(p == 3){
				answ = n - min(mk, erku);
				if(mk > erku) {
					answ -= mk - erku;
					answ += (mk - erku) / 3;
					if((mk - erku) % 3 !=0) answ++;
				}
				else {
					answ -= erku - mk;
					answ += (erku - mk) / 3;
					if((erku - mk) % 3 !=0) answ++;
				}
			}
			else{
				answ += a;
				answ += min(b, d);
				if(d > b){
					int k = d - b;
					answ += k / 4;
					if(c % 2 == 0){
						answ += c/2;
						if(k % 4 != 0) answ++;
					}
					else{
						if(k % 4 == 0){
							answ += c / 2 + 1;
						}
						else if(k % 4 == 1){
							answ += c / 2 + 1;
						}
						else if(k % 4 == 2){
							answ += c / 2 + 1;
						}
						else if(k % 4 == 3){
							answ += c / 2 + 2;
						}
					}
				}
				else{

					int k = b - d;
					answ += k / 4;
					if(c % 2 == 0){
						answ += c/2;
						if(k % 4 != 0) answ++;
					}
					else{
						if(k % 4 == 0){
							answ += c / 2 + 1;
						}
						else if(k % 4 == 1){
							answ += c / 2 + 1;
						}
						else if(k % 4 == 2){
							answ += c / 2 + 1;
						}
						else if(k % 4 == 3){
							answ += c / 2 + 2;
						}
					}
				}
			}
		}
		cout<<answ<<endl;
		cout<<endl;
	}
	return 0;
}






