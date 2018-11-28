#include <iostream>
#define large unsigned long long
using namespace std;

int main(void) {
	int test, t;
	large n, c, p, k;

	cin>>test;

	for(t=1; t<=test; ++t) {
		cin>>n;
		p = 1;
		for(c=n/10; c; c/=10)
			p*=10;
		c = (p*10-1)/9;
		if(c<=n)
			p=c;
		else
			p = (p-1)/9;

		for(k=p; k; k/=10) {
			while((p+k<=n) && ((p+k)%10))
				p+=k;
		}
		cout<<"Case #"<<t<<": "<<p<<endl;
	}

	return 0;
}