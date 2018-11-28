#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;

struct cmp_lol{
	bool operator()(ii const &a, ii const &b){
		int mid1 = (a.first + a.second)/2, mid2 = (b.first + b.second)/2;
		int l1 = mid1 - a.first, r1 = a.second - mid1, l2 = mid2 - b.first, r2 = b.second - mid2;
		if(min(l1, r1) > min(l2, r2))	return true;
		else if(min(l1, r1) < min(l2, r2))	return false;
		else{
			if(max(l1, r1) > max(l2, r2))	return true;
			else if(max(l1, r1) < max(l2, r2))	return false;
			else return mid1 < mid2;
		}
	}
};

set<ii, cmp_lol> S;

void solve(){
	S.clear();

	int n, k;
	cin>>n>>k;

	ii tmp;
	int mid, L, R;
	S.insert(make_pair(0, n + 1));

	while(k--){

		tmp = *S.begin();

		S.erase(*S.begin());

		mid = (tmp.first + tmp.second)/2;

		if(tmp.second != mid + 1)
			S.insert(make_pair(mid, tmp.second));

		if(tmp.first + 1 != mid)
			S.insert(make_pair(tmp.first, mid));
	}

	L = mid - tmp.first, R = tmp.second - mid;
	cout<<max(L, R) - 1<<" "<<min(L, R) - 1<<endl;
}

int main(){

	int t;
	cin>>t;
	for(int big = 1; big <= t; big++){
		cout<<"Case #"<<big<<": ";
		solve();
	}
}