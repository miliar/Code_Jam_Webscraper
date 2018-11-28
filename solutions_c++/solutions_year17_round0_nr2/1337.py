//chiragjn
#include <iostream>
#include <vector>
#include <sstream>
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define gibe_de_fast_io_b0ss ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;
const ll mod = 1e9 + 7;
const ll INF = 0x7FFFFFFFFFFFFFFF/2;
vector<ll> arr;
int main(){
    // gibe_de_fast_io_b0ss;
    for(ll i=1;i<=9;i++){
    	ll k = i;
    	while(k <= 1e18){
    		arr.pb(k);
    		k = k * 10 + i;
    	}
    }
    arr.pb(1111111111111111111);
    sort(arr.begin(), arr.end());
    int t;
    ll n, l, r;
    cin>>t;
    for(int T=1;T<=t;T++){
    	cin>>n;
    	for(int i=arr.size() - 2;i>=0;i--){
    		if(arr[i]<=n && n<=arr[i+1]){
    			l = arr[i];
    			r = arr[i+1];
    			break;
    		}
    	}
    	r = min(r, n);
    	stringstream ls,rs;
    	ls<<l;
    	rs<<r;
    	string lstr = ls.str();
    	string rstr = rs.str();
    	string ans = rstr;
    	for(int i=1;i<rstr.size();i++){
    		ans[i] = max(ans[i - 1], rstr[i]);
    		stringstream tmp1, tmp2;
    		ll ltmp1, ltmp2;
    		tmp1<<rstr.substr(0, i + 1);
    		tmp2<<ans.substr(0, i + 1);
    		tmp1>>ltmp1;
    		tmp2>>ltmp2;
    		if(ltmp2 > ltmp1){
    			char kek = ans[i - 1];
    			int j = i - 1;
    			while(j >=0 && ans[j] == kek) j--;
    			j++;
    			ans[j]--;
    			j++;
    			for(;j<rstr.size();j++) ans[j]='9';
    			break;
    		}
    	}
    	ll a;
    	stringstream anss;
    	anss<<ans;
    	anss>>a;
    	cout<<"Case #"<<T<<": "<<a<<"\n";
    }
    return 0;
}