#include <iostream>
using namespace std;


typedef unsigned long long ull;

int main(){
	int tests;
	cin >> tests;
	for (int test=1; test <= tests; test++){
		ull n,k;
		cin >> n >> k;
		string rev;
		while (k > 1){
			
			rev+= char('0' + k%2);
			k/=2;
		}
		
		ull h,l;
		h = n/2;
		l = (n-1)/2;
		for (int i =0; i < rev.length(); i++){
			ull s = (rev[i] == '1' ? l : h);
			h = s/2;
			l = (s-1)/2;
		}
		
		
		cout << "Case #" << test << ": ";
		cout << h << " " << l;
		cout << endl;
		
	}
	
	
	return 0;
}