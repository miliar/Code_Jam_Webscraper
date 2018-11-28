#include<iostream>
#include<algorithm>

using namespace std;

unsigned lastno(unsigned n) {
	unsigned i, rem[10],c = 0, f = 1;
	i = n;

	while(i!=0){
		rem[c] = i%10;
		c++;
		i = i / 10;
	}
	for (i = c-1; i >0; i--) {
		if (rem[i] > rem[i - 1]) {
			f = 0;
			break;
		}
	}
	return (f == 1) ? n : lastno(n - 1);
}

int main()
{
	unsigned t,n,i,no;
	cin >> t;
	for (i = 0; i < t; i++) {
		cin >> no;
		cout << "Case #" << i + 1 << ": " << lastno(no) << endl;
	}
    return 0;
}

