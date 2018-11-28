#include <bits/stdc++.h>

using namespace std;
long long n, k;

void output(long long cnt) {
    cnt = cnt - 1;
    cout << cnt - (cnt >> 1) << " " << (cnt >> 1) << endl;
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int T;
    cin >> T;
	for (int cas = 1; cas <= T; cas ++) {
        cin >> n >> k;
        printf("Case #%d: ", cas);
        long long cur = 0;
        map<long long, long long> kv;
        kv[n] = 1;
        while (true) {
            long long sum = 0;
			for (map <long long, long long> :: iterator it = kv.begin(); it != kv.end(); it ++) sum += it->second;
            if(cur + sum >= k) {
                vector < pair<long long, long long> > vec;
				for (map <long long, long long> :: iterator it = kv.begin(); it != kv.end(); it ++) {
                    vec.push_back(make_pair(it->first, it->second));
                }
                reverse(vec.begin(), vec.end());
                if(cur + vec[0].second >= k) {
                    output(vec[0].first);
                } else {
                    output(vec[1].first);
                }
                break;
            }
            map<long long, long long> nxt_kv;
            sum = 0;
			for (map <long long, long long> :: iterator it = kv.begin(); it != kv.end(); it ++) {
                long long cnt = it->first;
                cnt --;
                nxt_kv[cnt >> 1] += it->second;
                nxt_kv[cnt - (cnt >> 1)] += it->second;
                sum += it->second;
            }
            cur += sum;
			kv = nxt_kv;
		}
    }

    return 0;
}
