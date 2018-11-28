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
	bitset<1000> piastra, paletta;
	
	string str;
	int piastra_sz = 0, paletta_sz, i = 0, count = 0;

	cin >> str;
	
	for(char c : str)
		piastra[piastra_sz++] = (c=='-');
	
	
	for(cin >> paletta_sz; i < paletta_sz; ++i)
		paletta[i] = true;
		
	for(i = 0; i <= (piastra_sz - paletta_sz); ++i) {
		if(piastra[i]) {
			piastra ^= paletta;
			++count;
		}
		paletta <<= 1;
	}
	
	if(piastra.any())
		cout << "IMPOSSIBLE";
	else
		cout << count;
	
	cout << endl; 
}

int main() {
	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i)
		solve(i);
}
