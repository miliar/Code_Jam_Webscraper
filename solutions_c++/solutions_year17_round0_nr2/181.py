#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n;

ll makenum(string N,int i) {
	string r=N.substr(0,i);
	if (i<N.size()) r.push_back(N[i]-1);
	if (N.size()-r.size()) r.append(N.size()-r.size(),'9');
	bool succ=1;
	for (int i=0;i<r.size();i++) {
		if (r[i]<'0') succ=0;
		if (i+1<r.size() && r[i]>r[i+1]) succ=0;
	}

	//cerr << r << endl;
	if (succ) return stoll(r);
	return -1;
}

int main() {
	int T;
	string N;
	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> N;
		n=stoll(N);
		ll B=-1;
		for (int i=0;i<=N.size();i++) {
			ll cur=makenum(N,i);
			if (cur<=n) B=max(B,cur);
		}
		printf("Case #%d: %lld\n",cas,B);
	}
}
