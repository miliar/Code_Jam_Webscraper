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
char s[123];
int a[50][50],xx[50][50];
int main()
{
	int t,tt=1;
	sc1(t);
	while(t--)
	{
		ini(a,0);
		ini(xx,0);
		int r,c,i,j,k,l;
		sc2(r,c);
		for(i=0;i<r;++i)
		{
			scanf("%s",s);
			for(j=0;j<c;++j)
			{
				if(s[j]!='?')
				a[i][j] = s[j] - 'A' + 1;
				else a[i][j] = 0;
			}
		}
/*
		for(i=0;i<r;++i)
		{
			for(j=0;j<c;++j)
			{
				printf("%c",a[i][j]+'A'-1);
			}
			printf("\n");
		}*/
		for(i=0;i<r;++i)
		{
			for(int l=0;l<c;++l)
			{
				if(xx[i][l]==1)continue;
				int cnt = 0,rr,cc,val;
				for(j=i;j<r;++j)
				{
					for(k=l;k<c;++k)
					{
						int val2;
						int hsh[50]={0};
						cnt = 0;
						
		
						for(int p = i;p<=j;++p)
						{
							for(int q = l;q<=k;++q)
							{
								hsh[a[p][q]]++;		
								if(a[p][q]>0 && hsh[a[p][q]]==1)
								{
									cnt++;
									if(cnt==1)
									val2 = a[p][q];
								}
								if(cnt>1)break;
								
				
							}
						}
						if(cnt == 1)
								{
									rr = j;cc = k;
									val = val2;

								}		
						
					}
				}
				//debug4(i,l,rr,cc);debug(val);
				bool f=1;
				for(j=i;j<=rr;++j)
				{
					for(k=l;k<=cc;++k)
					{
						if(xx[j][k])f=0;
					}
				}
				if(f==0)continue;
				for(j=i;j<=rr;++j)
				{
					for(k=l;k<=cc;++k)
					{
						xx[j][k]=1;
						a[j][k] = val;
					}
				}

			}
		}
		printf("Case #%d:\n",tt++);
		for(i=0;i<r;++i)
		{
			for(j=0;j<c;++j)
			{
				printf("%c",a[i][j]+'A'-1);
			}
			printf("\n");
		}
	}	
	return 0;
}