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

#define LIM 100005
int hello;
bool cmp(pii a,pii b)
{
	if(a.fs != b.fs)
		return a.fs > b.fs;
	if(a.sc == hello)
		return 1;
	if(b.sc == hello)
		return 0;
	return 0;

}
int main()
{
	int t,tt=1;
	sc1(t);
	while(t--)
	{
		int n,i;
		sc1(n);
		vector<pii >  v;
		int mx = 0;
		for(i=0;i<6;++i)
		{
			int x;sc1(x);
			v.pb(mp(x,i));
			mx = max(mx,x);
		}
		VI ans;
		int j;
		sort(all(v),greater<pii>());
		ans.pb(v[0].sc);
		hello = v[0].sc;
		v[0].fs--;
		int last = hello;
		bool ff = 0;
		char poo[] = {'R','O','Y','G','B','V'};
		for(i=1;i<n;++i)
		{
			sort(all(v),cmp);
			
			int put ;
			for(j=0;j<v.size();++j)
			{
				if(v[j].fs > 0 && v[j].sc != last)
				{
					put = j;
					break;
				}
			}
			if(j==v.size())
			{
				ff = 1;
			}
			ans.pb(v[put].sc);
			v[put].fs--;
			last = v[put].sc;
		}
		printf("Case #%d: ",tt++);
		if(mx>n/2)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		for(i=0;i<ans.size();++i)
			{
				printf("%c",poo[ans[i]] );
			}
			printf("\n");
	}	
	return 0;
}