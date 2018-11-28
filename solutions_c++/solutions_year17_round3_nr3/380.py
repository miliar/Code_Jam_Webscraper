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

double arr[55];

void process(){
    int n, k;
    double u;
    scanf("%d %d %lf",&n,&k,&u);
    for(int i = 0 ; i < n ; i++){
        scanf("%lf",arr+i);
    }
    double l = 0, h = 1;
    for(int i = 0 ; i <= 10000 ; i++){
        double mid = (l+h)/2 , uu = 0;
        for(int i = 0 ; i < n ; i++){
            if(arr[i]<mid){
                uu += mid - arr[i];
            }
        }
        if(uu>u){
            h = mid;
        }
        else l = mid;
    }
    double ans = 1;
    for(int i = 0 ; i < n ; i++){
        if(arr[i] < l) ans *= l;
        else ans *= arr[i];
    }
    printf("%.10lf",ans);
}

int main(){
    //freopen("input.txt","rt",stdin);
    //freopen("output.txt","wt",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++){
        printf("Case #%d: ",i);
        process();
        puts("");
    }
}
