#include<cstdio>
#include<cstring>
#include<queue>

using std::queue;

int position[11] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};

struct state final {
    int pancakes;
    int moves;
};

int flip(int x, int start, int k) {
    int res = x;
    for (int i = 0; i < k; ++i) {
        int p = start + i;
        if ((x & (1 << p)) == 0) {
            res |= (1 << p);
        } else {
            res &= ~(1 << p);
        }
    }
    return res;
}

int main() {
    int t;
    scanf("%d", &t);
    int case_no = 0;
    char s[11];
    int k;
    size_t n;
    bool visited[1024];
    do {
        ++case_no;
        scanf("%10s %d", s, &k);
        n = strlen(s);
        queue<state> q;
        for (size_t i = 0; i < 1024; ++i) {
            visited[i] = false;
        }
        int starting_state = 0;
        int full = position[n] - 1;
        for (size_t i = 0; i < n; ++i) {
            if (s[i] == '+')
                starting_state += position[i];
        }
        q.push({starting_state, 0});
        visited[starting_state] = true;
        int result = -1;
        if (starting_state == full) {
            result = 0;
        } else {
            size_t end = n - k;
            while (!q.empty()) {
                state curr = q.front();
                q.pop();
                for (size_t start = 0; start <= end; ++start) {
                    int next = flip(curr.pancakes, start, k);
                    if (next == full) {
                        result = curr.moves + 1;
                        goto finish;
                    }
                    if (!visited[next]) {
                        visited[next] = true;
                        q.push({next, curr.moves + 1});
                    }
                }
            }
        }

        finish:
        if (result == -1) {
            printf("Case #%d: IMPOSSIBLE\n", case_no);
        } else {
            printf("Case #%d: %d\n", case_no, result);
        }
    } while (case_no != t);
    return 0;
}
