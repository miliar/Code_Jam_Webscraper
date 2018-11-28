#include <bits/stdc++.h>
using namespace std;
#define lln long long int

int main(){
	lln t;
	cin >> t;
	for(lln i=0;i<t;i++){
		lln n,k;
		cin >> n >> k;
		lln x = log2(k);
		lln z = 1;
		for(lln j=0;j<x;j++){
			z = z*2;
		}
		z = z-1;
		lln bache = k-z;
		lln slots = n-z;
		lln p = slots/(z+1);
		lln q = slots%(z+1);
		cout << "Case #" << i+1 << ": ";
		if(q>=bache){
			if((p+1)%2!=0){
				cout << (p+1)/2 << " " << (p+1)/2 << endl;
			}
			else
				cout << (p+1)/2 << " " << (p+1)/2-1 << endl;
		}
		else{
			if(p%2!=0){
				cout << p/2 << " " << p/2 << endl;
			}
			else
				cout << p/2 << " " << p/2-1 << endl;
		}
	}
	return 0;
}