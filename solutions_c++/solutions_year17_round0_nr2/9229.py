#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

ll T,N,tmp,ans,mx,cur;

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small.txt", "w", stdout);

    cin >> T;

    for(ll tc=0;tc<T;tc++){
        cin >> N;

        for(ll i=N;i>0;i--){
            bool fail = false;
            tmp = ans = i;
            mx = tmp%10; tmp/=10;

            while(tmp>0 && !fail){
                cur = tmp%10; tmp/=10;
                if(cur<=mx){
                    mx = cur;
                }
                else fail = true;
            }
            if(!fail){
                cout << "Case #" << tc+1 << ": " << ans << '\n';
                break;
            }
        }
    }

    return 0;
}
