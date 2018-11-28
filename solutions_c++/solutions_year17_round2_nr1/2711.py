#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

#define sc(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);

#define scl(x) scanf("%lld",&x);
#define scl2(x,y) scanf("%lld%lld",&x,&y);
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);

#define pb push_back
#define mp make_pair

#define M 1000000007
#define inf 99999999999999999LL	//long long inf

#define debug(x) cerr<<#x<<" :: "<<x<<"\n";
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";
#define debug4(x,y,z,a) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#a<<" :: "<<a<<"\n";

#define LIM 100020

double d ;
int n ;
vector<  pair < double , double > >v;
double pos[100020] , sp[100030];
int main()
{
	int i,j,t;
	sc(t);
	int cc = 1;
	while(t--)
	{
		v.clear();
		cin>>d>>n;
		for(i=1;i<=n;i++)
		{
			double ss,dd;
			cin>>ss>>dd;
			v.pb( mp(ss,dd) );
		}
		sort( v.begin() ,v.end() );
		double mini_till = 0 ;
		for(i=0;i<v.size();i++)
		{
		//	debug2( v[i].first,v[i].second );
		}
		for(i=v.size()-1;i>=0;i--)
		{
			assert(v[i].second!=0);
			double chut = (d - v[i].first)/v[i].second;
			//debug(chut);
			if(chut > mini_till)
				mini_till = chut ;
		}
		printf("Case #%d: %0.6lf\n",cc++,(d/mini_till));


	}


	return 0;
}