#include <iostream>
#include <set>
#include <queue>

using namespace std;

struct Node {
    string state;
    int step;
    Node(string se, int sp) : state(se), step(sp) {}
};

string flip(string pre, int k, int s) {
    for (int i = s; i < s + k; i++) {
        if (pre[i] == '+') pre[i] = '-';
        else pre[i] = '+';
    }
    return pre;
}

int solve(string initial_state, int n, int k) {
    string final_state = "";
    for (int i = 0; i < n; i++) {
        final_state += "+";
    }
    if (initial_state == final_state) return 0;
    
    set<string> seen;
    queue<Node> que;
    Node first(initial_state, 0);
    que.push(first);
    while (!que.empty()) {
        Node cur = que.front();
        que.pop();
        for (int i = 0; i <= n - k; i++) {
            string next = flip(cur.state, k, i);
            if (seen.find(next) != seen.end()) {
                continue;
            }
            if (next == final_state) return cur.step + 1;
            seen.insert(next);
            Node nn(next, cur.step + 1);
            que.push(nn);
        }
    }
    return -1;
}

int main(int argc, const char * argv[]) {
    int T;
    scanf("%d", &T);
    for (int caseno = 0; caseno < T; caseno++) {
        char state[1001];
        int k;
        scanf("%s %d", state, &k);
        string str(state);
        int ans = solve(str, str.length(), k);
        printf("Case #%d: ", caseno + 1);
        if (ans == -1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}
