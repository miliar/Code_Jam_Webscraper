#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<cmath>
#include<cstring>
using namespace std;

int main (){
    int T;
   // freopen("A-large.in","r",stdin);
   // freopen("ALout.txt","w",stdout);
    cin >> T;
    for(int ca=1;ca<=T;ca++){
        int N,P;
        int cnt[5];
        for(int i=0;i<4;i++)cnt[i] = 0;
        cin >> N >>P;
        for(int i=0;i<N;i++){
            int a;
            cin >> a;
            cnt[a % P]++;
        }
        int ans = 0;
        if(P == 2){
            ans = cnt[0];
            ans += cnt[1] / 2;
            cnt[1] %= 2;
            ans += cnt[1];
        }else if(P == 3){
            ans = cnt[0] + min(cnt[1],cnt[2]);
            int b =  min(cnt[1],cnt[2]);
            cnt[1]-=b;
            cnt[2]-=b;
            ans += cnt[1] / 3;
            cnt[1] %= 3;
            ans += cnt[2] / 3;
            cnt[2] %= 3;
            if(cnt[1]+cnt[2] > 0)ans++;
        }else if(P == 4){
            ans = cnt[0];
            int b = min(cnt[1],cnt[3]);
            cnt[1] -=b;
            cnt[3] -=b;
            ans += b;

            ans += cnt[2] / 2;
            cnt[2] %= 2;

            ans += cnt[1] / 4;
            cnt[1] %= 4;

            ans += cnt[3] / 4;
            cnt[3] %= 4;

            if(cnt[2]*2 + cnt[1] + cnt[3] >= 4){
                cnt[2] = 0;
                if(cnt[1] > 0)cnt[1]-=2;
                if(cnt[3] > 0)cnt[3]-=2;
                ans++;
            }

            if(cnt[1]+ cnt[2] +cnt[3] >0)ans++;

        }
        cout <<"Case #" << ca <<": " << ans <<"\n";
    }
    return 0;
}
