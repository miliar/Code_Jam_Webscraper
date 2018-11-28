#include <bits/stdc++.h>
using namespace std;

unsigned long long value(vector<int> d) {
    int n = d.size();
    unsigned long long ans = 0;
    for(int i = 0; i < n; ++i)
        ans = 10 * ans + d[i];
    return ans;
}

int main() {
    ifstream cin("B.in");
    ofstream cout("B.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        
        unsigned long long x; cin >> x;
        vector<int> digs;

        unsigned long long temp = x;

        while(temp) {
            digs.push_back(temp % 10);
            temp /= 10;
        }

        reverse(digs.begin(), digs.end());

        vector<int> ansDigs;
        int nr = digs.size();
        int last = 1;

        for(int poz = 0; poz < nr; ++poz) {
            for(int d = 9; d >= last; --d) {
                vector<int> cand = ansDigs;
                for(int i = poz; i < nr; ++i)
                    cand.push_back(d);
                if(value(cand) <= x) {
                    ansDigs.push_back(d);
                    last = d;
                    break;
                }
            }

            if(ansDigs.empty())
                break;
        }

        if(ansDigs.empty()) {
            unsigned long long nine = 9;
            while(nine * 10 + 9 <= x)
                nine = nine * 10 + 9;
            cout << nine << "\n";
        } else {
            cout << value(ansDigs) << "\n";
        }
    }
}
