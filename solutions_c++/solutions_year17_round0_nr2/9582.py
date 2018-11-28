#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>
#include <string.h>
#include <cctype>
#include <list>
#include <vector>
#include <cstdlib>
#include <stack>
#include <cmath>
#include <limits.h>
#include <map>
#include <utility>
#include <set>
#define xfor(i,start,end) for(int i=start;i<end;i++)
#define rfor(i,end,start) for(int i=end-1;i>=start;i--)
#define scan(x) scanf("%d",&x)
#define print(x) printf("%d ",x)
#define init(x) memset(x,0,sizeof(x))
#define pb push_back
#define pf pop_front
#define mp make_pair
#define f first
#define s second
#define PI 3.141592654
typedef long long ll;
const ll INF=ll(1e18);
const int MOD=1e9+7;
using namespace std;
list <int> adj[200001];
map < pair < int, int>, int > edge,visits;
bool vis[2000001];
int res=0,max1,num,bhai=0;
int c[200001],d[200001];

int rin[2000001],rout[2000001];
int in[2000001],out[2000001];
map < pair < int, int>, bool > vedge;
map < int , pair < int, int> > ith;
bool sw=true;
vector <int> final;

int main()
{
	std::ios_base::sync_with_stdio(false);
	freopen("/Users/Rahul/Desktop/B-small-attempt1.in","r",stdin);
	freopen("/Users/Rahul/Desktop/out.txt","w",stdout);
	int t;
	ll k;
	cin>>t;
	xfor(i,0,t)
	{
		cin>>k;
		ll cnt=0,m=k,comp=1,one,woh,woh1,f=-1,flaa=0;
		while(m>0)
		{
			woh=m%10;
			m/=10;
			woh1=m%10;
			cnt++;
			if(woh<woh1&&woh1!=0) flaa=1;
			if(woh<=woh1&&woh1!=0&&flaa==1) f=cnt;
		}
		if(f==-1) f=0;
		xfor(j,0,cnt-1) comp=(10*comp)+1;
		if(k<comp) cnt--;
		char num[cnt];
		string temp=to_string(k);
		xfor(j,0,cnt) num[j]=temp[j];
		xfor(j,cnt-f-1,cnt) num[j]='9';
		xfor(j,cnt-f-1,cnt)
		{
			bool flag=false;
			xfor(o,0,9)
			{
				num[j]='9'-o;
				one=strtol(num,NULL,10);
				if(one<=k) 
				{
					flag=true;
					break;
				}
			}
			if(flag) break;
		}
		cout<<"Case #"<<i+1<<": "<<one<<endl;
	}
	return 0;
}




