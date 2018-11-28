#include <iostream>
#define LL long long int

using namespace std;

LL find_num(LL n) {
	if (n<10) return n;
	 
	int d=0,ld,i;
	LL p=1,m,res,q;
	m=n;
	while(m>0) {
		m/=10;
		d++;
	}
	for (i=0;i<d-1;i++) p*=10;
	
	res = find_num(n%p);
	
	ld=n/p;
	q=p;
	p/=10;
	
	if ( res/p < ld) {
		return ld*q-1;
	}
	return ld*q+res;
}

int main() {
	int T,i=1;
	LL n;
	cin >> T;
	
	while (i<=T) {
		cin >> n;
		cout << "Case #" << i << ": " << find_num(n) << '\n';
		i++; 
	}
	
	return 0;
}
