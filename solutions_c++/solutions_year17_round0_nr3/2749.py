//0. at most two (x and x + 1) values in each level if we
//   process the level before the sub problems
//1. larger length => better solution.
//proof for 0 and 1
//   a. 2n + 1 2n + 2, n >= 0
//      2n + 1 => n, 1, n min(n, n) = n, max(n, n) = n
//      2n + 2 => n, 1, n + 1 (left before right)
//                        min(n, n+1) = n, max(n, n+1) = n + 1
//      sub problems: n and n + 1 
//      min(n, n + 1) == min(n, n), but max(n, n + 1) > max(n, n)
//      so 2n + 2 better than 2n + 1
//   b. 2n + 2 2n + 3, n >= 0
//      2n + 2 => n, 1, n + 1
//      2n + 3 => n + 1, 1, n + 1
//      sub probems: n and n + 1
//      min(n + 1, n + 1) > min(n, n + 1). so 2n + 3 is better than 2n + 2
//  so keep two values x and x + 1 always.
//  so x is better than x + 1. x + k better x + k - 1 better x + k - 2 ... y
//  if x > y
//
//3. we can process current level before sub problems.
//  we should remove mid, so at least remove one
//  if single x, sub <= x - 1. process x then sub. (see 1)
//  if x, x + 1. x -> sub1 <= x - 1. x + 1 => sub2 <= x
//      there is only one optimal min(ls, rs) and max(ls, rs) pair for 
//      each length. so we can process the x-sub-problem later.
//
#include <cassert>

#include <iostream>
#include <stdint.h>
#include <algorithm>
#include <map>


using namespace std;

typedef int64_t ll; //PRId64 SCNd64

void split(ll x, ll &ls, ll &rs)
{
    if(x > 0){
        ll mid = (x - 1)/2; //(0 + x - 1)/2
        ls = mid - 0;
        rs = x - 1 - mid;
    }
}
int main(int argc, char **argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0), cout.precision(15);
    int T;
    cin >> T; //1 100
    for(int cas = 1; cas <= T; cas ++){
        ll N, K; //N 1 1e18 K 1 N
        cin >> N >> K;
        map<ll, ll> mp;
        mp[N] = 1; // N > 0
        ll s = 0;
        ll ls = 0, rs = 0;
        while(mp.size()){
            map<ll, ll> tmp;
            for(map<ll, ll>::reverse_iterator it = mp.rbegin(); it != mp.rend(); it++){
                ll x = it->first;
                ll cnt = it->second;
                ll need = K - s;
                split(x, ls, rs);
                if(cnt >= need){
                    tmp.clear();
                    break;
                }
                //double cnt since x > 0
                tmp[ls] += cnt;
                tmp[rs] += cnt;
                s += cnt; // cnt < need = K - s => s + cnt < K 2*cnt < 2*K<=2e18
            }
            //double sum of cnt of map in each loop. 1 + 2 + 2^2 + ... <= K 
            if(tmp.empty()){
                break;
            }
            //keep len > 0
            if(tmp.begin()->first == 0){
                tmp.erase(tmp.begin());
            }
            swap(mp, tmp);
            assert(mp.size() <= 2);
        }
        cout << "Case #" << cas << ": " << max(ls, rs) << " " << min(ls, rs) << endl;
    }
    return 0;
}
