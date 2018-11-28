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
int a[NSIZ], b[NSIZ], lin[NSIZ];
char c[7]="ROYGBV", ans[NSIZ];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    scanf("%d", &test);
    lin[4]=1;
    lin[0]=3;
    lin[2]=5;
    for(int zz=1; zz<=test; zz++){
    	scanf("%d", &n);
    	for(i=0; i<6; i++){
    		scanf("%d", &a[i]);
    	}
    	printf("Case #%d: ", zz);
    	if(a[4]==a[1] && a[4]!=0){
    		if(a[4]+a[1]==n){
    			for(i=0; i<a[4]; i++){
    				printf("BO");
    			}
    			printf("\n");
    		}
    		else printf("IMPOSSIBLE\n");
    		continue;
    	}
    	if(a[0]==a[3] && a[0]!=0){
    		if(a[0]+a[3]==n){
    			for(i=0; i<a[0]; i++){
    				printf("RG");
    			}
    			printf("\n");
    		}
    		else printf("IMPOSSIBLE\n");
    		continue;
    	}
    	if(a[2]==a[5] && a[2]!=0){
    		if(a[2]+a[5]==n){
    			for(i=0; i<a[2]; i++){
    				printf("YV");
    			}
    			printf("\n");
    		}
    		else printf("IMPOSSIBLE\n");
    		continue;
    	}
    	a[4]-=a[1];
    	a[0]-=a[3];
    	a[2]-=a[5];

    	memset(ans,'.',sizeof(ans));
    	k=0;
    	if(a[2]>a[k])k=2;
    	if(a[4]>a[k])k=4;
    	for(i=0; i<a[k]; i++){
    		ans[i*3]=k;
    	}
    	int ch=1, fail=1;j=0;
    	// printf("..%d\n", k);
    	for(i=0; i<=4; i+=2){
    		if(i==k)continue;
    		for(l=0; l<a[i]; l++){
    			ans[j*3+ch]=i;j++;
    			if(j>=a[k]){j=0;fail=0;}
    		}
    		ch++;
    	}
    	if(fail){printf("IMPOSSIBLE\n");continue;}
    	chk[4]=(a[1]==0);
    	chk[0]=(a[3]==0);
    	chk[2]=(a[5]==0);
    	for(i=0; i<NSIZ; i++){
    		if(ans[i]=='.')continue;
    		if(chk[ans[i]]==0){
    			for(j=0; j<a[lin[ans[i]]]; j++){
    				printf("%c%c", c[ans[i]], c[lin[ans[i]]]);
    			}
    			chk[ans[i]]=1;
    		}
    		printf("%c", c[ans[i]]);
    	}printf("\n");
    }
    return 0;
}