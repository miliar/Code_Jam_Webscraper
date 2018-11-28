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

int main()
{
	std::ios_base::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("A-large-output.txt","w",stdout);
	
	
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		string s;
		int k;
		cin>>s>>k;
		
		int L = s.length();
		int i=0,cnt=0;
		while(i+k<=L){
			if(s[i]=='-'){
				cnt++;
				for(int j=1,z=i;j<=k;j++,z++){
					if(s[z]=='-')
						s[z]='+';
					else if(s[z]=='+')
						s[z]='-';
				}
			}
			i++;
		}
		
		bool flag=true;
		while(i<L){
			if(s[i]=='-'){
				cout<<"Case #"<<t<<": IMPOSSIBLE\n";
				flag=false;
				break;
			}
			i++;
		}
		
		if(flag)
			cout<<"Case #"<<t<<": "<<cnt<<"\n";
	}

	return 0;
}

