#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define F first
#define S second
#define X real()
#define Y imag()

const ld INF=1e18;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	cout<<setprecision(15);
	for (int tc=1;tc<=tcs;tc++) {
		int n;
		ld d;
		cin>>d>>n;
		ld parsa=0;
		for (int i=0;i<n;i++) {
			ld k,s;
			cin>>k>>s;
			parsa=max(parsa,(d-k)/s);
		}
		cout<<"Case #" <<tc<<": "<<d/parsa<<"\n";
	}
}
