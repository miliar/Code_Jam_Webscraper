// Author : Muhammad Rifayat Samee
// Problem :
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<complex>
#include<valarray>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b
#define INF 987654321
#define pi (2*acos(0.0))
#define eps 1e-12

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;
struct Node{
    int x;
    int s;
    bool operator<(const Node &a)const{
        return x<a.x;
    }
}N[1001];
int D,n;
int main(){

	freopen("A_l.in","r",stdin);

	freopen("A_large.out","w",stdout);
    int cases,i,j,k,ct=1;
    scanf("%d",&cases);
    while(cases--){
        scanf("%d %d",&D,&n);
        for(i=0;i<n;i++){
            scanf("%d %d",&N[i].x,&N[i].s);
        }
        sort(N,N+n);
        double curtime = (double)(D-N[n-1].x)/N[n-1].s;
        int cur = n-1;
        for(i=n-2;i>=0;i--){
            double t =  (double)(D-N[i].x)/N[i].s;
            if(t>curtime){
                cur = i;
                curtime = t;
            }
        }
        //printf("%d %d\n",N[cur].x,N[cur].s);
        printf("Case #%d: %lf\n",ct++,(double)D/curtime);
    }

	return 0;
}
