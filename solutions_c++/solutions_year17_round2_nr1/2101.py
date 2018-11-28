#include <bits/stdc++.h>

using namespace std;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A_large","w",stdout);


	int t;
	cin >> t;
	for(int p=1;p<=t;p++){
		int d,n;
		cin >> d >> n;
		long double ans = -1;
		long long int x,y;
		for(int i=0;i<n;i++){
			cin >> x >> y;
			long double aux_t = (long double)(d-x)/(long double)y;
			//double aux_ans = (double)d/(double)aux_t;
			ans = max(aux_t,ans);

		}
		cout.precision(6);
		long double aux_ans = (long double)d/(long double)ans;
		cout << "Case #" << p << ": " << fixed << aux_ans << endl;

	}

	return 0;
}