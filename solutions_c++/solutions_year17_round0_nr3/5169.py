#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<double> vd;





int main() {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("Output1.out", "w", stdout);
	int t,n,k,mi,ma;
	cin>>t;
	for(int i=1 ; i<=t ; i++){
		cin>>n>>k;
		while(k>1){
			k--;
			n--;
			n=(n+k%2)/2;
			k=(k+1)/2;

		}

		ma=n/2;
		mi=n-ma-1;
		cout<<"Case #"<<i<<": "<<ma<<" "<<mi<<endl;
	}
}


