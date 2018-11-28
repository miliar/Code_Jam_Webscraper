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
	freopen("/Users/Rahul/Desktop/A-large.in","r",stdin);
	freopen("/Users/Rahul/Desktop/out.txt","w",stdout);
	int t,k;
	cin>>t;
	string s;
	xfor(m,0,t)
	{
		int f=-1,l=-1,cnt=0,num=0,flag=0;
		cin>>s;
		cin>>k;
		xfor(i,0,s.length())
		{
			if(s[i]=='-')
			{
				if(num==0) f=i;
				num++;
			}
		}
		rfor(i,s.length(),0)
		{
			if(s[i]=='-')
			{
				l=i;
				break;
			}
		}
		if(l==-1)
		{
			cout<<"Case #"<<m+1<<": "<<0<<endl;
			continue;
		}
		while(num!=0)
		{
			cnt++;
			if(f+k<=s.length())
			{
				s[f]='+';
				num--;
				xfor(q,f+1,f+k)
				{
					if(s[q]=='-')
					{
						s[q]='+';
						num--;
					}
					else 
					{
						s[q]='-';
						num++;
					}
				}
				xfor(i,f+1,s.length())
				{
					if(s[i]=='-')
					{
						f=i;
						break;
					}
				}
			}
			else
			{
				num=0;
				flag=1;
			}
		}
		if(flag==0) cout<<"Case #"<<m+1<<": "<<cnt<<endl;
		else cout<<"Case #"<<m+1<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}




