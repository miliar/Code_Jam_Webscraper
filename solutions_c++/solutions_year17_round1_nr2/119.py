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

int main() {
	int q;
	cin >> q;
	

	for(int z=1; z<=q; z++){
		int hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		int dlo = -1;
		int dhi = ce(ak, d);
		int blo = -1;
		int bhi = ce(hk-ad,b);
		cout << "Case #" << z << ":" << endl; 
		
	}
	return 0;
}