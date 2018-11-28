#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using Pair = pair<ll, ll>;
const ll MOD = 1000000007;


ll R[52];
ll Q[52][52];

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N, P;
        cin >> N >> P;

        for(int i=0;i<N;i++){
            cin >> R[i];
        }

        vector<priority_queue<Pair, vector<Pair>, greater<Pair>>> ques(N);
        for(int i=0;i<N;i++){
            for(int j=0;j<P;j++){
                cin >> Q[i][j];
                ll l = (Q[i][j] * 10 + R[i] * 11 - 1) / (R[i] * 11);
                ll r = (Q[i][j] * 10) / (R[i] * 9);
                // cout << "l " << l <<", r " << r << " " << Q[i][j] << endl;
                if(1 <= l && l <= r){
                    ques[i].emplace(l, r);
                }
            }
        }
        int ans = 0;
        while(ques[0].size()){
            auto p_0 = ques[0].top(); ques[0].pop();
            ll target = p_0.first;
            ll max_first = p_0.first;
            bool finish = false;
            for(int i=1;i<N;i++){
                while(ques[i].size() > 0 && ques[i].top().second < target) ques[i].pop();
                if(ques[i].size() == 0){
                    finish = true;
                    break;
                }
                max_first = max(ques[i].top().first, max_first);
            }
            if(finish) break;
            if(target == max_first){
                ans++;
                for(int i=1;i<N;i++){
                    ques[i].pop();
                }
            }else{
                if(max_first <= p_0.second){
                    ques[0].emplace(max_first, p_0.second);
                }
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}