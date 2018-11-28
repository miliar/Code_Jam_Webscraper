#include <bits/stdc++.h>
using namespace std;

void fun() {
	long double d,k;
	long double a,b;
	cin >> d >> k;
	long double tim= 0;
	vector<pair<long,long> > v;
	for(int l=0;l<k;l++) {
		cin >> a >> b;
		v.push_back({a,b});
		tim = max(tim,(d-a)/b);
	}
	cout << fixed << setprecision(8) << d/tim;
}

int main(){
	int n;
	cin >> n;
	for(int i=1;i<=n;i++) {
		cout << "Case #" << i << ": ";
		fun();
		cout << endl;
	}

    return 0;
}