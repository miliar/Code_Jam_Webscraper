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

int n, m, o, re=0, test;
long long res=0;
char a[NSIZ], b[NSIZ];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
    	scanf("%s %d", a, &m);
    	n=strlen(a);
    	re=0;
    	for(i=0; i<n; i++){
    		if(a[i]=='+')continue;
    		re++;
    		if(i+m>n)break;
    		for(j=i; j<i+m; j++){
    			if(a[j]=='+')a[j]='-';
    			else a[j]='+';
    		} 
    	}
    	printf("Case #%d: ", zz);
    	if(i<n)printf("IMPOSSIBLE\n");
    	else printf("%d\n", re);
    }
    return 0;
}
