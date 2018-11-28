#include <bits/stdc++.h>
#include <cstring>
#include <cassert>

using namespace std;

typedef unordered_map <long long, long long> LLMapType;

long long sumUp(LLMapType mp) {
    long long sum = 0;
    for (auto item: mp) {
        sum += item.second;
    }
    return sum;
}

long long getNewN(long long n, long long k) {
    LLMapType cnt;
    cnt[n] = 1LL;
    while (sumUp(cnt) < k) {
        k -= sumUp(cnt);
        LLMapType newCnt;
        newCnt.clear();
        for (auto item: cnt) {
            long long u = item.first / 2;
            long long v = (item.first - 1) / 2;
            if (newCnt.find(u) == newCnt.end()) {
                newCnt[u] = 0;
            }
            if (newCnt.find(v) == newCnt.end()) {
                newCnt[v] = 0;
            }
            newCnt[u] += item.second;
            newCnt[v] += item.second;
        }
        cnt.clear();
        cnt = newCnt;
        assert(cnt.size() <= 2);
    }
    vector< pair<long long, long long> > vec;
    for (auto item: cnt) {
        vec.push_back(item);
    }
    sort(vec.begin(), vec.end());
    if (vec.size() == 1) {
        return vec[0].first;
    }
    assert(vec.size() == 2);
    if (vec[1].second < k) {
        return vec[0].first;
    }
    return vec[1].first;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int caseCnt;
    cin >> caseCnt;
    int caseNow = 0;
    while (caseNow < caseCnt) {
        ++caseNow;
        long long n, k;
        cin >> n >> k;
        n = getNewN(n, k);
        cout << "Case #" << caseNow <<": " << n / 2LL  << " " << (n - 1) / 2LL << endl;
    }
    return 0;
}
