#include<bits/stdc++.h>
#define inf 0x3f3f3f3f
#define mp make_pair
#define pb push_back
#define MAX_BITS 1000
using namespace std;

int T, N, K;

int main(){
    cin >> T;
    for(int t = 1; t <= T;t++){
        cin >> N >> K;
        priority_queue<int>pq;
        int ret;
        pq.push(N);
        for(int k = 0;k < K && !pq.empty();k++){
            int best = pq.top();
            ret = best;
            pq.pop();
            if(best % 2 == 0){
                pq.push(best/2);
                pq.push(best/2-1);
            }else{
                pq.push(best/2);
                pq.push(best/2);
            }
        }
        int max_lr =0, min_lr=0;
        if(ret % 2 == 0 && ret != 0){
            max_lr = max(ret/2, ret/2-1);
            min_lr = min(ret/2, ret/2-1);
        } else{
            max_lr = max(ret/2, ret/2);
            min_lr = min(ret/2, ret/2);
        }
        cout << "Case #" << t << ": " << max_lr << " " << min_lr  << endl;
    }
    return 0;
}
