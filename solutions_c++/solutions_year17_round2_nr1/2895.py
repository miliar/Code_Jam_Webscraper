//template.cpp
#include <bits/stdc++.h>
using namespace std;

#define lll long long int  
#define mp make_pair
#define pb push_back

#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define scl(x) scanf("%lld",&x)
#define scl2(x,y) scanf("%lld%lld",&x,&y)
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define scstr(x) scanf("%s",x)
#define pf(x) printf("%d",x)
#define pfl(x) printf("%lld",x)
#define pfstr(x) printf("%s",x) 


#define newl() printf("\n")
#define fl(i,n) for (i=0;i<n;i++)
#define fl1(i,n) for (i=1;i<=n;i++)
#define fla(i,n,a) for (i=a;i<n;i++)
#define mem(a,i) memset(a,i,sizeof(a))

typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > pipii ;
typedef pair<lll,pair<lll,lll> > plpll ;
typedef pair<lll,lll> pll;
typedef pair<lll,int> pli;
#define gcd __gcd

#define debug(x) cout<<"debug->"<<#x<<"::"<<x<<endl
#define debug2(x,y) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n"
#define debug3(x,y,z) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n"
#define debug4(x,y,z,P) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#P<<" :: "<<P<<"\n"
#define debug5(x,y,z,P,O) cout<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#P<<" :: "<<P<<"\t"<<#O<<" :: "<<O<<"\n"
#define itr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)


#define MOD 1000000009
#define MAX 100001

int main()
{
	double x;
	lll a, b, c, i, j, k, T, N, D, K[1001], M[1001], S[1001];

	std::cout << std::fixed;
    std::cout << std::setprecision(7);

	scl(T);
	b = 0;
	while(T--)
	{
		b++;
		cin >> D >> N;
		double x, y, z, ans = -1;
		fl(i, N){
			cin >> x >> z;
			y = D-x;

			// debug2(y, z);

			ans = max(ans, y / z);
		}

		// debug2(D, ans);
		cout << "Case #" << b << ": " << D / ans << endl;
		
	}


	return 0;
}