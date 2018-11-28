#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <queue>
#include <cstring>
#include <map>
#include <set>
#include <iomanip>
#include <algorithm>

# define ini(c) int c; scanf("%d",&(c))
# define outi(c) printf("%d \n",(c)) 
# define rf freopen("input.in","r",stdin)
# define wf freopen("output.txt","w",stdout)
# define pb(c) push_back(c)
# define mp(c,d) make_pair(c,d)
# define all(c) (c).begin(),(c).end()
# define tr(c,i) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
# define test(c) ini(c);while(c--)

using namespace std;

typedef vector< int > vi;
typedef vector< vi > vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef long long ll;

int main()
{
    rf;wf;
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		double d;int n;
		cin>>d>>n;
		double slowesttime=0;
		for(int i=0;i<n;i++)
		{
			double inipos,speed;
			cin>>inipos>>speed;
			double time=(d-inipos)/speed;
			if(time>slowesttime) slowesttime=time;
		}

		double ans=d/slowesttime;
		cout<<"Case #"<<test<<": "<<fixed<<setprecision(7)<<ans<<endl;
	}	
}
