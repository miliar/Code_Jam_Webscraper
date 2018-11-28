#include <stdio.h>
#include <string.h>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#define f first
#define s second
#define mp make_pair
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

int dx[4] = {0,0,1,-1}, dy[4] = {1,-1,0,0};

void process(){
    double d;
    int n;
    scanf("%lf %d",&d, &n);
    double mt = 0;
    for(int i = 0 ; i < n ; i++){
        double k,s;
        scanf("%lf %lf",&k,&s);
        mt = max(mt,(d-k)/s);
    }
    printf("%.8lf",d/mt);
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
