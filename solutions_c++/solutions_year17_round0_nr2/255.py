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
bool isok(){
	for(int i=0; i<n; i++)if(b[i]>'9')return false;
	for(int i=0; i<n; i++){
		if(b[i]>a[i])return false;
		if(b[i]==a[i])continue;
		if(b[i]<a[i])return true;
	}
	return true;
}
void print(){
	for(int i=0; i<n; i++){
		printf("%c", b[i]);
	}printf("\n");
}
void inc(int d){
	for(int i=d; i<n; i++){
		b[i]++;
	}
}
void dec(int d){
	for(int i=d; i<n; i++){
		b[i]--;
	}
}
void check(int d){
	do{
		inc(d);
		// print();
	}while(isok());
	dec(d);
}
int main(){
    int i, j, k, l;
    long long ll=0, rr=mxll, mid;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
    	scanf("%s", a);
    	n=strlen(a);
    	for(i=0; i<n; i++){
    		b[i]='1';
    	}
    	printf("Case #%d: ", zz);
    	if(!isok()){
    		for(i=0; i<n-1; i++){
    			printf("9");
    		}printf("\n");
    		continue;
    	}
    	for(i=0; i<n; i++){
    		check(i);
    		// printf("%d = ", i);print();
    	}
    	for(i=0; i<n; i++){
    		printf("%c", b[i]);
    	}printf("\n");
    }
    return 0;
}
