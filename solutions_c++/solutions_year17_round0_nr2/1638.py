#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define pb push_back
#define sz size()
#define pii pair<int,int>
#define mp make_pair
#define ff first
#define ss second
#define all(v) (v).begin(),(v).end()

std::vector< ll > v;

void call(int i,ll w,int now)
{
	if(i==18){

		v.pb(w);
		return;
	}
	v.pb(w);
	for(int j = now;j <= 9;j++){

		call(i+1,(w*10)+j,j);
	}
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	//std::ios_base::sync_with_stdio(false);

	call(0,0,1);

	sort(all(v));

	int t;
	ll x;

	cin >> t;

	for(int cases = 1;cases <= t;cases++){

		cin >> x;

		cout << "Case "<< "#" << cases << ": "<< * (--upper_bound(all(v),x)) << endl;
	}
	return 0;
}