/* 
	author: Bhrigu Gupta
		aka “bhrigudov”
*/

#include <bits/stdc++.h>

using namespace std;

#define fo(i,a,b) for(i=a;i<b;i++)
#define INF 1e11
#define MX 200002

typedef long long ll;

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false); 

	ll n, j, i, item2, t, k, item1, cur;

	cin>>t;
	fo(j,1,t+1)
	{	
		priority_queue<ll, vector<ll> > pq;
		cin>>n>>k;

		pq.push(n);
		while(k--) {
			cur = pq.top();
			pq.pop();

			cur--;
			item1 = cur/2;
			item2 = cur-item1;

			pq.push(item1);
			pq.push(item2);
		}

		cout<<"Case #"<<j<<": "<<max(item1, item2)<<" "<<min(item1, item2)<<"\n";
	}

	return 0;
}