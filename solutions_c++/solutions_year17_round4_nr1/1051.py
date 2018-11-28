#include <bits/stdc++.h>
using namespace std;
void solve() {
    int n,p;
    int arr[5] = {0,0,0,0,0};
    scanf("%d %d",&n,&p);
    for(int i = 0;i < n;i++) {
        int x;
        scanf("%d",&x);
        arr[x%p]++;
    }
    int ans = arr[0];
    if(p==2) {
        // match even
        ans += arr[1]/2;
        if(arr[1] % 2 == 1) ans++; // fresh last
    }
    else if(p == 3) {
        while(arr[1] > 0 && arr[2] > 0) {
            ans++;
            arr[1]--;
            arr[2]--;
        }
        ans += arr[1]/3; arr[1] %= 3;
        ans += arr[2]/3; arr[2] %= 3;
        if(arr[1]>0 || arr[2]>0) ans++;
    }
    else {
        int tans = 0;
        int tmp1 = arr[1];
        int tmp2 = arr[2];
        int tmp3 = arr[3];
        while(tmp3 >= 0) {
            // check this
            // match 3 with 1
            while(tmp3 > 0 && tmp1 > 0) {
                tans++;
                tmp3--;
                tmp1--;
            }
            // match 2 2
            while(tmp2 >= 2) {
                tans++;
                tmp2-=2;
            }
            // 2 1 1
            while(tmp2 > 0 && tmp1 >= 2) {
                tans++;
                tmp2--;
                tmp1 -= 2;
            }
            tans += tmp3/4;
            tans += tmp1/4;

            tmp3 = arr[3]-2;
            arr[3]-=2;
            ans = max(ans,ans+tans);
        }
    }
    printf("%d\n",ans);
}
int main() {
    int tt;
    scanf("%d",&tt);
    for(int i = 0;i < tt;i++) {
        printf("Case #%d: ",i+1);
        solve();
    }
}
