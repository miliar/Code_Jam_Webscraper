/*input
100
132
1000
7
130
240
974
387
844
929
694
801
598
522
760
378
923
382
461
685
447
831
206
138
999
333
1
64
888
842
88
174
608
189
113
257
905
459
664
885
798
527
702
472
480
389
645
306
788
839
840
693
471
63
253
2
158
971
268
319
267
752
178
231
353
782
225
511
280
56
687
410
909
813
731
131
536
963
620
658
356
955
920
54
273
952
655
717
932
943
303
210
989
835
571
260
957
634
991
718
723

*/
#include <iostream>
#include <bits/stdc++.h>
#include <queue>
#include <vector>
#include <cmath>
#include <cstring>
#include <climits>
#include <set>
#include <algorithm>
#define inf LONG_MAX
#define MAX 10001000
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define RESET(a,b) memset(a, b, sizeof a)
#define boost ios_base::sync_with_stdio(false);cin.tie(0) 
#define PII pair<ll,ll>
typedef long long int ll;
using namespace std;
ll T;
ll M=1e9+7;
ll total=0;
vector<ll> ans;
ll a[MAX+5];
void pre()
{
	queue<ll> q;
	for(ll i=1;i<=9;i++)
	{
		a[++total]=i;
		q.push(i);
	}

	while(!q.empty())
	{
		ll x=q.front();
		q.pop();
		
		if(x>1e18)
			break;

		ll last=x%10;
		for(ll j=1;j<=9;j++)
		{
			if(j>=last)
			{
				q.push(x*10+j);
				a[++total]=x*10+j;
			}
		}

	}

}

ll Search(ll x)
{
	ll l=1;
	ll r=total;
	ll d;
	while(l<=r)
	{
		ll mid=(l+r)/2;
		if(a[mid]<=x)
		{
			d=a[mid];
			l=mid+1;
		}

		else
			r=mid-1;

	}

	return d;
}


int main() {
	
	boost;	
	pre();
	total--;
	cin>>T;
	ll k=0;
	while(T--)
	{
		ll x;
		cin>>x;
		k++;
		cout<<"Case #"<<k<<": "<<Search(x)<<endl;
	}
}