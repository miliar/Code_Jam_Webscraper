#include<iostream>
#include<algorithm>
#include<queue>
#include<map>
using namespace std;
#define LL long long
#define PL pair<LL, LL>
int main(){
    int t;
    cin >> t;
    LL n, k;
    for(int i = 0; i < t; i++){
        cin >> n >> k;

        map<LL, LL> mp;
        LL ans = n;
        mp[ans] = 1;
        while(k > 0){

            PL p = *mp.rbegin();
            LL range = p.first;
            LL num = p.second;
            mp.erase(range);
            k -= num;
            ans = range;
            range--;
            if(range == -1)
                break;
            if(range % 2ll == 0)
                mp[range / 2ll] += num * 2ll;
            else{
                mp[range / 2ll] += num;
                mp[range / 2ll + 1ll] += num;
            }

        }

        ans--;
        cout << "Case #" << i + 1 << ": ";
        if(ans % 2ll == 0){
            cout << ans / 2ll << " " << ans / 2ll << endl;
        }else{
            cout << ans / 2ll + 1ll << " " << ans / 2ll << endl;
        }

    }

    return 0;
}
