#include <bits/stdc++.h>
using namespace std;
#define PB push_back
typedef long long ll;
typedef long double ld;
const ll INF = ll(1e18);
ll T, N, M, K;

struct Node {
    ld R;
    ld H;
} ;

bool operator >(const Node& x, const Node& y) {
    return x.R * x.H > y.R * y.H;
}

ld calculate(auto& arr, int x) {
    ld ans = 0;
    Node bottom {0, 0};
    for (int i = 0; i < K; ++i) {
        ans += 2 * M_PI * arr[x+i].R * arr[x+i].H;
        if (arr[x+i].R > bottom.R)
            bottom = arr[x+i];
    }
    ans += M_PI * bottom.R * bottom.R;
    return ans;
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N >> K;
        vector<Node> arr(N);
        for (int i = 0; i < N; ++i)
            cin >> arr[i].R >> arr[i].H;
        sort(arr.begin(), arr.end(), greater<Node>());

        ld res = 0, sum = 0, ns;
        Node bottom {0, 0};
        for (int i = 0; i < K; ++i) {
            sum += 2 * M_PI * arr[i].R * arr[i].H;
            if (arr[i].R > bottom.R)
                bottom = arr[i];
        }
        res = M_PI * bottom.R * bottom.R + sum;

        for (int i = 0; i < K; ++i) {
            ns = sum - 2 * M_PI * arr[i].R * arr[i].H;

            Node bottom {0, 0};
            for (int j = 0; j < K; ++j)
                if (arr[j].R > bottom.R && j != i)
                    bottom = arr[j];

            for (int j = K; j < N; ++j) {
                Node nb = bottom;
                if (arr[j].R > nb.R)
                    nb = arr[j];
                res = max(res, ns + 2 * M_PI * arr[j].R * arr[j].H + M_PI * nb.R * nb.R);
            }
        }

        printf("Case #%d: %.9Lf\n", t, res);
    }

    return 0;
}
