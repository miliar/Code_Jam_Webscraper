#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<vector>
#include<algorithm>
#define FOR(i,l,n) for(int i=l;i<n;i++)
#define ull unsigned long long int
using namespace std;
void add_map_val(map<ull, ull> &interval_count_map, ull key, ull val) {
    if (interval_count_map.find(key) != interval_count_map.end()) {
        interval_count_map[key] += val;
    } else {
        interval_count_map[key] = val;
    }
}
void dec_map_val(map<ull, ull> &interval_count_map, ull key) {
    if (interval_count_map[key] == 1) {
        interval_count_map.erase(key);
    } else {
        interval_count_map[key]--;
    }
}
int main() {
    int t;
    scanf("%d", &t);
    FOR(i, 0, t) {
        ull n, k;
        scanf("%llu %llu", &n, &k);
        map<ull, ull> interval_count_map;
        interval_count_map[n] = 1;
        while(k>=1) {
            ull curr_interval = interval_count_map.rbegin()->first;
            ull l,r;
            if (curr_interval%2) {
                l = (curr_interval-1)/2;
                r = (curr_interval-1)/2;
            } else {
                l = curr_interval/2 - 1;
                r = curr_interval/2;
            }
            //cout << "k " << k << " curr " << curr_interval << " cnt " << interval_count_map[curr_interval] << " l " << l << " r " << r << endl;
            if (interval_count_map[curr_interval] < k) {
                add_map_val(interval_count_map, l, interval_count_map[curr_interval]);
                add_map_val(interval_count_map, r, interval_count_map[curr_interval]);
                k-=interval_count_map[curr_interval]-1;
                interval_count_map.erase(curr_interval);
            } else {
                //cout << "Case #" << i+1 << ": " << interval_count_map.rbegin()->first << " " << interval_count_map.begin()->first << endl;
                cout << "Case #" << i+1 << ": " << r << " " << l << endl;
                break;
            }
            k--;
        }
    }
    return 0;
}
