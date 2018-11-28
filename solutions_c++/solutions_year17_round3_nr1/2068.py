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
    double r;
    double h;
    double A;
    bool operator<(const Node &a)const{
        if(A!=a.A)
            return A > a.A;

    }
}N[1001];
int n,k;

int main(){

	freopen("A.in","r",stdin);
	freopen("A_s.out","w",stdout);
    int cases,i,j,ct=1;
    scanf("%d",&cases);

    while(cases--){
        scanf("%d %d",&n,&k);
        for(i=0;i<n;i++){
            scanf("%lf %lf",&N[i].r,&N[i].h);
            N[i].A = N[i].r*N[i].h;
        }

        sort(N,N+n);

        double res = 0;
        int tot = 0;
        for(i=0;i<n;i++){
            tot = 1;
            double r = pi*N[i].r*N[i].r + 2*pi*N[i].A;

            for(j=0;j<n;j++){
                if(tot == k)break;
                if(i!=j && N[i].r>=N[j].r){
                    r = r + 2*pi*N[j].r*N[j].h;
                    tot++;
                }
            }
            if(res<r)res = r;

        }

        printf("Case #%d: %.10lf\n",ct++,res);
    }

	return 0;
}
