#include <iostream>
#include <cstdio>
using namespace std;

int main(){
	int t,n;
	double d;
	cin >> t;
	for(int a = 0;a < t;a++){
		double ma = 0;
		cin >> d >> n;
		for(int i = 0;i < n;i++){
			double k,s;
			cin >> k >> s;
			ma = max(ma,(d - k) / s);
		}
		printf("Case #%d: %.9lf\n",a + 1,d / ma);
	}
	return 0;
}