#include<bits/stdc++.h>
#define lli long long int
#define test()  int test;cin>>test;while(test--)
const lli MOD = 1000000007ll;

using namespace std;

int main() {
  	freopen("in", "r", stdin);
  	freopen("out", "w", stdout);
	std::ios_base::sync_with_stdio(false);
  	int tt;
  	cin >> tt;
  	for (int qq = 1; qq <= tt; qq++) {
    	cout << "Case #" << qq << ": ";
    	int d,n;
    	cin >> d >> n;
    	double mx=0;
    	for(int i=0;i<n;i++){
    	    int k,s;
    	    cin >> k >> s;
    	    double dist = ((double)d - (double)k);
    	    mx = max(mx,(double)((double)dist/(double)s));
    	}
    	cout << setprecision(8) << (double)d/(double)mx << endl;
    }
  return 0;
}
