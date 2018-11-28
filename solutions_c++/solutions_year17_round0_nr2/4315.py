#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;

int cis(char cis){
	return (int)(cis-'0');
}

int toz(int i){
	return (char)(i + '0');
}

void solve(int test){
	string cif;
	cin>>cif;


	bool zmena = true;
	while(zmena){
		int pred = 0;
		zmena = false;
		REP(a, cif.size()){
			if(zmena){
				cif[a] = toz(9);
				continue;
			}
			if(pred < cis(cif[a])) pred = cis(cif[a]);
			if(pred > cis(cif[a])) {
				cif[a-1] = toz(pred-1);
				zmena = true;
				cif[a] = toz(9);
			}
		}
	}

	printf("Case #%i: ",test);

	REP(a,cif.size()){
		if(a == 0 && cif[a] == toz(0)){
			continue;
		}
		printf("%c",cif[a]);
	}
	printf("\n");

	

}


int main(){
	int t;
	cin>>t;
	REP(a,t) solve(a+1);
	return 0;
}
