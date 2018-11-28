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
set<ll> s;
vector<ll> vv;
void generatee(int las, ll curr, int pla)
{

	if(pla >= 20)
		return ;
	s.insert(curr);
	for(ll i=las;i<=9;i++)
	{
		generatee(i,curr*10+las,pla+1);
	}
}
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
	generatee(0,0,0);
	int t,tt=0;
	//sort(vv.begin(),vv.end());
	vv.resize(s.size());
	int k=0;
	for(ll j : s)
		vv[k++]=j;
	cin>>t;
	while(tt++<t)
	{
		cout<<"Case #"<<tt<<": ";
		ll n;
		cin>>n;
		auto kk = lower_bound(vv.begin(),vv.end(),n);
		//cout<<n<<"\n";
		//cout<<*kk<<"\n";
		if(*kk != n)
		{
			kk--;
			cout<<(*kk)<<"\n";
		}
		else cout<<n<<"\n";
	}
	return 0;
}