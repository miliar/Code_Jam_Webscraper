#include <bits/stdc++.h>
#define  mp make_pair
#define pb push_back
#define pf push_front
#define pp pop_back
#define ppf pop_front
#define fi first
#define se second
#define maxn 1000005

typedef long long ll;
using namespace std;
#define pi pair<int,int>


/*struct node
{
	int i;

	bool friend operator < (node a,node b)
	{
		return w[a.i]>w[b.i];
	}
};
priority_queue<node>pq;*/


int main()
{
	ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);

	int q;
	cin>>q;
	int c =1;
	while(q--)
	{
		ll n;
		cin>>n;
		int a[20],b[20];
		ll k = n;
		int sz =0 ;
		while(k!=0)
		{
			b[sz++] = k%10;
			k = k/10;
		}
		for(int i=0;i<sz;i++)
		{
			a[i] = b[sz-i-1];
		}
		int idx = -1;
		for(int i=0;i<sz-1;i++)
		{
			if(a[i]>a[i+1])
			{
				idx = i;
				break;
			}
		}
		if(idx==-1)
		{
			cout<<"Case #"<<c<<":"<<" "<<n<<endl;
		}
		else
		{
			int idx1 = -1;
			for(int j = idx;j>0;j--)
			{
				if(a[j]!=a[j-1])
				{
					idx1 = j;
					break;
				}
			}
			if(idx1==-1)
			{
				if(a[0]==1)
				{
					cout<<"Case #"<<c<<":"<<" ";
					for(int i=0;i<sz-1;i++) cout<<"9";
					cout<<endl;
				}
				else
				{
					cout<<"Case #"<<c<<":"<<" "<<a[0]-1;
					for(int i=0;i<sz-1;i++) cout<<"9";
					cout<<endl;
				}
			}
			else
			{
				cout<<"Case #"<<c<<":"<<" ";

				for(int i=0;i<idx1;i++) cout<<a[i];
				cout<<a[idx1]-1;
				for(int i=idx1+1;i<sz;i++) cout<<"9";
				cout<<endl;
			}
		}
		c++;
	}
	return 0;
}
