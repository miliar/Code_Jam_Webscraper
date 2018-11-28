#include <bits/stdc++.h>

using namespace std;
typedef long long int64;
#define DEBUG(x) cerr << #x << " = " << x << endl;
#define REP(x, n) for(__typeof(n) x = 0; x < (n); ++x)
#define FOR(x, b, e) for(__typeof(b) x = (b); x != (e); x += 1 - 2 * ((b) > (e)))
const int INF = 1000000001;
const double EPS = 10e-9;

struct Node {
    int size, best;
    Node *parent, *left, *right;

    Node(Node *p, int n) : size(n), best(n), parent(p), left(nullptr), right(nullptr) { }

    ~Node() {
        if (left != nullptr) {
            delete left;
        }
        if (right != nullptr) {
            delete right;
        }
    }
};

pair<int, int> visit(Node *node) {
    Node *it = node;
    while (it->left != nullptr) {
        if (it->left->best >= it->right->best) {
            it = it->left;
        } else {
            it = it->right;
        }
    }
    int left = (it->size - 1) / 2;
    int right = it->size - left - 1;
    it->left = new Node(it, left);
    it->right = new Node(it, right);
    while (it != nullptr) {
        it->best = max(it->left->best, it->right->best);
        it = it->parent;
    }
    return make_pair(max(left, right), min(left, right));
}

void print(Node *node, int depth) {
    cout << string(depth, ' ') << node-> size << " (" << node->best << ")\n";
    if (node->left != nullptr) {
        print(node->left, depth + 1);
        print(node->right, depth + 1);
    }
}

#ifndef CATCH_TEST
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

    int t;
    cin >> t;
    REP(o, t) {
        int64 n, k;
        cin >> n >> k;

        Node *node = new Node(nullptr, n);
        REP(x, k - 1) {
            visit(node);
        }
        auto res = visit(node);
        cout << "Case #" << o + 1 << ": " << res.first << " " << res.second << endl;

        // print(node, 0);

        delete node;
    }

	return 0;
}
#endif