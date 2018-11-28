#include<bits/stdc++.h>

using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
 
#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,a,b) for(int i=a;i<b;i++)
#define ALL(v) (v).begin(),(v).end()
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define pb push_back
#define mp make_pair
#define INF (int)1e9
#define EPS (double)(1e-9)
#define PI (double)(3.141592653589793)
#define gc getchar
#define ff first
#define ss second

inline int read(){
	int n = 0, c = gc(), f = 1;
	while(c != '-' && (c < '0' || c > '9')) c = gc();
	if(c == '-') f = -1, c = gc();
	while(c >= '0' && c <= '9')
	n = (n<<3) + (n<<1) + c - '0', c = gc();
	return n * f;
}


int main()
{


freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);

int test,cas;
long i,d,n;
vector<long> k,s;
double *t,ans;
long kval,sval;

cin >> test;

for(cas = 1 ; cas <= test ; cas ++)	{

	scanf("%ld %ld",&d,&n);
	t = new double[n];
	k.clear();
	s.clear();
	for(i=0;i<n;i++)	{
		scanf("%ld %ld",&kval,&sval);
		k.pb(kval);
		s.pb(sval);
		t[i] = ((double) (d - k[i])) / s[i];
	}

	double min_time = t[0];
	long min_dist = k[0];
	long min_speed = s[0];

	for(i=0;i<n;i++)	{
		if(t[i] > min_time)	{
			min_time = t[i];
			min_dist = k[i];
			min_speed = s[i];
		}
	}
	ans = (double)min_dist / min_time  + min_speed;
	printf("Case #%d: %.6f\n",cas,ans);
}

return 0;
}

