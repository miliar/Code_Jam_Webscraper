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
typedef pair<long long,int> pli;
typedef pair<long long,long long> pll;
typedef pair<double,double> pdd;
typedef pair<int,pair<int,int> > pip;
typedef pair<long long,pair<int,int> > plp;
typedef pair<pair<int,int>,pair<int,int> > ppp;

long long n, m, o, re=0;
int test;
long long res=0;
pll tmp[2][2];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
    	scanf("%lld %lld", &n, &m);
    	memset(tmp,0,sizeof(tmp));
    	tmp[0][0]=pll(n,1);
    	bool ch=1;o=1;
    	while(o<m){
    		tmp[ch][0]=tmp[ch][1]=pll(0,0);
    		ll=tmp[!ch][0].F/2;rr=ll-1;
    		tmp[ch][0].F=ll;
    		tmp[ch][1].F=rr;
    		if(tmp[!ch][0].F%2==1){
    			tmp[ch][0].S+=tmp[!ch][0].S*2;
    		}
    		else{
    			tmp[ch][0].S+=tmp[!ch][0].S;
    			tmp[ch][1].S+=tmp[!ch][0].S;
    		}
    		if(tmp[!ch][1].F%2==1){
    			tmp[ch][1].S+=tmp[!ch][1].S*2;
    		}
    		else{
    			tmp[ch][0].S+=tmp[!ch][1].S;
    			tmp[ch][1].S+=tmp[!ch][1].S;
    		}
    		m-=o;
    		o<<=1;
    		// printf("%lld,%lld = %lld,%lld %lld,%lld\n", o,m, tmp[ch][0],tmp[ch][1]); 
    		ch=!ch;
    	}
    	ch=!ch;
    	// printf("%lld %lld-%lld %lld-%lld\n", o, tmp[ch][0], tmp[ch][1]);
    	if(tmp[ch][0].S<m)o=tmp[ch][1].F;
    	else o=tmp[ch][0].F;
    	if(o%2==0)printf("Case #%d: %lld %lld\n", zz, o/2,o/2-1);
    	else printf("Case #%d: %lld %lld\n", zz, o/2, o/2); 
    }
    return 0;
}
