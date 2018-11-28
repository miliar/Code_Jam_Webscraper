/* In the Name of God */
#include <bits/stdc++.h> 
#define F first
#define S second
#define mod 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 100000+10;

ofstream fout("out.out");

ld eps = 1e-8;
ld s[maxn] , k[maxn];
ld dis ;
ll n ;
bool check(ld mid)
{
	ld tim = dis / mid ;
	for( int i = 1 ; i <= n ; i ++ )
		if( s[i]*tim + k[i] < dis )
			return 0;
	return 1;
}
int main()
{
	int t ,test = 1 ;
	cin>>t;
	while(t)
	{

		ld l=0 , h=1e18 , mid =0;

		cin>>dis>>n;
		for(int i = 1 ; i <= n ; i ++ )
			cin>>k[i]>>s[i];

		if(n >0)
			for(int i = 1 ; i <=300 ; i ++ )
			{
				mid = (l+h)/2;
				if(check(mid))
					l=mid+eps;
				else
					h=mid-eps;
			}
		if(n == 0 )
			cout<<":|";
		fout<<"Case #"<<test<<": "<<fixed<<setprecision(6)<<mid<<endl;

		t--;
		test ++ ;
	}	
}	
