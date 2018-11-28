
// Redefined
#include<bits/stdc++.h>

using namespace std;

typedef long long int LL;

#define  SI(N)          scanf("%d",&N)
#define  SLL(N)         scanf("%lld",&N)
#define  MP             make_pair
#define  PB             push_back
#define  X              first
#define  Y              second
#define  FOR(i,M,N)     for(int i=(M);i<=(N);++i)
#define  FORN(i,N,M)    for(int i=(N);i>=(M);--i)
#define  MIN(a,b)       ((a)<(b) ? (a) : (b))
#define  MAX(a,b)       ((a)>(b) ? (a) : (b))
#define  VI             vector<int>
#define  PII            pair<int,int>
#define  FILL(arr,n)    memset((arr),n,sizeof((arr)))
#define  fastInput      ios_base::sync_with_stdio(false)

const int MAXN = 100007;

void solve(int testcase){
    int D,N;
    SI(D);
    SI(N);
    VI d(N+2),s(N+2);
    double maxTime = 0.0;
    FOR(i,1,N){
        SI(d[i]);
        SI(s[i]);
        maxTime = MAX((D - d[i])/(double)s[i], maxTime);
    }


    FOR(i,1,N){

        int index = -1;
        FOR(j,i+1,N){
            if(s[i] > s[j] && d[j] >= d[i]){
                double t = (d[j] - d[i])/(double)(s[i] - s[j]);
                double dist = d[i] + s[i] * t;
                if(dist <= D){
                    maxTime = MAX(maxTime, t + (D - dist)/s[j]);
                    //cout << i << " " << j << " " << t + (D - dist)/s[j] <<  " " << dist << endl;
                }
            }
        }
    }
    printf("Case #%d: %.6lf\n", testcase, D / maxTime);
}

void init(){
    //fastInput;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}
int main() {


    clock_t tc,_start, _end;
    init();
	int T = 1;

    tc = clock();
	scanf("%d",&T);
	FOR(test, 1, T)
	{
        _start = clock();
        solve(test);
        _end = clock();
        //fprintf(stderr,"**  Time: %d :           %lf \n", test, (_end - _start)/ (double)CLOCKS_PER_SEC);
	}

    //fprintf(stderr,"*** Total time :       time : %lf \n",  (_end - tc )/(double)CLOCKS_PER_SEC);
	return 0;
}
