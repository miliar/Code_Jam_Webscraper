/*
	Author: Hamza Hasbi
	Copyrights: "h.hamza" ==> "www.hamzahasbi.me"
	Date: 08/04/2017 00:06:57
*/
#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define ull unsigned long long
#define uld unsigned long double
#define ui unsigned int
#define ud unsigned double
#define uf unsigned float
#define pi 2*acos(0.0)
#define module cin.ignore()
#define rep(i,l,r) for(auto i=l;i<=r;i++)
#define range(x,y) for(auto x:y)
//inline lcm(int a,int b) {return a*b/__gcd(a,b);}
//inline gcd(ll a,ll b) {return 1LL*b == 0 ? a : gcd(1LL*b, a*1LL % b*1LL);}
using namespace std;

main()
{

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	freopen("outputA.out","w",stdout);
	freopen("A-large.in","r",stdin);
	int it=1;
	int t;
	cin>>t;
	while(t--){
		string s;
		cin>>s;
		int n;
		cin>>n;
		int ans=0,ct=0;
		bool flag=true;
			for(int i=0;i<s.size();i++){
				int curr=0;
				int j=i;
				if(s[i]=='-'){
					for(;curr<n && j<s.size();j++,curr++){
						s[j]= s[j]=='-'?'+':'-';
					}
					if(curr<n) {
						flag=false;
						break;
					}
					ans++;
				}
			}
			//cout<<s<<endl;
			for(int i=0;i<s.size();i++){
				flag&=s[i]=='+';
			}
	
		//cout<<ans<<endl;
		if(flag) cout<<"Case "<<"#"<<it++<<": "<<ans<<endl;
		else cout<<"Case "<<"#"<<it++<<": "<<"IMPOSSIBLE"<<endl;
	}
	
	return 0;
}

