
#include <iostream>
#include <cmath>
using namespace std;


unsigned getNumberOfDigits (unsigned i){
    return i > 0 ? (int) log10 ((double) i) + 1 : 1;
}

bool tidyNum(unsigned long int x){
	int len = getNumberOfDigits(x);
	int current = x%10;
	int last;

	while ( x /= 10 ){
		len--;
		last = current;
		current = x%10;
		if (last < current)
			return false;
	} return true;
}


unsigned long int lastTidy(unsigned long int x){
	while (x!=0){
		if (tidyNum(x) == true)
			return x;
		x--;
	}
	return 0;
}

void parse(){
	int t;
	cin >> t;

	unsigned long int n;
	for (int i = 1; i <= t; ++i) {
		cin >> n;
		cout << "Case #" << i << ": " << lastTidy(n) << endl;
	}
}


int main(){
	parse();
	return 0;
}








