#include <bits/stdc++.h>
using namespace std;
#define mp(X,Y) make_pair(X,Y)
#define F first
#define S second
typedef long long ll;
typedef pair<int,int> PII;
typedef pair<ll,ll> PLL;

PII Cam[110];
PII Jam[110];
int color[2010];

int main(){
    ios::sync_with_stdio(0);
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    int cas = 1;
    int t;
    cin >> t;
    while(t--){
        cout << "Case #" << cas ++ << ": ";
        int x,y;
        cin >> x >> y;
        for(int i = 0 ;i <2010; i ++){
            color[i] = 0;
        }
        if(x == 0 && y == 0){
            cout << 2 << endl;
            continue;
        }
        int L,R;
        int tot = 24 * 60;
        int leftx = 720;
        int lefty = 720;
        for(int i = 0 ;i < x; i ++){
            cin >> L >> R;
            L %= tot;
            R %= tot;
            while(L != R){
                color[L] = 1;
                L++;
                lefty --;
                L %= tot;
            }
        }
        for(int i = 0 ;i <y ; i ++){
            cin >> L >> R;
            L %= tot;
            R %= tot;
            while(L != R){
                color[L] = 2;
                L++;
                leftx--;
                L %= tot;
            }
        }
        int ans = 0;
        int inseg = 0;
        vector<int>vecx,vecy;
        for(int i = 0; i < tot ; i++){
            if(!color[i]){
                L = i ; R= i + 1;
                while(color[L] == 0){
                    color[L] = 3;
                    L--;
                    L = (L + tot) % tot;
                }
                while(color[R] == 0){
                    color[R] = 3;
                    R ++;
                    R %= tot;
                }
                if(color[L] != color[R]){
                    //cout << L <<" " << R <<endl;
                    inseg ++;
                }else{
                    if(color[L] == 1){
                        vecy.push_back((R-L-1+tot)%tot);
                    }else{
                        vecx.push_back((R-L-1+tot)%tot);
                    }
                }
            }else if(color[i] < 3 && color[(i+1)%tot] < 3 && color[(i+1)%tot]!=0){
                if(color[i] != color[(i +1 ) % tot]){
                    //cout << L << " " <<R <<endl;
                    inseg ++;
                }
            }
        }
        ans = inseg;
        //cout << ans << endl;
        sort(vecx.begin(),vecx.end());
        sort(vecy.begin(),vecy.end());
        int cur = 0;
        int sz = vecx.size();
        while(leftx && cur < sz){
            if(leftx >= vecx[cur]){
                leftx -= vecx[cur];
                cur++;
            }else{
                break;
            }
        }
        ans += 2 * (sz - cur);
        cur = 0;
        sz = vecy.size();
        //cout << "Y : " << vecy[cur] <<endl;
        while(lefty && cur <sz){
            if(lefty >= vecy[cur]){
                lefty -= vecy[cur];
                cur++;
            }else{
                break;
            }
        }
        ans += 2 * (sz - cur);
        cout <<ans <<endl;



    }
    return 0;
}
