#include <bits/stdc++.h>

#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef long long ll;

int v[105];

int main(){
    int T,n,p;

    scanf("%d", &T);

    for(int t = 1; t <= T; t++){
        scanf("%d%d", &n, &p);

        for(int i = 0; i < n; i++)
            scanf("%d", &v[i]);
        
        int ans = 0;
        if(p == 2){
            int odd = 0, even = 0;
            for(int i = 0; i < n; i++)
                if(v[i]&1) odd++;
                else even++;

            ans = even + (odd+1)/2;
        }
        else if(p == 3){
            int cnt[3] = {0};
            for(int i = 0; i < n; i++)
                cnt[v[i]%3]++;
            
            ans = cnt[0];
            int tmp = min(cnt[1], cnt[2]);

            ans += tmp;
            cnt[1] -= tmp; cnt[2] -= tmp;

            tmp = cnt[1] + cnt[2];
            for(int i = 0; i < tmp; i++)
                if(i%3 == 0) ans++;
        }

        printf("Case #%d: %d\n",t,ans);
    }
    
    return 0;
}