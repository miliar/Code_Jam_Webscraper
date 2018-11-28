#include <iostream>
#include <math.h>
#define ALREADY_TIDY -1
using namespace std;

typedef unsigned long long ulong;


int first_index_not_tidy(ulong n) {
    int ndigits = 0;
    ulong naux = n;
    while(naux > 0) {
        ++ndigits;
        naux /= 10;
    }
    for (int i = ndigits - 1; i > 0; --i) {
        ulong first = n/ulong(pow(10,i))%10;
        ulong second = n/ulong(pow(10,i-1))%10;
        if (first > second) return i; 
    }
    return ALREADY_TIDY;
}

bool index_pair_not_tidy(int i, ulong n) {
    ulong first = n/ulong(pow(10,i))%10;
    ulong second = n/ulong(pow(10,i-1))%10;
    return (first > second);
}

ulong substract_until_tidy(int i,ulong n) {
    ulong p = ulong(pow(10,i));
    return n/p*p-1;    
}

ulong last_tidy_number(ulong n) {
    int i = first_index_not_tidy(n);
    if (i == ALREADY_TIDY) return n;
    while (index_pair_not_tidy(i,n)) {
        n = substract_until_tidy(i,n);
        i += 1;
    }
    return n;
}
    

int main() {
	int t;
    ulong n;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		cin >> n;
        cout << last_tidy_number(n) << endl;
	}
}
