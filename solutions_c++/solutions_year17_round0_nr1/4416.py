#include<bits/stdc++.h>
using namespace std;

typedef long long ll;


int success(){
    vector<ll> ans;
    ll t;
    cin >> t;
    for(ll k = 1;k <= t;k++){
        ll n;
        cin >> n;
        while(n){
            ans.push_back(n%10);
            n /= 10;
        }
        reverse(ans.begin(),ans.end());
        for(ll i = ans.size() - 1;i >= 1;i--){
            if(ans[i] < ans[i - 1]){
                for(ll j = i;j< ans.size();j++)
                    ans[j] = 9;
                ans[i - 1]--;
            }
        }
        ll i = 0;
        cout << "Case #" << k << ": ";
        while(i < ans.size() && ans[i] == 0)
            i++;
        for(;i < ans.size();i++)
            cout << ans[i];
        cout << "\n";
        ans.clear();
    }
    return 0;
}


int check(string s)
{
	for(ll i=0;i<s.size();i++)
	{
		if(s[i]=='-')
		return 0;
	}
	return 1;
}
int main()
{

   freopen("in2.txt", "r", stdin);
   freopen("out.txt", "w", stdout);

	ll t;
	cin>>t;

	for(ll tc=1;tc<=t;tc++)
	{
		ll K;
		string s;
		cin>>s>>K;

		ll l=s.size();
		ll ans=0;
		for(ll i=0;i<l;i++)
		{
			if(s[i]=='-' && i+K<=l)
			{
				for(ll j=i; j<i+K ; j++)
				{
					if(s[j]=='-')
					s[j]='+';
					else
					s[j]='-';
				}
				ans++;
			}
		}

		if(check(s)==1)
		{
			cout<<"Case #"<<tc<<": "<<ans<<"\n";
		}
		else
		{
			cout<<"Case #"<<tc<<": IMPOSSIBLE"<<"\n";
		}

	}

}
