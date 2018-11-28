#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;cin >> t;
	for(int tt=1;tt<=t;tt++)
	{
		long long int n,k;cin >> n;cin >> k;
		long long int blocks = pow(2,floor(log(k)/log(2)));
		long long int rem = (n-blocks+1)%blocks, div = (n-blocks+1)/blocks;
		if(k-blocks+1 <= rem ) div++;
		if(div%2==0) cout << "Case #" << tt << ": " << div/2 << ' ' << (div/2)-1 << endl;
		else cout << "Case #" << tt << ": "  << (div-1)/2 << ' ' << (div-1)/2 << endl;
	}
}