#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<unsigned long long> v;
void fun(unsigned long long n) {
    if(n == 0)
    return;
    else {
        v.push_back(n);
        unsigned long long l = (n - 1) / 2;
        unsigned long long r = (n - 1 - l);
        fun(r);
        fun(l);
    }
}
int main() {
	unsigned long long t;
	cin >> t;
	for (unsigned long long T = 1; T <= t; T++) {
	    unsigned long long n, k;
	    cin >> n >> k;
	    fun(n);
	    sort(v.begin(), v.end());
	    reverse(v.begin(), v.end());
	    unsigned long long l=(v[k - 1] - 1) / 2; 
	    unsigned long long r=v[k - 1] - 1 - l;
	    cout << "Case #" << T << ": " << r << " " << l <<endl;
	    v.clear();
	}
	return 0;
}






































