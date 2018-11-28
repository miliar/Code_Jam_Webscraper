#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>

using namespace std;

typedef long long int lint;

void code() {
    lint N, K;
    cin >> N >> K;

    K--;

    set<lint> q;
    unordered_map<lint, lint> count;
    count[N] = 1;
    q.insert(-N);

    while (K) {
        lint top = -(*q.begin());
        lint num = count[top];

        if (num > K) {
            break;
        }

        K -= num;
        lint hi = top/2;
        lint lo = (top-1)/2;
        q.insert(-lo);
        q.insert(-hi);
        count[lo] += num;
        count[hi] += num;

        q.erase(q.begin());
    }

    lint top = -(*q.begin());
    lint hi = top/2;
    lint lo = (top-1)/2;

    cout << hi << " " << lo << endl;
}

int main() {
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        cout << "Case #" << i << ": ";
        code();
    }
}
