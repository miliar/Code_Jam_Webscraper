#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define N 1000005
#define hg ios_base::sync_with_stdio(0);cin.tie(0)
#define ff first
#define ss second
#define gcd __gcd
#define inf (1<<30)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define all(xx) xx.begin(),xx.end()
#define bitcit __builtin_popcount
#define mset(x,y) memset(x,y,sizeof(x))
#define INF 1e18
#define PI acos(-1)
#define ll long long
#define endl "\n"

map<ll ,ll> freq;
set<ll> st;
set<ll>::iterator it;
int main() {
	hg;
	//freopen("input.in","r",stdin);
	//freopen("output.out","w",stdout);
    int t,tt=0;
    ll n,m,mm,f,i;
    ll num;
    cin>>t;
    while(t--)
    {
    	tt++;
    	cin>>n>>m;
    	freq.clear();
    	f=0;
    	st.clear();
    	num=1;
    	cout<<"Case #"<<tt<<": ";
    	if(n&1){
    		freq[n/2LL]=2;
    		st.insert(n/2LL);
    		if(m<=num){
    			cout<<n/2LL<<" "<<n/2LL<<"\n";
    			continue;
    		}
    	}
    	else
    	{
    		freq[n/2LL]=1;
    		freq[(n/2LL)-1]=1;
    		st.insert(n/2LL);
    		st.insert((n/2LL)-1);
    		if(m<=num){
    			cout<<n/2LL<<" "<<(n/2LL)-1<<"\n";
    			continue;
    		}
    	}
    	ll n1,times;
    	while(!f)
    	{
    		it=st.end();
    		it--;
    		n1=*it;
    		st.erase(*it);
    		times=freq[n1];
    		if(n1&1)
    		{
    			freq[n1/2LL]+=2LL*times;
    			st.insert(n1/2LL);
    			num+=times;
    			if(num>=m)
    			{
    				cout<<n1/2LL<<" "<<n1/2LL<<"\n";
    				f=1;
    			}
    		}
    		else
    		{
    			if(n1==1){
    				num+=times;
    				if(num>=m)
    				{
    					f=1;
    					cout<<n1/2LL<<" "<<(n1/2LL)<<"\n";
    				}
    			}
    		  else
    		  {
    			freq[n1/2]+=1LL*times;
    			freq[(n1/2)-1]+=1LL*times;
    			st.insert(n1/2LL);
    			st.insert((n1/2LL)-1);
    			num+=times;
    			if(num>=m)
    			{
    				f=1;
    				cout<<n1/2LL<<" "<<(n1/2LL)-1<<"\n";
    			}
    		  }
    		}
    	}
	}
    return 0;
}