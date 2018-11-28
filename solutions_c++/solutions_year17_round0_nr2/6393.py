#include<bits/stdc++.h>
using namespace std;
/*author : jatin_jt_narula
           B.tech CSE  
           MNNIT-Allahabad */
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#define sf(x) scanf("%lf",&x)
#define sl(x) scanf("%lld",&x)
#define pl(x) printf("%lld",x)
#define pln(x) printf("%lld\n",x)
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#define wh(t) while(t--)
#define ms(a , value) memset(a , value , sizeof(a))
#define f(c,itr) for(itr=(c).begin();itr!=(c).end();itr++)
#define M 1000000007
#define sc scanf
#define pr printf
#define pi(x) printf("%d",x)
#define pin(x) printf("%d\n",x)
#define ss(x) scanf("%s",x)
#define ps(x) printf("%s",x)
#define nl() printf("\n")
#define psn(x) printf("%s\n",x)
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define si2(x,y) scanf("%d%d",&x,&y)
#define each(v) v.begin(),v.end()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define N 507
const double PI=3.1415926535897;
typedef long long int ll;
int main()
{
	int test;
	string res,ans;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		string str;
		cin>>str;
		int len=str.length();
		if(len == 1)
		{
			cout<<"Case #"<<t<<": "<<str<<"\n";
			continue;
		}
		int pos=0;
		res.clear();
		ans.clear();
		int flag=0;
		for(int i=1;i<len;i++)
		{
			int j=i-1;
			if(str[j] == str[i])
				continue;
			else if(str[j]<str[i])
			{
				pos=i;
				continue;
			}
			else
			{
				for(int i=0;i<=pos-1;i++)
					res.pb(str[i]);
					res.pb((char)(str[pos]-1));
				for(int i=pos+1;i<len;i++)
					res.pb('9');
				pos=0;
				len=res.length();
				for(int i=0;i<len;i++)
					{
						if(res[i]!='0')
						{
							pos=i;
							break;
						}
					}

				for(int i=pos;i<len;i++)
					ans.pb(res[i]);

				flag = 1;
				break;
			}
		}
		if(flag == 1)
		cout<<"Case #"<<t<<": "<<ans<<"\n";
		else
			cout<<"Case #"<<t<<": "<<str<<"\n";
	}
	return 0;
}