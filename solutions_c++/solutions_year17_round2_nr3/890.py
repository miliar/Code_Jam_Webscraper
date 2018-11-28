#include<bits/stdc++.h>

using namespace std;

// Shortcuts for "common" data types in contests
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define s(i) scanf("%d",&i)
#define sl(i) scanf("%ld",&i)
#define sll(i) scanf("%lld",&i)
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define NREP(i,a,b) \
for (int i = int(a); i >= int(b); i--)
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 20000000 // 2 billion

double dp[109];
double dis[109][109] ;
int N , Q;
pair<double,double> a[109];

double memoize( int start ){
	if( start == N - 1 )
		return 0;
	if( dp[start] != -1 ){
		return dp[start];
	}
	double maxi = INF *1ll* INF; 
	REP( i , start + 1 , N - 1 ){
		double distance = 0 ;
		REP( j , start + 1 , i ){
			distance += dis[j - 1][j];
		}
		//cout << distance << " " << a[start].first << endl;
		if( distance <= a[start].first ){
			maxi = min( maxi , memoize(i) + (distance) / a[start].second ) ;
		}
	}
	return dp[start] = maxi ;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T ; 
    s(T);
    REP( t , 1 , T ) {
    	int u , v;
    	s(N) ;
    	s(Q); 
    	REP( i , 0 , N - 1 ){
    		scanf("%lf",&a[i].first);
    		scanf("%lf",&a[i].second);
    	}
    	REP( i , 0 , N - 1 ){
    		REP( j , 0 , N - 1 ){
    			scanf("%lf",&dis[i][j]);
    		}
    	}
    	s(u) ; s(v);
    	REP( i , 0 , N ) {
    		dp[i] = -1;
    	}
    	printf("Case #%d: %0.7lf\n",t,memoize(0));
    }
    return 0;
}
