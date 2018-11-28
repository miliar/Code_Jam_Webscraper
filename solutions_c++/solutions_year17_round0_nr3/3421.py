#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef string sg;
typedef long long ll;
int main(){
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for(int i = 1;i <= T;i++){
        ll n,k;
        cin >> n >> k;
        int deg = 0;
        while( (1<<deg) < k){
            deg++;
        }
        if( (1<<deg) > k) deg--;
        int pow2 = (1<<deg);
        ll num = (n - pow2 + 1) % pow2;
        int ans = (n - pow2 + 1) / pow2;
        if(k < pow2 + num) ans++;
        ans--;
        int ansl = ans/2 + ans%2,ansr = ans/2;
        printf("Case #%d: %d %d\n",i,ansl,ansr);
    }
    return 0;
}
