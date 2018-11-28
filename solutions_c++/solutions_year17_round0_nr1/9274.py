#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <climits>
#include <bitset>
#include <cmath>
#include <cstring>
#include <assert.h>
using namespace std;
#define all(M) (M).begin(), (M).end()
#define vi vector<int>
#define vl vector<ll>
#define sort(v) sort(all(v))
#define fo(i,m,n) for(auto i = m ; i < n ; i++)
#define rep(i,n) fo(i,0,n)
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define pqueue priority_queue<pll,vector<pll>, greater<pll>>
#define sz(s) s.size()
#define trace(a) {for(auto i:a) cout << i << ' '; cout << '\n';}
//#define set(a) memset(a,0,sizeof(a))
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define pl(n) printf("%lld\n",n)
#define smi(n,m) scanf("%d%d",&n,&m)
#define pmi(n,m) printf("%d %d\n",n,m)
#define sml(n,m) scanf("%lld%lld",&n,&m)
#define pml(n,m) printf("%lld %lld\n",n,m)
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int main()
{
	int t;
	si(t);
	fo(tt,1,t+1)
	{
		string s; int k;
		cin >> s; si(k);
		int n = sz(s),cnt=0;
		bool f = true;
		rep(i,n)
		{
			if(s[i] == '-')
			{
				if(i+k-1 >= n)
				{
					f = false;
					break;
				}
				fo(j,i,i+k)
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				cnt++;
			}
		}
		cout << "Case #" << tt << ": ";
		if(!f)
			puts("IMPOSSIBLE");
		else pi(cnt);
	}
	return 0;
}
