#include<bits/stdc++.h>
#define pii pair<int,int>
#define Get(a,b) make_pair(a,b)
using namespace std;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t,kase=1,N,K;
    cin >> t;
    while(t--)
    {
    	cin >> N >> K;
    	priority_queue<pii> q;
    	vector<int> v;
    	set<int> s;
    	N+=2;
    	s.insert(1);
    	s.insert(N);
    	q.push(Get(0,0));
    	v.push_back((1+N)/2);
    	int A,B;
    	for(int i=1;i<=K;i++)
    	{
    		int now = v[q.top().second];
    		q.pop();
    		auto it = s.upper_bound(now);
    		int r = *it;
    		int l = *(--it);
    		if(i==K)
    		{
    			A = max(r-now,now-l);
    			B = min(r-now,now-l);
			}
    		s.insert(now);
    		int L = (l+now)/2;
    		int R = (now+r)/2;
			if(now-l < r-now)
			{
				if(r-now>=2)
				{
				    q.push(Get(r-now,v.size()));
					v.push_back(R);
				}
				if(now-l>=2)
				{
				    q.push(Get(now-l,v.size()));
					v.push_back(L);
				}
			}
			else
			{
				if(now-l>=2)
				{
				    q.push(Get(now-l,v.size()));
					v.push_back(L);
				}
				if(r-now>=2)
				{
				    q.push(Get(r-now,v.size()));
					v.push_back(R);
				}
			}
		}
		cout << "Case #" << kase++ << ": " << A-1 << " " << B-1 << endl;
	}
    return 0;
}

