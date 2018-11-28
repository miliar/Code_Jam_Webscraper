#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;

inline bool all_happy(string ps) {
    for (char p : ps) { if (p == '-') return false; }
    return true;
}

inline string flip(string ps, int i, int K) {
    string flipped(ps);
    for (int j = i; j < i + K; j++) {
        flipped[j] = (ps[j] == '+') ? '-' : '+';
    }
    return flipped;
}

string pancake(string pancakes, int K) {
    const int N = pancakes.size();
    unordered_set<string> visited;
    unordered_map<string, string> parent;
    queue<string> q;
    q.emplace(pancakes);

    while (!q.empty()) {
        string top = q.front();
        q.pop();
        if (all_happy(top)) {
            int num_flips = 0;
            string curr = top;
            while (parent.find(curr) != parent.end()) {
                num_flips++;
                curr = parent[curr];
            }
            return to_string(num_flips);
        }
        for (int i = 0; i <= N - K; i++) {
            string neighbor = flip(top, i, K);
            if (visited.find(neighbor) == visited.end()) {
                q.emplace(neighbor);
                visited.emplace(top);
                parent.emplace(neighbor, top);
            }
        }
    }
    return "IMPOSSIBLE";
}

int main(int argc, char *argv[]) {
    int T; cin >> T; int case_no = 1;
    string S; int K;
    while (T--) {
        cin >> S; cin >> K;
        cout << "Case #" << case_no++ << ": ";
        cout << pancake(S, K) << endl;
    }
}
