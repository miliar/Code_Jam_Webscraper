#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int > pii;
typedef pair<int,pii > piii;
typedef vector<int>     VI;

#define sc1(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);
/*
#define sc1(x) scanf("%lld",&x);
#define sc2(x,y) scanf("%lld%lld",&x,&y);
#define sc3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);
*/
#define pb push_back
#define mp make_pair
#define ini(x,val) memset(x,val,sizeof(x));
#define fs first
#define sc second
#define MOD 1000000007
#define inf 1000000001
#define linf 99999999999999999ll	//long long inf
#define PI 3.1415926535897932384626
const double eps=0.000000000000001 ;

#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define PrintCont(cont) {cout<<("\n----------------\n");\
for(typeof(cont.begin()) it = cont.begin();it!=cont.end();++it) cout<<*it<<" ";cout<<("\n----------------\n");}
#define all(v) v.begin(),v.end()
string convertstring(ll n) { stringstream ss; ss << n ; return ss.str(); }

#define debug(x) cerr<<#x<<" :: "<<x<<"\n";
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";
#define debug4(x,y,z,a) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#a<<" :: "<<a<<"\n";
#define debugarr(a,st,en) {cerr<<"\n"<<#a<<" :: ";for(int i=st;i<=en;++i)cerr<<a[i]<<" ";cerr<<"\n";}

#define LIM 2005

int a[LIM],temp[100];
VI v[100];
int main()
{
	int t,tt=1;
	sc1(t);
	while(t--)
	{

		int n,p,i,j;
		sc2(n,p);
		for(i=0;i<100;++i)
			v[i].clear();
		for(i=0;i<n;++i)
		{
			sc1(a[i]);
		}
		for(i=0;i<n;++i)
		{
			for(j=0;j<p;++j)
			{
				int x;
				sc1(x);
				v[i].pb(x);
			}
			sort(all(v[i]));
		}
		int serv = 1,kit = 0,prevserv = 1,cnt=0;
		for(i=0;i<p;)
		{

			int x = v[0][i];
			bool f= 0 ;
			serv = prevserv;
			bool ff = 0;
			for(;;)
			{
				cnt++;
				//debug2(i,serv);
				int req = serv*a[0];
				int z = ceil(req*9.0/10.0);
				int y = req*11.0/10.0;
				if(x<z){
					f=1;
					break;
				}
				if(x>=z && x<=y)
				{
					if(ff==0)
						prevserv = serv;
					for(j=1;j<n;++j)
					{
						int req = serv*a[j];
						int z = ceil(req*9.0/10.0);
						int y = req*11.0/10.0;
						int yo = lower_bound(all(v[j]),z) - v[j].begin();
						temp[j] = yo;
						if(yo<v[j].size() && v[j][yo]<=y)
						{
							//v[j].erase(v[j].begin(),v[j].begin()+yo+1);
						}
						else break;
					}
					if(j==n)
					{
						kit++;
						for(j=1;j<n;++j)
						{
							v[j].erase(v[j].begin(),v[j].begin()+temp[j]+1);
						}
						goto hello;
					}
					else serv++;
				}
				else serv++;
			}

			if(f){
				hello :
				++i;
				continue;
			}
		}
		printf("Case #%d: %d\n",tt++,kit);
		

	}	
	return 0;
}