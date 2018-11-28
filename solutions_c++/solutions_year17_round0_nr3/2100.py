#include<iostream>
#include<map>
#include<string>
#include<string.h>
#include<vector>
#include<stdio.h>
#include <cstdio>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <functional>
#include <math.h>
#define LL long long int
#define ii pair< int,int >
#define iii pair< int , ii > 
#define vi vector<int>
#define vii vector<ii>
#define II pair< LL , LL >
#define III pair< LL  , LL > 
#define vI vector<LL>
#define rI(B) scanf("%d",&B)
#define wI(B) printf("%d",B)
#define R(i) freopen(i,"r",stdin)
#define W(i) freopen(i,"w",stdout)
///C-small-2-attempt0.in
#define R_W R("C-large.in"),W("o.txt");
//#define R_W R("i.txt"),W("o.txt");
#define FOR(i,f,t) for(int i=f;i<t;i++)
#define r(e) for(int i=0;i<e;i++)
#define EPS 1e-9
using namespace std;
long long int solve(long long int  rest,long long int  sz){
	if(rest==1) return sz;
	long long int  l,r;
	l=r=sz/2;
	if(sz%2==0)l--;
	if(rest%2==1)return solve(rest/2,l);
	else return solve(rest/2,r);
}
int main(){
	R_W;
	long long int  t;
	cin>>t;
	long long int  cases=1;
	while(t--)
	{
		long long int  n,k;
		cin>>n>>k;
		long long int last=solve(k,n);
		if(last%2==1){
			printf("Case #%lld: %lld %lld\n",cases++,last/2,last/2);
		}else{
			printf("Case #%lld: %lld %lld\n",cases++,last/2,last/2-1);
		}
		
	}
	return 0;
}