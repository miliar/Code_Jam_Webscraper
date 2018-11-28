#include<bits/stdc++.h>
 
using namespace std;
#define go_baby_go ios::sync_with_stdio(false);cin.tie(NULL);
#define pb push_back
#define pp pop_back
#define f first
#define s second
#define ll long long
const int size=1e6+7;

int main()
{
	go_baby_go
	int t1,T;
	ll n,k,minm,maxm,i;
	pair<ll,ll> p,q,r,t;
	cin>>T;
	t1=T;
	while(T--)
	{
		cout<<"Case #"<<t1-T<<": ";
		cin>>n>>k;
		p=make_pair(0,0);
		q=make_pair(0,0);
		if(n&1)p=make_pair(n,1);
		else q=make_pair(n,1);
		i=1;
		while(1)
		{
			t=r=make_pair(0,0);
			//cerr<<p.f<<","<<p.s<<" "<<q.f<<","<<q.s<<endl;
			if(k<=i)
			{
				
				if(p.f>q.f)
				{
					if(k>p.s)
					{
						maxm=q.f;
						minm=maxm-1;
					}
					else
					minm=maxm=p.f;
				}
				else
				{
					if(k>q.s)
					{
						maxm=minm=p.f;
					}
					else
					minm=maxm=q.f,minm--;
				}
				break;
			}
			if((p.f/2)%2==0)
			{
				r.f=p.f/2;
				r.s=p.s*2;
			}
			else
			{
				t.f=p.f/2;
				t.s=p.s*2;
			}
			//if(p.f==31)cout<<t.s;
			if(q.f!=0)
			{
				if(q.f+1==p.f)
				{
					r.f=p.f/2;
					t.f=p.f/2-1;
					if((p.f/2)&1)swap(r.f,t.f);
				}
				else if(q.f==p.f+1)
				{
					r.f=q.f/2-1;
					t.f=q.f/2;
					if((q.f/2)%2==0)swap(r.f,t.f);
				}
				else
				{
					r.f=q.f/2;
					t.f=q.f/2-1;
					if((q.f/2)&1)swap(r.f,t.f);
				}
			r.s+=q.s;
			t.s+=q.s;
			}
			p=make_pair(t.f,t.s);
			q=make_pair(r.f,r.s);
			k-=i;i*=2;
		}	
		cout<<maxm/2<<" "<<minm/2<<endl;
	}
	return 0;
}