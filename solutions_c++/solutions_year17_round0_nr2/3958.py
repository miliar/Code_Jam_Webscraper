#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#define pb push_back
#define fi first
#define se second
#define sz size
#define fod find_by_order
#define fastio ios::base_sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);
#define ofk order_of_key
#define val(x) cout << "Value dari "<< #x << " adalah " << x  << "\n"
#define tr tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update>
typedef long long ll;
using namespace __gnu_pbds;
using namespace std;
void readf(string x){
	freopen((x+".in").c_str(),"r",stdin);
	freopen((x+".out").c_str(),"w",stdout);
}

int read()
{
	bool min = 0;
	int  result = 0;
	char ch;
	ch = getchar();
	while(1)
	{
		if(ch == '-') break;
		if(ch >='0' && ch <= '9') break;
		ch = getchar();
	}
	if(ch == '-') min = 1;else result = ch-'0';
	while(1)
	{
		ch =getchar();
		if(ch< '0' || ch>'9') break;
		result = result * 10 + (ch-'0');
	}
	if(min) return -result;
	return result;
}

int main(){
//	readf("B");	
	ll T,cs = 0;
	cin >> T;
	while(T--){
		ll N;
		cin >> N;cout << "Case #" << ++cs << ": ";
		if(N < 10) {
			cout << N << "\n";
			continue;
		}
		ll temp = N;
		vector<ll> x;
		ll mini = 10;
		ll jum = 0;
		while(temp != 0){
			x.pb(temp % 10);
			mini = min(mini,temp%10);
			temp = temp/10;
			jum++;
		}
		bool masalah[25];
		memset(masalah,0,sizeof masalah);
		reverse(x.begin(),x.end());
		for(ll i=1;i<x.size();i++){
			if(x[i] < x[i-1]){
				for(ll j=i-1;j>=0;j--){
					if(j == 0 || x[j-1] != x[j]){
						masalah[j] = 1;
					//	cout << j << "asd\n";
						break;
					}
				}
			//	masalah[i-1] = 1;
				break;
			}
		}
		bool ok = 0;
		for(ll i=0;i<x.size();i++){
		//	cout<< i << " " << masalah[i]<< " " << x[i] << "aw\n";
			if(masalah[i]){
				ok = masalah[i];
				if(i == 0 && x[i] - 1 == 0) continue;
				cout << x[i]-1 ;
			}
			else if(ok ){
				cout << 9 ;
			}
			else cout << x[i];
		}
		cout << "\n";
	}
}

