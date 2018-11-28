#include<bits/stdc++.h>

#define li long int
#define lli long long int
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define sli(n) scanf("%ld",&n)
#define slli(n) scanf("%lld",&n)
#define sf(n) scanf("%f",&n)
#define sstr(s) scanf("%s",s)

const int mod = 10000009;
const lli MOD = 1000000007;

using namespace std;

bool check(string &s){
	for(int i=0;i+1<s.length();i++)
		if(s[i]>s[i+1])
			return false;
	
	return true;
}

int main()
{
	std::ios_base::sync_with_stdio(false);
	freopen("B-large.in","r",stdin);
	freopen("B-large-output2.txt","w",stdout);
	
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		string strN;
		cin>>strN;
		cout<<"Case #"<<t<<": ";
		
		int L = strN.length();
		if(L==1){
			cout<<strN<<"\n";
			continue;
		}
		
		while(true){
			string ans="";
			for(int i=0;i+1<L;i++){
				if(strN[i]>strN[i+1]){
					ans += strN[i]-1;
					string sub(L-i-1,'9');
					ans += sub;
					break;
				}
				else{
					ans += strN[i];
					if(i==L-2)
						ans += strN[i+1];
				}
			}

			strN=ans;
			if(check(ans))
				break;	
		}
		
		if(strN[0]=='0')
			cout<<strN.substr(1);
		else
			cout<<strN;
		cout<<"\n";
	}

	return 0;
}

