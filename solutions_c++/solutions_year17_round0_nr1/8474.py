#include <iostream>
#include <unordered_map>
#include <bitset>
#include <set>
#include <string>
#include <queue>

using namespace std;

const size_t MAX_S = 10;
typedef bitset<MAX_S> state;


state string2bitset(const string& str_state) {
    auto cur = str_state.cbegin();
    state result;
    for (int i = 0; i < str_state.size(); ++i, ++cur) {
        if(*cur == '+') {
            result.set(i);
        }
    }

    return result;
}

int bfs(const state& start, const state& target, const int Slen, const int K) {
    unordered_map<state, int> visited;
    queue<state> state_queue;

    visited.insert(make_pair(start, 0));
    state_queue.push(start);

    cerr << start.to_string() << endl;
    cerr << target.to_string() << endl;

    while(state_queue.size() > 0) {
        state cur = state_queue.front();
        state_queue.pop();
        cerr << "P:" << cur.to_string() << endl;

        if(cur == target) {
            return visited[cur];
        }


        for (int s = 0; s <= Slen-K; ++s) {
            state next = cur;
            for (int k = 0; k < K; ++k) {
                next.flip(s+k);
            }
            cerr << next.to_string() << endl;

            if(visited.find(next) == visited.end()) {
                cerr << "A:" << next << endl;
                state_queue.push(next);
                visited.insert(make_pair(next, visited[cur]+1));
            }
        }
    }

    return -1;
}

int main() {

    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {
        string S;
        cin >> S;
        int K;
        cin >> K;

        cerr << "S: " << S.length() << ", K: " << K << endl;

        //Create target state
        state target;
        for (int i = 0; i < S.length(); ++i) {
            target.set(i);
        }

        state start = string2bitset(S);
        int result = bfs(start, target, S.length(), K);

        //Print result
        cout << "Case #" << t+1 << ": ";
        if(result >= 0) {
            cout << result;
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;

    }

    return 0;
}