#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <sstream>
#include <list>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <limits>
#include <map>
#include <istream>

using namespace std;

/*
long long tidy_num(long long N) {
    if (N < 10) return N;

    vector<int> nums;
    long long temp = N;

    while (temp) {
        nums.push_back(temp % 10);
        temp /= 10;
    }

    reverse(nums.begin(), nums.end());
    for (int i = 1; i < nums.size(); ++i) {
        if (nums[i] < nums[i - 1]) {
            --nums[i - 1];
            for (int j = i - 2; j >= 0; --j) {
                if (nums[j] > nums[j + 1]) {
                    --nums[j];
                    i = j + 1;
                }
            }

            for (int j = i; j < nums.size(); ++j) {
                nums[j] = 9;
            }
            break;
        }
    }

    temp = 0;
    for (int i = 0; i < nums.size(); ++i) {
        temp *= 10;
        temp += nums[i];
    }

    return temp;
}
*/

vector<long long> bathroom(long long N, long long K) {
    vector<long long> res(2, 0);
    map<long long, long long> cons_len;
    long long ls       = N;
    long long rs       = N;
    long long max_len  = 0;
    long long cur      = 0;
    long long temp     = 0;

    if (N == K) return res;
    //if (K % 2 && (K > N / 2 + 1)) return res;
    //else if (K % 2 == 0 && K > N / 2) return res;

    cons_len[0]  = N;

    for (long long i = 0; i < K; ++i) {
        auto it = cons_len.begin();
        max_len = 0;
        cur     = 0;
        for (; it != cons_len.end(); ++it) {
            if (it->second > max_len) {
                max_len = it->second;
                cur = it->first;
            }
        }

        temp = cur;

        if (max_len % 2) {
            cur += max_len / 2 + 1;
            ls   = max_len / 2;
            rs   = ls;
        }
        else {
            cur += max_len / 2;
            ls = max_len / 2 - 1 ? max_len / 2 - 1 : 0;
            rs = max_len / 2;
        }
        cons_len[temp] = ls;
        cons_len[cur] = rs;
    }

    res[0] = max(ls, rs);
    res[1] = min(ls, rs);

    return res;
}

vector<long long> bath(priority_queue<long long> &q, long long K) {
    long long len = q.top();

    q.pop();

    if (K <= 1) {
        long long min_len, max_len;

        max_len = len / 2;
        if (len % 2) {
            min_len = len / 2;
        }
        else {
            min_len = len / 2 - 1 > 0 ? len / 2 - 1 : 0;
        }

        return {max_len, min_len};
    }

    if (len % 2) {
        if (len > 1) {
            q.push(len / 2);
            q.push(len / 2);
        }
        return bath(q, K - 1);
    }
    else {
        if (len / 2 - 1 > 0) {
            q.push(len / 2 - 1);
        }
        q.push(len / 2);

        return bath(q, K - 1);
    }
}

vector<long long> bathroom2(long long N, long long K) {
    vector<long long> res(2, 0);
    priority_queue<long long> q;

    //if (K % 2 && (K > N / 2 + 1)) return res;
    //else if (K % 2 == 0 && K > N / 2) return res;

    q.push(N);

    return bath(q, K);
}

int main(int argc, char **argv) {
    int n;
    long long N;
    long long K;

    vector<long long> res;

    //res = bathroom2(10, 7);
    //cout<< res[0]<< " "<< res[1]<< endl;
    cin>> n;
    for (int i = 1; i <= n; ++i) {
        cin>> N >> K;
        res = bathroom2(N, K);
        cout<< "Case #"<< i<< ": "<< res[0]<< " "<< res[1]<< endl;
    }

    return 0;
}
