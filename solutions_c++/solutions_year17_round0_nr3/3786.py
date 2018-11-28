#include <iostream>
#include <vector>
#include <tuple>
#include <math.h>
#include <queue>

using namespace std;

tuple<int, int, int> findBestInSlow(vector<bool> &stalls) {
    int best = 0;
    int minOfLSRS = 0;
    int maxOfLSRS = 0;
    for (int i = 1; i < stalls.size() - 1; i++) {
        if (!stalls[i]) {
            int j = i - 1;
            int countLeft = 0;
            while(!stalls[j]) {
                countLeft++;
                j--;
            }
            j = i + 1;
            int countRight = 0;
            while(!stalls[j]) {
                countRight++;
                j++;
            }

            int minn = min(countLeft, countRight);
            int maxx = max(countLeft, countRight);

            if (minn > minOfLSRS || (minn == minOfLSRS && maxx > maxOfLSRS)) {
                best = i;
                minOfLSRS = minn;
                maxOfLSRS = maxx;
            }
        }
    }
    return make_tuple(best, minOfLSRS, maxOfLSRS);
}

tuple<long, long> stallsSlow(long N, int K) {
    vector<bool> stalls(N + 2, false);
    stalls[0] = true;
    stalls[N + 1] = true;
    int loc, m, mm;
    for (int i = 0; i < K - 1; i++) {
        tie (loc, m, mm) = findBestInSlow(stalls);
        stalls[loc] = true;
    }
    tie (loc, m, mm) = findBestInSlow(stalls);
    return make_tuple(mm, m);
}

tuple<long, long> stallsMedium(long N, long K) {
    priority_queue<int> q;
    q.push(N);
    for (int i = 0; i < K - 1; i++) {
        int a = q.top();
        q.pop();
        a -= 1;
        if (a > 0) {
            int b = a / 2;
            int c = a - b;
            q.push(c);
            if (b>0) q.push(b);
            //cerr << a << " = " << c << " = " << b << endl;
        }
    }
    int a = q.top() - 1;
    int b = a / 2;
    int c = a - b;
    return make_tuple(c, b);
}

int main() {
    int tests;
    long N, K;
    cin >> tests;
    for (int i = 0 ; i < tests; i++) {
        cin >> N >> K;
        tuple<long, long> res = stallsMedium(N, K);
        cout << "Case #" << (i + 1) << ": " << get<0>(res) << " " << get<1>(res) << endl;
        //res = stallsSlow(N, K);
        //cout << "A: Case #" << (i + 1) << ": " << get<0>(res) << " " << get<1>(res) << endl;
    }
}