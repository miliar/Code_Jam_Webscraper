#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define pb push_back
#define ff first
#define ss second
using namespace std;

ll tc,num,arr[50],ans[50];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(ll t=1;t<=tc;t++){
		cin>>num;
		ll temp = num,cnt=0;
		while(temp){
			arr[cnt] = temp%10;
			temp = temp/10;
			cnt++;
		}
		ll mx = 0;
		ll k;
		for(k=cnt-1;k>=0;k--){
			ll i = mx;
			for(;i<=9;i++){
				bool flag = 1;
				for(ll j=k;j>=0;j--){
					if(i > arr[j]){
						flag = 0;
						break;
					}
					if(i < arr[j])
						break;
				}
				if(flag == 0)
					break;
			}
			i--;
			mx = max(mx,i);
			ans[k] = i;
			if(ans[k] < arr[k])
				break;
		}
		k--;
		for(;k>=0;k--)
			ans[k] = 9;
		cout<<"Case #"<<t<<": ";
		ll i=cnt-1;
		if(ans[i] == 0)
			i--;
		for(;i>=0;i--)
			cout<<ans[i];
		cout<<"\n";
	}
	
	return 0;
}

