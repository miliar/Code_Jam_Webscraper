#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

typedef long long int lli;
typedef pair<lli, lli> pllilli;

pllilli f(int k, int n){
	if (k == 1){
		return pllilli((n-1)/2, n/2);
	}
	bool kPar = (k & 1) == 0;
	bool nPar = (n & 1) == 0;
	if (kPar && nPar){
		return f(k/2, n/2);
	}
	if (kPar && !nPar){
		return f(k/2, n/2);
	}
	if (!kPar & nPar){
		return f(k/2, (n-1)/2);
	}
	if (!kPar & !nPar){
		return f(k/2, n/2);
	}
}

int main(){ _
	int t;
	cin >> t;
	for (int q = 1; q <= t; q++){
		lli n, k;
		cin >> n >> k;
		pllilli ans = f(k, n);
        cout << "Case #" << q << ": " << max(ans.first, ans.second) << " " << min(ans.first, ans.second) << endl;
	}
	return 0;
}
