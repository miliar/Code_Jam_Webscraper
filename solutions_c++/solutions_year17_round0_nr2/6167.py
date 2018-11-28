#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <cmath>
#include <string>
#include <set>
#include <deque>
#include <cctype>
#include <bitset>
#include <regex>

using namespace std;

#define For(i, n) for(int (i) = 0; (i) < (n); (i)++)

void solve(int T){
	long long n, old, maxi = 1, nine = 0, base = 1, bb;
	cin >> n;
	old = n;
	For(i, 18) base *= 10;
	while(base > n) base /= 10;
	bb = base;

	while(base > 1){
		if( (n / base) % 10 > (n / (base / 10)) % 10 ){
			n = n - base;
			n = (n / base) * base + base - 1;
		//	cout << "odp = " << n << endl;
		//	maxi = max(maxi, base);
			base *= 100;
		//	break;
		}
		base /= 10;
	}

//	cout << "maxi = " << maxi  << "   n= " << n << endl;

//	n = (n / maxi) * maxi + maxi - 1;

	cout << "Case #" <<  T + 1 << ": " << n << endl;
}

int main(){
	int T;
	cin >> T;
	For(i, T) solve(i);
	return 0;
}
