#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef map<int,int> mii;


ll n,m,x,y,k;
int t;


int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		cin>>n>>k;
		printf("Case #%d: ",tc);
		x=0;
		queue<ll> q;
		q.push(n);
		map<ll,ll> mymap;
		mymap[n]=1;
		while(q.size())
		{
			y=q.front();
			q.pop();
			m=(y+1)/2;
			x+=mymap[y];
			if(k<=x)
			{
				cout<<y-m<<" "<<m-1<<endl;
				break;
			}
			if(y>1)
			{
				if(y%2!=0)
				{
					if(mymap[y-m])
					{
						mymap[y-m]+=mymap[y]*2;
					}
					else
					{
						mymap[y-m]=mymap[y]*2;
						q.push(y-m);
					}
					continue;
				}
				if(mymap[y-m])
				{
					mymap[y-m]+=mymap[y];
				}
				else
				{
					mymap[y-m]=mymap[y];
					q.push(y-m);
				}
				if(m>1){
					if(mymap[m-1])
					{
						mymap[m-1]+=mymap[y];
					}
					else
					{
						mymap[m-1]=mymap[y];
						q.push(m-1);
					}	
				}

			}
		}

	}


	return 0;	
}