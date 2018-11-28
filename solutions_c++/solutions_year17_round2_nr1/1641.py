#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		printf("Case #%d: ", tt);
		double d;
		int n;
		double k, s;
		cin>>d>>n;
		double m=0;
		for(int i=1;i<=n;i++){
			cin>>k>>s;
			m=max(m, (d-k)/s);
		}
		printf("%.6f\n", d/m);
	}
}

