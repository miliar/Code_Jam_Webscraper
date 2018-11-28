/******************************************************************
* Oh, Lord.                                                       *
* Oooh, You are so big... So absolutely huge.                     *
* Gosh, We're all really impressed down here, I can tell you.     *
* Forgive us, Oh Lord, for this our dreadful toadying... and bare-*
* faced flattery.                                                 *
* But you're so strong and, well just so... super.                *
* Fantastic.                                                      *
******************************************************************/
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
#define forr(i, n) for(int i=0;i<(n);i++)
#define forv(i, v) for(int i=0;i<(int)v.size();i++)
#define fords(it, ds) for(auto it = ds.begin();it!=ds.end();it++)
#define OO (int)1e9
#define fr first
#define se second
#define II pair<int, int>
#define pb push_back
#define dist(x,y,xx,yy) sqrt((x-xx)*(x-xx)+(y-yy)*(y-yy))
///////////////////// Solution Code

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	#ifndef ONLINE_JUDGE
		#ifdef _WIN64
		freopen("C:\\Users\\mamdouh\\Desktop\\a1.in","r",stdin);
		freopen("C:\\Users\\mamdouh\\Desktop\\A2.out","w",stdout);
		#elif __linux__
		freopen("/media/mamdouh/System/Users/Mamdouh/Desktop/a1.in","r",stdin);
		freopen("/media/mamdouh/System/Users/Mamdouh/Desktop/A2.out","w",stdout);
		#endif
	#endif
	int t,tt=0;
	cin>>t;
	while(tt++<t)
	{
		cout<<"Case #"<<tt<<": ";
		ll n,k,x,y;
		cin>>n>>k;
		priority_queue<ll> q;
		unordered_map<ll, ll> mymap;
		mymap[n] =1;
		q.push(n);
		while(k>0)
		{
			
			n= q.top();
			q.pop();
			//cout<<k<<" "<<n<< " "<<mymap[n]<<endl;
			if(mymap[n]>=k)
			{
				n--;
				x=n/2;
				y=(n/2) + (n%2);
				break;
			}
			k-=mymap[n];
			n--;
			x=n/2;
			y=(n/2) + (n%2);
			//cout<<n<<" "<<x<<" "<<y<<"\n";
			if(x>0&&mymap.find(x)==mymap.end()) q.push(x);
			mymap[x]+=mymap[n+1];
			if(y>0&&mymap.find(y)==mymap.end()) q.push(y);
			mymap[y]+=mymap[n+1];
			
			//cout<<x<<" "<<y<<" ";
		}
		cout<<max(x,y)<<" "<<min(x,y)<<"\n";
	}
	return 0;
}