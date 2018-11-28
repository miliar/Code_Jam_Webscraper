#include <iostream>
#include <math.h>
using namespace std;

int test(unsigned long j) {
	long tmp;
	int i = 1;
	while(j>0) {
		tmp = j % 10;
		j = j / 10;
        if(j%10>tmp) {return i;}
        i++;
	}
    return 0;
}

int main() {
	unsigned long n, j, t, dig, a, b, c;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		j = n;
		while(j>0) {
			dig = test(j);
			if(dig==0) {
				break;
			}
			else {
				//j = j/(10^dig)*(10^dig)-1;
				
				a = pow(10, dig);
				b = j / a;
				c = b * a;
				j = c - 1;
				//cout << "dig=" << dig << ";  a=" << a << ";  b=" << b << ";  c=" << c << ";  j=" << j << endl;
			}
		}
		cout << "Case #" << i << ": " << j << endl;
	}
    return 0;
}
