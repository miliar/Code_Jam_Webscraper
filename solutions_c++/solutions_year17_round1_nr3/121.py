#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define mp make_pair
#define ll long long
#define pb push_back
#define vi vector<ll>

int ce(int a, int b){
	if(a%b==0){
		return a/b;
	}
	return 1 + (a/b);
}

int hd, ad, hk, ak, b, d;
int chd, cad, chk, cak;

int solve(int bn, int dn){
	int an = ce(hk, ad+bn*b);
	//cout << an << endl;
	chd = hd;
	cad = ad;
	chk = hk;
	cak = ak;
	
	int cn = 0;
	for(int i=0; i<dn; i++){
		cak-=d;
		chd-=cak;
		if(chd<=0){
			return -1;
		}
		if((chd<=max(cak - d, 0) && i<dn-1) || (chd<=max(cak, 0) && i==dn-1) ){
			cn++;
			chd = hd-cak;
		}
	}

	for(int i=0; i<(an+bn); i++){

		chd -= cak;
		if(chd<=0 && i<(an+bn-1)){
			return -1;
		}
		if(chd<=cak && i<(an+bn-2)){
			//cout << i;
			cn++;
			chd = hd-cak;
		}
	}
	return an+bn+cn+dn;
}

int main() {
	int q;
	cin >> q;
	

	for(int z=1; z<=q; z++){
		
		cin >> hd >> ad >> hk >> ak >> b >> d;
		int min = 0x7FFFFFFF;
		//cout << solve(0, 0) << endl;
		for(int dn = 0; dn < 101; dn++){
			for(int bn = 0; bn<101; bn++){

				//cout << bn <<" " << dn << endl;
				
				int ans = solve(bn, dn);
				if(solve(bn, dn) ==4){
					//cout << bn << " " << dn << endl;
				}
				if(ans !=-1 && ans<min){
					min = ans;
				}
			}
		}
		if(min == 0x7FFFFFFF){
			cout << "Case #" << z << ": IMPOSSIBLE"<< endl; 
		}else{
			cout << "Case #" << z << ": " << min << endl; 
		}
		
	}
	return 0;
}