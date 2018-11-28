#include <iostream>
#include <vector>
#include <utility>

using namespace std;

typedef pair<int, int> tup2;

int main() {
    int t, T;
    cin >> t; T= t;
    while (t--) {
        int K, N;
        cin >> N >> K;
        vector<tup2> stalls; int s = 1; vector<tup2> temp;
        stalls.push_back(make_pair(N, 1));
        int prev_sz, new_sz, less, more, pnum;

        while (K >= s) {
            K -= s; 
            if (!K)
                break;

            temp.clear();
            // For 0
            prev_sz = stalls[0].first; pnum = stalls[0].second;
            more = prev_sz / 2; less = prev_sz - more - 1;
            temp.push_back(make_pair(less, pnum));
            if (stalls[0].first % 2) 
                temp[0].second += pnum;
            else {
                temp.push_back(make_pair(more, pnum));
            }

            // Deal with the odd size if it exists
            if (stalls.size() > 1) {
                prev_sz = stalls[1].first; pnum = stalls[1].second;
                more = prev_sz / 2; less = prev_sz - more - 1;
                if (prev_sz % 2)
                    // Case like 4 5
                    temp[1].second += 2 * pnum;
                else {
                    // Case like 3 4
                    temp[0].second += pnum;
                    temp.push_back(make_pair(more, pnum));
                }
            }

            // for (int m = 0; m < temp.size(); ++m)
            //     cout << temp[m].first << "," << temp[m].second << " ";
            // cout << endl;
            
            stalls = temp;
            s = stalls[0].second;
            if (stalls.size() > 1)
                s += stalls[1].second;


        }

        tup2 row;
        if (K == 0)
            row = stalls[0];
        else if (K <= stalls[1].second)
            row = stalls[1];
        else
            row = stalls[0];

        // cout << stalls.size() << " " << row.first << endl;
        int max = row.first / 2;
        int min = row.first - max - 1;
        cout << "Case #" << T - t <<  ": " << max << " " << min << "\n";
    }
    return 0;
}