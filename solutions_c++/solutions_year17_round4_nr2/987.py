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
#define MAX 10000
#define f first
#define s second
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int arr[1005][1005];

void process(){
    memset(arr, 0, sizeof(arr));
    int n,c,m;
    scanf("%d %d %d",&n,&c,&m);
    int ans1 = 0, ans2 = 0;
    for(int i = 0 ; i < m ; i++){
        int p,b;
        scanf("%d %d",&p,&b);
        arr[p][b]++;
        arr[1001][b]++;
        arr[p][1001]++;
        ans1 = max(ans1,arr[1001][b]);
    }
    ans1 = max(ans1,arr[1][1001]);
    for(int i = 1 ; i <= 1000 ; i++){
        ans2 = max(ans2,arr[i][1001]-ans1);
    }
    printf("%d %d",ans1,ans2);
}

int main(){
    //freopen("input.txt","rt",stdin);
    //freopen("output.txt","wt",stdout);
    int t;
    scanf("%d\n",&t);
    for(int i = 1 ; i <= t ; i++){
        printf("Case #%d: ",i);
        process();
        puts("");
    }
}
