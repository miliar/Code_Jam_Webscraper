#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <bitset>
#include <string>

/*#include <gmpxx.h>
	mpz_class i = 1;
	for(int j = 1; j < 10*_case; ++j) {
		i+=j;
		i*=i;
//		i*= j;
	}
*/

using namespace std;

void solve(int _case) {
	cout << "Case #" << _case << ": ";
	string number;
	
	cin >> number;
	
	// La regola: si scorre verso destra finchè si può.
	// Quando non si può più, da li in poi sono 9.
	int i = 1, j = number.length();
	char c;
	for(; i < number.length(); ++i){
		if(number[i] < number[i-1]) {
			// TROVATO!
			j = i-1;
			c = number[j];
			for(;i < number.length(); ++i)
				number[i] = '9';
		}
	}
	
	for(; j >= 0 && number[j] == c; --j)
		number[j] = '9';
	
	// Il primo della serie invece deve essere messo a c-1
	if(j != number.length())
		number[j+1] = c-1;
	
	
	
	cout << (number.c_str() + number.find_first_not_of('0'));

	cout << endl; 
}

int main() {
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i)
		solve(i);
}
