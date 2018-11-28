#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define itt ::iterator
#define ritt ::reverse_iterator
#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >
const int NSIZ=1000010;
const int MSIZ=1000010;
const int inf=1010580540;
const int mxint=2147483647;
const long long mxll=9223372036854775807LL;
const long long prime15=1000000000000037LL;
const long long mod=1000000007LL;
const long long mod9=1000000009LL;
typedef pair<int,int> pii;
typedef pair<double,int> pdi;
typedef pair<long long,long long> pll;
typedef pair<double,double> pdd;
typedef pair<int,pair<int,int> > pip;
typedef pair<long long,pair<int,int> > plp;
typedef pair<pair<int,int>,pair<int,int> > ppp;

int n, m, o, re=0, test;
long long res=0;
pii a[NSIZ], b[NSIZ];
char c[NSIZ];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
    	scanf("%lld %d", &ll, &n);
    	for(i=0; i<n; i++){
    		scanf("%d %d", &a[i].F, &a[i].S);
    	}
    	sort(a,a+n);
    	double tim=0;
    	for(i=n-1; i>=0; i--){
    		double t=(double)(ll-a[i].F)/a[i].S;
    		tim=max(tim,t);
    	}
    	double v=ll/tim;
    	printf("Case #%d: %.8lf\n", zz, v);  
    }
    return 0;
}