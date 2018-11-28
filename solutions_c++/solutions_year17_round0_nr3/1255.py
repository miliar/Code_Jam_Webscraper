#include<iostream>
#include<string>
#include<bitset>
#include<queue>
#include<map>

using namespace std;

typedef long long ll;
typedef pair<long long, long long> pll;

long long t, n, k;

struct Solution {
    ll stall;
    ll ls;
    ll rs;
    bool dirty;
    Solution *left;
    Solution *right;
    Solution(ll s, Solution *l, Solution *r) {
        stall = s;
        left = l;
        right = r;
        clean();
    }
    void clean() {
        ls = stall - (left ? left->stall : 0) - 1;
        rs = (right ? right->stall : n + 1) - stall - 1;
        dirty = false;
    }
    string toString() {
        return "Solution [" + to_string(stall) + "] Left=" + to_string(left->stall) + " Right=" + to_string(right->stall);
    }
};
struct SolutionComparator {
    inline bool operator()(Solution *a, Solution *b) {
        ll amin = min(a->ls, a->rs), bmin = min(b->ls, b->rs);
        if (amin != bmin) {
            return bmin > amin;  // pick higher min
        }
        ll amax = max(a->ls, a->rs), bmax = max(b->ls, b->rs);
        if (amax != bmax) {
            return bmax > amax;  // pick higher max
        }
        return a->stall < b->stall;  // pick left one
    }
};

pll solve(ll n, ll k) {
    // prio q, pick them out make 2 new potentials and make neighbouring solutions dirty
    priority_queue<Solution*, vector<Solution*>, SolutionComparator> queue;
    Solution *guardLeft = new Solution(0, NULL, NULL);
    Solution *guardRight = new Solution(n+1, NULL, NULL);
    Solution *initial = new Solution((n + 1) / 2, guardLeft, guardRight);
    queue.push(initial);

    while (k > 1) {
        --k;
        Solution *s = queue.top(); queue.pop();
        while (s->dirty) {
            s->clean();
            queue.push(s);
            s = queue.top(); queue.pop();
        }
        // generate 2 new solutions between s.stall and s.left.stall and between s.stall and s.right.stall
        // add them to queue
        //if (n<5)cerr << s->toString() << endl;
        int delta = s->stall - s->left->stall;
        if (delta > 1) {
            Solution *newl = new Solution(s->left->stall + delta / 2, s->left, s);
            s->left->right = newl;
            queue.push(newl);
        }
        delta = s->right->stall - s->stall;
        if (delta > 1) {
            Solution *newr = new Solution(s->stall + delta / 2, s, s->right);
            s->right->left = newr;
            queue.push(newr);
        }
        s->left->dirty = true;
        s->right->dirty = true;
    }

    if (queue.empty()) return make_pair(0, 0);

    Solution *s = queue.top(); queue.pop();
    while (s->dirty) {
        s->clean();
        queue.push(s);
        s = queue.top(); queue.pop();
    }
   // cerr << "Final " << s->toString() << endl;
    return make_pair(max(s->ls, s->rs), min(s->ls, s->rs));
}

struct PllComparator {
    bool operator()(pll a, pll b) {
        return b.first > a.first;
    }
};

pll quicksolve(ll n, ll k) {
    map<ll, ll> sols;
    sols[n] = 1;  // sols[range_size] = number of ranges
    while (k>0) {
        pll next = make_pair(0,0);
        for (auto kvp : sols) {
            if (kvp.second == 0) {
                //sols.erase(kvp.first);
                continue;
            }
            if (kvp.first > next.first) {
                next = kvp;
            }
        }
        //cerr << "Next is " << next.first << " " << next.second << endl;
        ll rightRegion = next.first / 2;
        ll leftRegion = (next.first - 1) / 2;
        if (k <= next.second) {
            return make_pair(rightRegion, leftRegion);
        }
        else {
            k -= next.second;
            sols[next.first] = 0;
            if (rightRegion == leftRegion) {
                sols[rightRegion] += 2 * next.second;
            }
            else {
                sols[rightRegion] += next.second;
                sols[leftRegion] += next.second;
            }
        }
    }
    return make_pair(n / 2, (n + 1) / 2);
}

int main() {
    cin >> t;
    for (ll i = 1; i <= t; ++i) {
        cin >> n >> k;
        //pll s2 = solve(n, k);
        pll s = quicksolve(n, k);
        //if (s != s2) { cout << "FAILED "<<s2.first<< " " << s2.second<< " "; }
        cout << "Case #" << i << ": " << s.first << " " << s.second << endl;
    }
    return 0;
}
