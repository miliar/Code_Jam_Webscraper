#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int t,n,p,a;
vector<int> choc;

void solve(int Case){
	cin >> n >> p;
	choc.assign(p+1, 0);
	for(unsigned i = 0; i < n; ++i) {
		cin >> a;
		choc[a%p]++;
	}
	int num = 0;
	if(p==2){
		num += choc[0];
		num += (choc[1] + 1)/2;
	}else if(p==3){
		num += choc[0];
		num += min(choc[1], choc[2]);
		int lov = abs(choc[2] - choc[1]);
		num += (lov+2)/3;

	}else{
		num += choc[0];
		num += min(choc[1],choc[3]);
		int lov = abs(choc[1] - choc[3]);
		if(choc[2]%2==1)lov+=2;
		num += choc[2]/2;
		num += (lov+3)/4;
	}

	cout << "Case #" << Case << ": " << num << "\n";
	return;
}

int main()
{
	cin >> t;
	for (int i = 0; i < t; ++i){
		solve(i+1);
	}
	return 0;
}