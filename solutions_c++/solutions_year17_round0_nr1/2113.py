#include <iostream>
#include <vector>
using namespace std;

#define INP "A-large.in"
#define OUT "output.txt"


void update(vector<int> &tree, int i, int v) {
    if (i >= tree.size()) {
        return;
    } else {
        tree[i] += v;
        update(tree, i + (i&-i), v);
    }
}

int get(vector<int> &tree, int i) {
    if (i == 0) {
        return 0;
    } else {
        return tree[i] + get(tree, i - (i&-i));
    }
}

int main(int argc, char const *argv[])
{
    freopen(INP, "r", stdin);
    freopen(OUT, "w", stdout);

    int n_tests;
    cin >> n_tests;
    for (int test = 1; test <= n_tests; ++test) {
        // Read inputs
        string S;
        int K;
        cin >> S >> K;

        // Initialize BIT
        vector<int> tree(S.length(), 0);

        // Solve
        int n_changes = 0;
        for (int i = 0; i + K - 1 < S.length(); ++i) {
            int state = ((S[i] == '+') + get(tree, i)) & 1;
            if (!state) {
                update(tree, i + 1, 1);
                update(tree, i + K, -1);
                ++n_changes;
            }
        }

        // Verify
        bool ok = true;
        for (int i = S.length() - K + 1; i < S.length(); ++i) {
            ok &= ((S[i] == '+') + get(tree, i)) & 1;
        }

        if (ok) {
            cout << "Case #" << test << ": " << n_changes << endl;
        } else {
            cout << "Case #" << test << ": IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
