#include<algorithm>
#include<cmath>
#include<iomanip>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<vector>
using namespace std;
using uint = unsigned int;
using ll = long long;
const int M = 1e9 + 7;
const ll MLL = 1e18L + 9;
#pragma unused(M)
#pragma unused(MLL)
#ifdef LOCAL
#include"rprint.hpp"
#else
template <class... T> void printl(T&&...){ }
template <class... T> void printc(T&&...){ }
template <class... T> void prints(T&&...){ }
template <class... T> void printd(T&&...){ }
#endif

int main(){
    int t; cin >> t;
    for(int i=1;i<=t;i++){
        cout << "Case #" << i << ": ";
        int n, p;
        cin >> n >> p;
        vector<int> rs(n);
        for(int i=0;i<n;i++){
            cin >> rs[i];
        }
        vector<vector<int>> qs(n, vector<int> (p));
        for(int i=0;i<n;i++){
            for(int j=0;j<p;j++){
                cin >> qs[i][j];
            }
            sort(qs[i].begin(), qs[i].end());
        }
        // prints(qs);
        vector<int> idxs(n), idxs2;
        int cnt = 0;
        while(idxs[0] < qs[0].size()){
            idxs2 = idxs;
            int idx = idxs[0];
            int num = 1;
            int r0 = rs[0], q0 = qs[0][idx];
            // other case??
            while(!(r0 * num * 0.9 - 1e-8 <= q0 && q0 <= r0 * num * 1.1 + 1e-8)){
                num++;
                if(q0 < r0 * num * 0.9 - 1e-8){
                    break;
                }
            }
            vector<int> nums;
            while(r0 * num * 0.9 - 1e-8 <= q0 && q0 <= r0 * num * 1.1 + 1e-8){
                nums.push_back(num);
                num++;
            }
            // printd(num);
            if(nums.empty()){
                idxs[0]++;
                continue;
            }
            bool ok2 = false;
            // prints(nums);
            // static int nnp = 0;
            // nnp += nums.size() * n * p;
            // prints(nums.size(), nums.size() * n * p, nnp);
            for(int h=0;h<nums.size();h++){
                bool ok = true;
                for(int i=1;i<n;i++){
                    int idx2 = idxs[i];
                    // double targ = 1.0 * qs[0][idx] / rs[0] * rs[i];
                    double targ = 1.0 * rs[i] * nums[h];
                    double tl = targ * 0.9 - 1e-8, tr = targ * 1.1 + 1e-8;
                    while(idx2 < qs[i].size() && !(tl <= qs[i][idx2] && qs[i][idx2] <= tr)){
                        idx2++;
                        if(qs[i][idx2] > tr){ break; }
                    }
                    if(idx2 < qs[i].size() && tl <= qs[i][idx2] && qs[i][idx2] <= tr){
                        idxs[i] = idx2;
                    }else{
                        ok = false;
                        break;
                    }
                }
                if(ok){
                    ok2 = true;
                    break;
                }else{
                    idxs = idxs2;
                }
            }
            if(ok2){
                // prints(idxs);
                cnt++;
                for(int& i : idxs){
                    i++;
                }
            }else{
                // idxs = idxs2;
                idxs[0]++;
            }
        }
        cout << cnt << '\n';
    }
    return 0;
}
