#include <bits/stdc++.h>
using namespace std;
#define lln long long int

int main(){
	lln t;
	cin >> t;
	for(lln i=0;i<t;i++){
		lln d,n;
		double ans = INT_MIN;
		cin >> d >> n;
		for(lln j=0;j<n;j++){
			double k,s,tim;
			cin >> k >> s;
			lln dis = d-k;
			tim = (double)dis/s;
			if(tim>ans)
				ans = tim;
		}
		cout << "Case #" << i+1 << ": ";
		float sol = (double)d/ans;
		printf("%.10f\n",sol);
	}
	return 0;
}