#include<bits/stdc++.h>
#define nl ('\n')
#define pb push_back
#define MOD 1000000007
#define MAX 100000
typedef long long ll;
using namespace std;
//ll expo(ll x,ll y,ll M){ if(y==0) return 1; ll z = expo(x,y/2,M); if(y&1) return (1ll * ((1ll * x * z)%M) * z)%M; else return (1ll * z * z)%M;}
//ll gcd(ll x,ll y){ if(x==0) return y; return gcd(y%x,x); }
int main()
{
	//ios::sync_with_stdio(0);cin.tie(0);
	int t,r,c;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>r>>c;string str[30];char ch;int em[30]={};
		//getchar();
		for(int j=1;j<=r;j++){
			cin>>str[j];
			//cout<<"M : "<<str[j]<<nl;
		}
		//getchar();
		//cout<<"Hello\n";
		for(int j=1;j<=r;j++)
		{
			int fl = 0;int lun = 0;
			for(int k=0;k<str[j].length();k++)
			{
				if(str[j][k] != '?')
				{
					//cout<<"Enter\n";
					fl = 1;ch = str[j][k];int x;string tp;tp.pb(ch);
					for(x = lun;x<str[j].length();x++){
						if(str[j][x] == '?' || str[j][x] == ch)
							str[j].replace(x,1,tp);
						else break;
					}
					lun = x;
					k = x-1;
				}
			}
			if(!fl) em[j] = 1;
		}
		int lunf = 1;
		for(int j=1;j<=r;j++){
			if(!em[j]){
				int jj;
				for(jj = lunf;jj<=r;jj++){
					if(jj==j || em[jj]) str[jj] = str[j];
					else break;
				}
				lunf = jj;
				j = jj-1;
			}
		}
		cout << "Case #"<<i<<":"<<nl;
		for(int j=1;j<=r;j++)
			cout<<str[j]<<nl;
	}
	return 0;
}
