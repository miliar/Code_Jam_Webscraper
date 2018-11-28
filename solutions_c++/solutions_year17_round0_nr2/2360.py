// Tidy Numbers 

#include <vector>
#include <string>
#include <iostream>

using namespace std;

typedef unsigned long long int ll;

int digit(ll n, int i){
	for(; i>0; i--)
		n/=(ll)10;

	return n%((ll)10);
}

int main(){
	int T, t;
	cin >> T;

	for(t=0; t<T; t++){
		ll x;
		cin >> x;

		int i, j, k;

		for(k=0; k<20; k++){
			for(i=20; digit(x, i)==0&&i>0; i--);
			for(; i>0&&(digit(x, i)<=digit(x, i-1)); i--);

			if(i!=0){
				for(j=0; j<i; j++)
					x/=(ll)10;

				x--;

				for(j=0; j<i; j++){
					x*=(ll)10;
					x+=(ll)9;
				}
			}
		}

		cout << "Case #" << (t+1) << ": " << x << endl;
	}
}