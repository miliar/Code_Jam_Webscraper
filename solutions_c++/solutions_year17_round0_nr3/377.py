
// In the name of God
#include <bits/stdc++.h>

using namespace std;
#define Size(x) ((int)(x).size())
#define pb push_back
typedef long long ll;
typedef long double ld;
typedef pair<int,int>pii;
const int INF = 1e9 + 10;

void func(ll cnt1,ll cnt2,ll val,ll k)
{
	if(k <= cnt2){
		cout << val/2 << ' ' << (val-1)/2 << '\n';
		return;
	}
	if(k <= cnt1 + cnt2){
		cout << (val-1)/2 << ' ' << (val-2)/2 << '\n';
		return;
	}
	ll tmp2 = val/2 , tmp1 = (val-2)/2;
	ll C1 = cnt1 , C2 = cnt2;
	if((val-1)/2 == tmp2) C2 += cnt2 + cnt1;
	else C1 += cnt2 + cnt1;
	
	func(C1 , C2 , val/2 , k - cnt1 - cnt2);
}

int main()
{
	ios_base :: sync_with_stdio(false) ,cin.tie(0) , cout.tie(0);
	int T,cnt = 0;cin>>T;
	while(T--){
		ll tmp , num; cin >> tmp >> num;
		++cnt;
		cout << "Case #" << cnt << ": ";
		func(0 , 1 , tmp , num);
	}
	return 0;
}

