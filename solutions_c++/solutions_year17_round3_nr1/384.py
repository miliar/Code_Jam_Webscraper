#include <stdio.h>
#include <iostream>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;
#define f first
#define s second
#define push_back pb
typedef long long ll;
typedef pair<double, double> pii;

const double PI = 3.141592653589793238;

pii arr[1005];
pii tmp[1005];

bool cmp1(pii a, pii b){
    return a.f > b.f;
}

bool cmp2(pii a, pii b){
    return a.s > b.s;
}

void process(){
    memset(arr,0,sizeof(arr));
    memset(tmp,0,sizeof(tmp));
    int n, k;
    double maxi = -1;
    scanf("%d %d",&n,&k);
    for(int i = 0; i < n ; i++){
        double a, b;
        scanf("%lf %lf",&a,&b);
        arr[i].f = a*a;
        arr[i].s = 2*a*b;
        tmp[i] = arr[i];
    }
    sort(arr,arr+n,cmp1);
    sort(tmp,tmp+n,cmp2);
    for(int i = 0 ; i <= n-k ; i++){
        double mx = arr[i].f, ck = arr[i].s;
        int chk = 1;
        double ans = ck;
        int cnt = 1;
        for(int j = 0 ; j < n ; j++){
            if(cnt == k){
                break;
            }
            if(chk&&tmp[j].f==mx&&tmp[j].s==ck){
                chk = 0;
                continue;
            }
            if(tmp[j].f <= mx){
                cnt++;
                ans += tmp[j].s;
            }
        }
        //printf("%d %lf\n",i,ans+mx);
        maxi = max(ans+mx,maxi);
    }
    printf("%.8lf",maxi*PI);
}

int main(){
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++){
        printf("Case #%d: ",i);
        process();
        puts("");
    }
}
