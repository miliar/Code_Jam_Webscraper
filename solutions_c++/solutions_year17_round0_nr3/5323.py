#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;

int intlog2(unsigned long long n)
{
    for(int i=0; i<64; i++) {
        if (n==1)
            return i;
        n >>= 1;
    }
    return 0;
}

unsigned long long pow2(int p)
{
    return 1<<p;    
}

string run_test(unsigned long long n, unsigned long long k)
{
    auto l = intlog2(k);
    auto nb = pow2(l+1);

    if (n+1 < nb)
        return "0 0";
    auto bt = n-nb+1;
    auto np = pow2(l);
    auto bp = bt/np;
    auto r = bt%np;
    auto x = np-n+k+bt;
    auto a = x<=r?1:0;
    auto p = bp+a;
    auto min = p/2;
    auto max = min+p%2;

    return to_string(max) + " " + to_string(min);
}

int main()
{
	string line;
	cin>>line;

	auto n_tests = stoi(line);	

	for(int i = 0; i < n_tests; i++) {        
        unsigned long long n;
		cin>>n;
        unsigned long long k;
        cin>>k;

		cout<<"Case #"<<i+1<<": ";

		auto result = run_test(n, k);

		cout<<result<<"\n";	
	}
}
