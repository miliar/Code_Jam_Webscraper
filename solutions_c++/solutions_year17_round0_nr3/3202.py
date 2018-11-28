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
ll a[100][5];

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);

	int q;
	cin>>q;
	int c =1;
	while(q--)
	{
		ll n,k;
		//s.clear();
		cin>>n>>k;
	//	s.insert(n);
		if(k==1)
		{
			long long int mean = (n % 2)?(n+1)/2:n/2;
			cout << "Case #" << c << ": ";
			cout << max(mean-1, n-mean) << " " << min(mean-1, n-mean) << endl;
			c++;
			continue;
			
		}
		ll sz = n;
		ll i=0;
		for(int j=0;j<4;j++) a[0][j] =0 ;

		a[0][0] = n/2,a[0][1] = 1,a[0][2] = n/2,a[0][3] = 1;
		int k1 = 0,k2=k;
		if(n%2==0) a[0][2]--;
		//cout<<a[0][2]<<endl;
		ll sum = a[0][1]+a[0][3]+1;
		if(sum>=k) goto me;
		for(i=1;i<65&&sum<k;i++)
		{
			//s.clear();
			
			ll c = a[i-1][0],d = a[i-1][2],c1=0,c2=0,d1=0,d2=0;
		//	for(int j=0;j<4;j++) a[i-1][j] = 0;
			int x =0 ,x1 = 0;
			if(c%2) c1 = c/2,c2 = c/2;
			else c1 = c/2-1,c2 =c/2;
			if(d%2) d1 = d/2,d2 = d/2;
			else d1 = d/2-1,d2 = d/2;
		//	cout<<c1<<" "<<c2<<" "<<d1<<" "<<d2<<endl;
			ll b[] = {c1,c2,d1,d2};
			ll b1[] = {a[i-1][1],a[i-1][1],a[i-1][3],a[i-1][3]};
			//int idx = -1;
			for(int j=0;j<4;j++)
			{
				for(int l=j+1;l<4;l++)
				{
					if(b[j]==b[l])
					{
						b1[j]+=b1[l];
					}
				}
			}
			a[i][0] = b[0],a[i][1] = b1[0];
			int j;
			for( j=1;j<4;j++)
			{
				if(b[j]!=b[0])
				{
					break;
				}
			}
			if(j>=4) a[i][2] = b[0],a[i][3] = 0;
			else a[i][2] = b[j],a[i][3] = b1[j];
			
		 	sum+=a[i][1]+a[i][3];
			if(sum>=k) break;
			//cout<<a[i][1]<<" "<<a[i][3]<<" "<<i<<endl;
		}
		me:
		k1 = i;
		k-=sum-(a[k1][1]+a[k1][3]);
		//cout<<a[k1][0]<<" "<<a[k1][2]<<" "<<k<<endl;
		if(a[k1][0]>a[k1][2])
		{
			if(a[k1][1]>=k) sz = a[k1][0];
			else sz =a[k1][2];
		}
		else 
		{
			if(a[k1][3]>=k) sz = a[k1][2];
			else sz =a[k1][0];
		}
		cout<<"Case #"<<c<<":"<<" ";
		if(sz==1||sz==0	) cout<<"0"<<" "<<"0"<<endl;
		else
		{
			if(sz%2) cout<<sz/2<<" "<<sz/2<<endl;
			else cout<<sz/2<<" "<<sz/2-1<<endl;
		}
		c++;
	}
	return 0;
}