#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int T;
ll k,n;
ll t;
ll x,y;
struct Node
{
	ll l,r,pos;
	Node(ll l,ll r):l(l),r(r){}
	Node(){}
	friend bool operator< ( Node t1,Node t2)
	{
		return (t2.r-t2.l) > (t1.r-t1.l);
	}
};

void solve(ll l ,ll r)
{
	Node t;
	priority_queue<Node> q;
	q.push(Node(l,r));
	int m;
	int cnt=0;
	while(!q.empty()){
		t=q.top();
		q.pop();
		m=(t.l+t.r)/2;
		if(t.l > t.r)
			continue;
		cnt++;
		if(cnt==k){
			//cout << t.l <<" " << t.r <<" " << m<<endl;
			x=max(m-t.l,t.r-m);
			y=min(m-t.l,t.r-m);
			return;
		}
		if(m-1-t.l>t.r-m-1)
		{
			q.push(Node(t.l,m-1));
			q.push(Node(m+1,t.r));
		}
		else
		{
			q.push(Node(m+1,t.r));
			q.push(Node(t.l,m-1));
		}
	}
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C.out","w",stdout);
#endif
	cin >> T;
	int kase=1;
	while(T--){
		cin >> n >> k;
		x=y=0;
		t=0;
		solve(1,n);
		//cout << x <<" " << y << endl;
		/*
		for(int i=0;i<n+2;i++)
			cout <<pos[i];
		cout << endl;
		*/
		printf("Case #%d: %lld %lld\n",kase++,x,y);
	}

	return 0;
}
