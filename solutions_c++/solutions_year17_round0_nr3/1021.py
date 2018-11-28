#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
struct Node
{
	ll v,cnt;
	Node(){}
	Node(ll _v , ll _cnt):v(_v),cnt(_cnt) {}
	bool operator < (const Node & r) const
	{
		return v<r.v||(v==r.v&&cnt<r.cnt);
	}
};
void ioinit()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
}
int main()
{
	ioinit();
	int T,kase=1;
	cin>>T;
	while(T--)
	{
		ll n,k;
		cin>>n>>k;
		priority_queue<Node> q;
		map<ll,ll> cnt;
		q.push(Node(n,1));
		bool flag=true;
		printf("Case #%d: ",kase++);
		while(k>0)
		{
			if(q.size()==1)
			{
				Node t=q.top();q.pop();
				ll cnt=t.cnt;
				ll v=t.v-1;
				if(v&1)
				{
					q.push(Node(v/2,cnt));
					q.push(Node(v-v/2,cnt));
				}
				else q.push(Node(v/2,cnt*2));
				if(k-cnt<=0) cout << max(v/2,v-v/2) << " " << min(v/2,v-v/2) << endl,flag=false;
				k-=cnt;
			}
			else
			{
				Node l=q.top();q.pop();
				Node r=q.top();q.pop();
				ll vl=l.v-1,vr=r.v-1;
				ll cl=l.cnt,cr=r.cnt;
				set<ll> s;
				s.insert(vl/2); s.insert(vl-vl/2);
				s.insert(vr/2); s.insert(vr-vr/2);
				ll v1=*s.rbegin(),v2=*s.begin();
				//cout << cl << " " << cr << " " << k << endl;
				map<ll,ll> cnt;
				cnt[vl/2]+=cl;
				cnt[vl-vl/2]+=cl;
				cnt[vr/2]+=cr;
				cnt[vr-vr/2]+=cr;
				ll c1=cnt[v1],c2=cnt[v2];
				if(k-cl<=0)
				{
					if(vl&1) cout << v1 << " " << v2 << endl;
					else cout << v1 << " " << v1 << endl;
					flag=false;
				}
				else if(k-cl-cr<=0)
				{
					if(vr&1) cout << v1 << " " << v2 << endl;
					else cout << v2 << " " << v2 << endl;
					flag=false;
				}
				q.push(Node(v1,c1));
				q.push(Node(v2,c2));
				k-=cl+cr;
 			}
		}
		if(flag) cout << "0 0"<< endl;
	}
	return 0;
}
