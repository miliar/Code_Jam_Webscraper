#include <cstdio>
#include <iostream>
#include <map>

using namespace std;

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        long long n = 0, k = 0;
        cin >> n >> k;
        map<long long, long long> my_map;
        my_map.insert(pair<long long, long long>(n, 1));
        map<long long, long long>::iterator my_map_it;
        long long cnt = 0;
        while (cnt < k) {
            if (my_map.empty()) {
                cout << "Case #" << kase << ": 0 0" << endl;;
                break;
            }
            my_map_it = my_map.end();
            my_map_it--;
            long long global_max = my_map_it->first;
            long long global_max_cnt = my_map_it->second;
            my_map.erase(global_max);
            long long local_min = (global_max - 1) / 2;
            long long local_max = global_max - local_min - 1;
            cnt += global_max_cnt;
            if (cnt >= k) {
                cout << "Case #" << kase << ": " << local_max << " " << local_min << endl;
                break;
            }
            if (local_min > 0) {
                map<long long, long long>::iterator temp_it = my_map.find(local_min);
                if (temp_it != my_map.end()) {
                    temp_it->second = temp_it->second + global_max_cnt;
                } else {
                    my_map.insert(pair<long long, long long>(local_min, global_max_cnt));
                }
            }
            if (local_max > 0) {
                map<long long, long long>::iterator temp_it = my_map.find(local_max);
                if (temp_it != my_map.end()) {
                    temp_it->second = temp_it->second + global_max_cnt;
                } else {
                    my_map.insert(pair<long long, long long>(local_max, global_max_cnt));
                }
            }
        }
    }
    return 0;
}
