#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <queue>
#include <stack>
#include <cstring>

using namespace std;

priority_queue<long long> q;

int main(){
    int T; cin >> T;
    for(long long i = 1; i <= T; i++){
        long long N, K; cin >> N >> K;
        cout << "Case #" << i << ": ";
        long long top = 0;
        q.push(N);

        while(K--){
            top = q.top(); q.pop();
            if(top & 1){
                q.push(top/2);
                q.push(top/2);
            }
            else{
                q.push(top/2 -1);
                q.push(top/2);
            }
        }
        while(!q.empty()) q.pop();
        long long ans1, ans2;
        if(top & 1){
            ans1 = top/2;
            ans2 = top/2;
        }
        else {
            ans1 = top/2;
            ans2 = top/2 - 1;
        }
        cout << ans1 << " " << ans2 << endl;
    }
}
