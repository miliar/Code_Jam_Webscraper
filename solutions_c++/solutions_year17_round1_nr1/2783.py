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
char ch[40][40];
int r,c;
int starting, ending ;
int done[40];
int check( int i , int j , int x , int y)
{
	int has[ 30 ] = {0};
	for(int kk =i;kk<i+x;kk++)
	{
		for(int tt = j ; tt < j+y ;tt++)
		{
			if( ch[kk][tt] != '?' )
			{
				has[ ch[ kk ][ tt ] - 'A' +1 ]++;
				if( has[ ch[ kk ][ tt ] - 'A' +1 ] >1 )
					return 0;
			}
		}
	}
	int coun = 0 , last;
	char ch ;
	for(i=1;i<=26;i++)
	{
		if(has[ i ])
		{
			coun++;
			last = i;

		}
	}
	if(coun==1)
	{
		return last;
	}
	else
	{
		return 0;
	}
}
vector< pair< int, pair < int, int> > >v;
void doit(int x , int y)
{
	//debug2(x,y);
	if(x<=0 || y<=0)
		return ;
	else
	{
		for(int i=0 ; i+x <=r;i++)
		{
			for(int j =0;j+y <=c;j++)
			{
				int tamtam = check( i,j,x,y ) ;
				if( tamtam >0 && done[ tamtam ] ==0)
				{

					int todo = tamtam;
					if(todo)
						for(int k = i ; k< i+x;k++)
						{
							for (int l = j; l < j+y; l++)
							{
								ch[k][l] = todo + 'A' -1 ;
							}
						}
						done[ tamtam ]++;
				}
			}
		}
	}
}
int bhos = 1;
int main()
{
	int i,j,t;
	sc(t);
	while(t--)
	{
		memset(done,0,sizeof done);
		sc2(r,c);
		v.clear();
		for(i=1;i<=r;i++)
		{
			for(j=1;j<=c;j++)
			{
				v.pb(mp( -i*j ,mp(i,j) ));
			}
		}
		sort( v.begin() , v.end() );
		for(i=0;i<r;i++)
			scanf("%s",ch[i]);
		for(i=0;i<v.size();i++)
		{
			doit( v[i].second.first,v[i].second.second ); 
		}	
		printf("Case #%d:\n",bhos++);
		for(i=0;i<r;i++)
			printf("%s\n",ch[i]);
	}
	return 0;
}