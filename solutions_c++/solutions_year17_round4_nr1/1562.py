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

int arr[105];

void process(){
    memset(arr,0,sizeof(arr));
    int n,p;
    scanf("%d %d",&n,&p);
    for(int i = 0 , tmp; i < n ; i++){
        scanf("%d",&tmp);
        arr[tmp%p]++;
    }
    int ans = arr[0];
    if(p==2){
        ans += (arr[1]+1)/2;
    }
    if(p==3){
        int mini = min(arr[1],arr[2]);
        int maxi = max(arr[1],arr[2]);
        ans += mini + (maxi-mini+2)/3;
    }
    if(p==4){
        int mini = min(arr[1],arr[3]);
        ans += mini;
        ans += arr[2]/2;
        arr[1] -= mini;
        arr[2] %= 2;
        arr[3] -= mini;
        if(arr[1]){
            if(arr[2]){
                if(arr[1]>=2){
                    ans++;
                    arr[1]-=2;
                }
            }
            ans += (arr[1]+3)/4;
        }
        if(arr[3]){
            if(arr[2]){
                if(arr[3]>=2){
                    ans++;
                    arr[3]-=2;
                }
            }
            ans += (arr[3]+3)/4;
        }
    }
    printf("%d",ans);
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
