
#include <bits/stdc++.h>
using namespace std;

#define wl(n) while(n--)
#define fr(i,a,b) for(i=a;i<b;i++)

#define bitcnt(x) __builtin_popcount(x)
#define mem(a,i) memset(a,i,sizeof(a))
typedef pair<int,int> ii;
#define mp make_pair
#define ll long long
#define MOD 1000000007
#define pb push_back
#define nl printf("\n")
#define INF (1LL<<52)
typedef pair<ll,pair<ll,ll> > iii;

bool debug = false;
int main()
{
	freopen("in2.txt","r",stdin);
	freopen("out2.txt","w",stdout);
	int T,t,i,j;
	ll n,k,K,move,mx,mn;
	cin>>T;
	fr(t,1,T+1)
	{

		k = 0;
		cin>>n>>K;

		priority_queue<iii , vector<iii> >Q;
		Q.push(mp(n,mp(0,n+1)));

		while(!Q.empty())
		{
			iii tmp = Q.top();
			Q.pop();
			ll len = tmp.first;
			ll l = tmp.second.first;
			ll r = tmp.second.second;

			if(debug)
			{
				cout<<"l : "<<l<<" r : "<<r<<" len :"<<len;nl;
			}
			if(len % 2)
			{   

				move = len/2 + 1;
				if(debug)
					cout<<"		placing at :"<<l+move<<endl;
				Q.push(mp( (len-1)/2 ,mp(l,l + move)));
				Q.push(mp( (len-1)/2 ,mp(l + move,r)));
				mn = mx = (len-1)/2;
			}
			else
			{
				move = len/2;
				if(debug)
					cout<<"		placing at :"<<l+move<<endl;
				Q.push(mp(len/2 - 1,mp(l,l + move)));
				Q.push(mp(len/2 , mp(l + move , r)));
				mn = len/2 - 1;
				mx = len/2;
			}
			k++;
			if(k == K)
			{
				cout<<"Case #"<<t<<": "<<mx<<" "<<mn<<endl;
				break;
			}
		}
	}
	return 0;
}

