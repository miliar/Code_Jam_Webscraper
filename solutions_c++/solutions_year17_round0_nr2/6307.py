#include <iostream> 
#include <cstdio>

using namespace std;



long long t, n;
string s;

long long ans;
long long calc(long long x) {	
	long long res = 0;
	if (x > n) return 0;
 	if (x != 0) res++; 
 	ans = max(ans, x);
 	int e = max(1ll, x % 10);
 	for (int i = e; i <= 9; i++)
 		res += calc(x*10 + i);
 	return res;

}
int main(){
 	cin >> t;
 	for (int i = 1; i <= t; i++) {
 		cout << "Case #" << i << ": ";
 		cin >> n;
 	
 	     ans = 0;
 	     calc(0);
// 		cout << calc(0) << endl;
 		cout << ans << endl;
 	 
 	}
}