#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<set>
#include<map>
#include<string.h>
#include<cstdio>
#include<queue>
using namespace std;
const int inf = 1000000001;
const int MOD = 1000000007;
typedef long long Int;
#define FOR(i,a,b) for(int i=(a); i<=(b);++i)
#define mp make_pair
#define pb push_back
#define sz(s) (int)((s).size())

const int N = 100000;
double s[N+1];
int k[N+1];

int main()
{
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    FOR(tt,1,t) {
        int n,d;
        cin>>d>>n;
        FOR(i,1,n) cin>>k[i]>>s[i];

        long double low=0, high = 1e18;
        FOR(iter,1,200) {
            long double mid = (low+high)/2;

            long double mn=d+1;
            FOR(i,1,n) {
                long double cur = k[i]+(d/mid)*s[i];
                mn=min(mn, cur);
            }

            if(mn<d) high=mid;else low=mid;
        }
        cout<<"Case #"<<tt<<": ";
    	printf("%.6lf\n", (double)high);
    }
}
