#include <iostream>
#include <list>
#include <utility>
#include <vector>

using namespace std;

using ULL = long long;
using P = pair<ULL, ULL>;

void insert_ull_list(list<ULL>& ull_list, ULL val)
{
    auto it = ull_list.begin();
    while (it != ull_list.end() && *it < val) {
        ++it;
    }
    ull_list.insert(it, val);
}

ULL find_insertion_pos(const list<ULL>& ull_list, P& p)
{
    ULL min_dist = 0;
    ULL min_index = -1;
    for (auto it = ull_list.begin(); it != ull_list.end(); ++it) {
        auto it_next = next(it, 1);
        if (it_next == ull_list.end()) break;
        ULL distance = *it_next - *it - 1;
        if (distance > min_dist) {
            min_dist = distance;
            min_index = (*it_next + *it) / 2;
        }
    }
    ULL max_min = (min_dist - 1) / 2;
    ULL max_max = (min_dist % 2 != 0) ? max_min : max_min + 1;
    p = make_pair(max_max, max_min);
    return min_index;
}

void small(ULL k, ULL n, ULL num_case)
{

    list<ULL> ull_list;
    insert_ull_list(ull_list, 0);
    insert_ull_list(ull_list, n + 1);
    for (ULL i = 0; i < k; ++i) {
        P p;
        ULL min_index = find_insertion_pos(ull_list, p);
        insert_ull_list(ull_list, min_index);
        if (i == k - 1) {
            cout << "Case #" << num_case << ": " << p.first << " " << p.second << endl;
        }
    }
}

ULL power(ULL base, ULL n)
{
    ULL now = 1;
    for (ULL i = 0; i < n; ++i) {
        now *= base;
    }
    return now;
}

ULL log_two_ceiling(ULL n)
{
    ULL base = 1;
    for (ULL i = 0; i <= 60; ++i, base *= 2) {
        if (n <= base) {
            return i;
        }
    }
    return -1; // indicate error
}

void large(ULL k, ULL n, ULL num_case)
{
    /*
//    cout << "Case #" << num_case << ": " << p.first << " " << p.second << endl;
    ULL dist = (n - 1) / 2;
    // 1, 3, 7, 15
    vector<ULL> two_power(61);
    ULL base = 1;
    for (ULL i = 0; i <= 60; ++i, base *= 2) {
        two_power[i] = base;
    }
//    cout << two_power[40] << endl;
    ULL p1 = 0;
    for (ULL i = 1; i <= k; ++i) {
        // 2 ** p1 >= i
        while (i >= two_power[p1 + 1]) {
            ++p1;
            dist = (dist - 1) / 2;
        }
        cout << "Case #" << num_case << ": " << dist << " " << dist << endl;
    }
    */
    ULL ith_layer = log_two_ceiling(k + 1) - 1;
    ULL ith_layer_num_full_nodes = power(2, ith_layer);
    ULL ith_no_nodes = k - (ith_layer_num_full_nodes - 1);
    ULL ith_layer_sum = n - (ith_layer_num_full_nodes - 1);
    ULL kth_node_val = (ith_layer_sum / ith_layer_num_full_nodes);
    kth_node_val += ((ith_no_nodes <= (ith_layer_sum % ith_layer_num_full_nodes)) ? 1 : 0);
    /*
    cout << "layer:\t" << ith_layer << endl;
    cout << "num_full_nodes:\t" << ith_layer_num_full_nodes << endl;
    cout << "no_nodes:\t" << ith_no_nodes << endl;
    cout << "layer_sum:\t" << ith_layer_sum << endl;
    cout << "kth_node_val:\t" << kth_node_val << endl;
    */
    ULL distance = kth_node_val;
    ULL min_s = (distance - 1) / 2;
    ULL max_s = (distance % 2 != 0) ? min_s : min_s + 1;
    cout << "Case #" << num_case << ": " << max_s << " " << min_s << endl;
}

int main(void)
{
    ULL t;
    cin >> t;
    for (ULL i = 0 ; i < t; ++i) {
        ULL n, k;
        // cout << "FUCK" << endl;
        cin >> n >> k;
        // small(k, n, i + 1);
        large(k, n, i + 1);
    }
    return 0;
}

