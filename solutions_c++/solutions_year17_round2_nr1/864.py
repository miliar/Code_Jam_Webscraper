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
#define INF 2000000000 // 2 billion

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    s(T);
    REP( t , 1 , T ) {
    	double d ; 
    	int n ; 
    	cin >> d; 
    	double maxtimeTaken = 0;
    	s(n);
    	REP( i , 0 , n - 1 ){
    		double currentDist , speed ; 
    		cin >> currentDist >> speed ; 
    		maxtimeTaken = max( (d - currentDist) / speed , maxtimeTaken ) ;
    	}
    	double ans = d / maxtimeTaken;
    	printf("Case #%d: %0.7lf\n",t,ans);
    }
    return 0;
}
