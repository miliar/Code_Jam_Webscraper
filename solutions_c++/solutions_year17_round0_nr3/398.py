#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long long int lli;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef pair<ii,string> iis;
typedef vector<iii> viii;
typedef vector<int> vi;
priority_queue<iii> pq;
int main()
{
	//freopen("C-small-2.in","r",stdin);
	//freopen("C-small-2.out","w",stdout);
	ios_base::sync_with_stdio(false);
	int T;
    int tc;
    cin >> tc;
    int n,k;
    iii u;
    for(int t = 1; t<=tc; t++)
	{
       cin >> n >> k;
       u.second.first = -1;
       u.second.second = (n + 1);
       u.first = (u.second.second - (-u.second.first));
       pq.push(u);
       iii v;
       int mid;
       iii last1;
       iii last2;
       for( int i = 1; i<= k; i++)
	   {
        u = pq.top();
		pq.pop();
        mid = (u.second.second + (-u.second.first) - 1 ) /2;
        v.second.second = mid;
        v.second.first = u.second.first;
        v.first = ( v.second.second - (-v.second.first));
        last1 = v;
        pq.push(v);
        v.second.first = -(mid +1);
        v.second.second = u.second.second;
        v.first = (v.second.second - (-v.second.first));
        pq.push(v);
        last2 = v;

       }
       int value_1 = last1.second.second - (-last1.second.first);
       pq.pop();
       int value_2 = last2.second.second - (-last2.second.first);
       printf("Case #%d: %d %d\n",t,max(value_1,value_2),min(value_1,value_2));
       while(!pq.empty()) pq.pop();
    }
    return 0;
    
}