#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define sz(a) (int)(a.size())
#define all(c) (c).begin(),(c).end()
#define F first
#define S second
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define MOD 1000000007
#define endl '\n'
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)
typedef long long int ll;
ll powmod(ll a,ll b)
{
    if(b==0)return 1;
    ll x=powmod(a,b/2);
    ll y=(x*x)%MOD;
    if(b%2)
    return (a*y)%MOD;
    return y%MOD;
}

int main() {
	freopen ("inpa.txt","r",stdin);
    freopen ("aao.txt","w",stdout);
	int t,T=1;
	cin>>t;
	while(T<=t){
		long long n,m,i,j,k,a[305][305],h[305]={0};
		multiset<long long>st[305];
		cin>>n>>m;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				cin>>k;
				st[i].insert(k);
			}
			
		}

		long long ans=0;
		for(i=0;i<n;i++){
			
			long long mn=1000009LL,mi=-1;
			for(j=0;j<=i;j++){
				if(st[j].size()>0){
				if(*(st[j].begin())<mn){
					mn=*(st[j].begin());
					mi=j;
				
				}
				}
			}
			//
			h[mi]+=1;
			ans+=mn;
		//	cout<<mi<<" "<<mn<<endl;
			st[mi].erase(st[mi].begin());
		//	cout<<st[mi].size()<<endl;
			
		}	;
		for(i=0;i<n;i++){
			ans+=h[i]*h[i];
		}
		cout<<"Case #"<<T++<<": "<<ans<<endl;
		
	}
	
	
	// your code goes here
	return 0;
}