/*input
5
9999999999999999 1279999999999
5 2
6 2
1000 1000
1000 1
*/
#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define F(i,a,b) for(ll i = a; i <= b; i++)
#define RF(i,a,b) for(ll i = a; i >= b; i--)
#define pii pair<ll,ll>
#define PI 3.14159265358979323846264338327950288
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define P(x) printf("%d\n",x)
#define all(v) v.begin(),v.end()
bool arr[1005];
ll n,k;
void brute()
{
	memset(arr,0,sizeof(arr));
	ll aa,bb,ans;
	arr[0] = arr[n+1] = 1;
	while(k--) // place k soldiers one by one
	{
		//debug(k);
		bool onefound = 0;
		ll ii,jj;
		ll minoflr=-1,maxoflr=-1;
		F(i,0,n+1)
		{
			ll num,mid,l,r,id;
			if(arr[i]==1 && onefound==0)
			{
				onefound = 1;
				ii = i;
				continue;
			}
			if(arr[i]==1)
			{
				jj = i;
				//cout<<ii<<" "<<jj<<endl;
				{
					num = (jj-ii-1);
					mid = (num+1)/2;
					id = ii + mid;
					l = id-ii;
					r = jj-id;
					//debug(id);
					if(min(l,r) > minoflr)
					{
						minoflr = min(l,r);
						maxoflr = max(l,r);
						ans = id;
					}
					else if(min(l,r) == minoflr)
					{
						if(max(l,r) > maxoflr)
						{
							maxoflr = max(l,r);
							ans = id;
						}	
					}
				}
				ii = i;
			}
		}
		//debug(ans);
		arr[ans] = 1;
	}
	ll ls=0,rs=0;
	F(i,ans+1,n+1)
	{
		if(arr[i]==1)
			break;
		rs++;
	}
	RF(i,ans-1,0)
	{
		if(arr[i]==1)
			break;
		ls++;
	}
	aa = max(ls,rs);
	bb = min(ls,rs);
	cout<<aa<<" "<<bb<<endl;
}
priority_queue < ll , vector<ll> > pq;
void brute_2()
{
	while(!pq.empty())
		pq.pop();
	ll curl = (n-1)/2;
	ll curr = n/2;
	pq.push(curl);
	pq.push(curr);
	k--;
	while(k > 0)
	{
		ll val = pq.top();
		pq.pop();
		if(val == 1)
		{
			curl = 0;
			curr = 0;
			break;
		}
		curl = (val-1)/2;
		curr = (val)/2;
		pq.push(curl);
		pq.push(curr);
		k--;
	}
	//printf("%d %d",curl,curr);
	cout<<curr<<" "<<curl<<endl;
}
map <ll,ll> mymap;
void large()
{
	mymap.clear();
	mymap[n]++;
	ll curl,curr;
	while(k>0)
	{
		map <ll,ll>::iterator it = mymap.end();
		it--;
		ll val = it->ff;
		ll cnt = it->ss;
		//debug(val);
		curl = (val-1)/2;
		curr = (val)/2;
		mymap[curl] += cnt;
		mymap[curr] += cnt;
		k -= cnt;
		mymap.erase(it);
	}
	cout<<curr<<" "<<curl<<endl;
}
int main() 
{
	std::ios::sync_with_stdio(false);
	freopen("is1.txt","r",stdin);
	freopen("os1.txt","w",stdout);
	ll tc=1;
	ll t;
	cin>>t;
	while(t--)
	{
		cout<<"Case #"<<tc++<<": ";
		cin>>n>>k;
		//brute(); // for small 1
		//brute_2(); // for small 2
		large();
	}
	return 0;
}