#include <iostream>
#include <stdint.h>
#include <queue>
#include <utility>
using namespace std;

using l = int64_t;
using ll = pair<l,l>;


void do_case() {
    l N,K;
    cin >> N >> K;
    queue<ll> q;
    q.push({1LL,N});
    while(true) {
        ll current = q.front();
        q.pop();
        if(current.first >= K) {
            if(current.second%2LL==1LL) {
                cout << (current.second/2LL) << " " << (current.second/2LL) << endl;
            }
            else {
                cout << ((current.second/2LL)) << " " << max((current.second/2LL-1LL),0LL) << endl;
            }
            return;
        }
        K -= current.first;
        if(current.second % 2LL == 1LL) {
            l temp = current.second/2LL;
            if(q.back().second == temp) {
                q.back().first += 2LL*current.first;
            }
            else {
                q.push({current.first*2LL,temp});
            }
        }
        else {
            l tempmin = current.second/2LL -1LL;
            l tempmax = current.second/2LL;
            if(q.back().second == tempmax) {
                q.back().first += current.first;
            }
            else {
                q.push({current.first,tempmax});
            }
            q.push({current.first,tempmin});
        }
    }
    return;
}

int main() {
    int T;
    cin >> T;
    for(int i = 0; i<T; i++) {
        cout << "Case #" << i+1 << ": ";
        do_case();
    }
}
