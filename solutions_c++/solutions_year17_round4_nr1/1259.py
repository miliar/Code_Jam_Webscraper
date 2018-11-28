#include <bits/stdc++.h>
using namespace std;
#define F first
#define S second
#define itt ::iterator
#define ritt ::reverse_iterator
#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >
const int NSIZ=110;
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

int n, m, o, re=0, test;
long long res=0;
int a[NSIZ], b[NSIZ];
char c[NSIZ];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
    	memset(a,0,sizeof(a));
    	re=0;
    	scanf("%d %d", &n, &m);
    	for(i=0; i<n; i++){
    		scanf("%d", &j);
    		a[j%m]++;
    	}
    	printf("Case #%d: ", zz);
    	if(m==2){
    		re+=a[0];
    		re+=(a[1]+1)/2;
    	}
    	else if(m==3){
    		re+=a[0];
    		re+=min(a[1],a[2]);
    		k=max(a[1],a[2])-min(a[1],a[2]);
    		re+=(k+2)/3;
    	}
    	else {
    		// printf("%d %d %d\n", a[1], a[2], a[3]);
    		re+=a[0];
    		re+=min(a[1],a[3]);
    		k=max(a[1],a[3])-min(a[1],a[3]);
    		j=min(k/2,a[2]);
    		re+=j;
    			k-=j*2;a[2]-=j;
    		j=a[2]/2;
    		re+=j;
    			a[2]-=j*2;
    		j=k/4;
    		re+=j;
    			k-=j*4;
    		if(a[2]+k>0)re++;
    	}
    	printf("%d\n", re);
    }
    return 0;
}