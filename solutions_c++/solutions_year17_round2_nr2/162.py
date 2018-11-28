#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream cin("B.in");
    ofstream cout("B.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        
        vector<int> f(500, 0);
        int n; cin >> n >> f['R'] >> f['O'] >> f['Y'] >> f['G'] >> f['B'] >> f['V'];
        
        bool oh = false;

        string only = "RYB";
        string block = "GVO";
        
        for(int i = 0; i < 3; ++i)
            if(f[block[i]] > 0 and f[only[i]] == 0) {
                oh = true;
            }

        if(oh) {
            cout << "IMPOSSIBLE\n";
            continue;
        }

        string ans = "";
        
        vector<string> chunks(3);

        for(int i = 0; i < 3; ++i) {
            if(not f[only[i]])
                continue;

            string temp = "";
            temp += only[i];
            f[only[i]]--;

            while(f[block[i]] > 0) {
                temp += block[i];
                f[block[i]]--;
                if(f[only[i]] > 0) {
                    temp += only[i];
                    f[only[i]]--;
                } else {
                    break;
                }
            }

            if(f[block[i]] > 0) {
                oh = true;
            } else if(temp.back() == block[i] and n > int(temp.size())) {
                oh = true;
            } else {
                chunks[i] = temp;
                f[only[i]]++;
            }
        }

        if(oh) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        
        int all = 0;
        for(int i = 0; i < 3; ++i)
            all += f[only[i]];

        char last = 'X';
        string fine = "IMPOSSIBLE";

        for(int it = 0; it < 3; ++it) {
            string ans;
            last = only[it];
            bool bad = false;

            for(int i = 0; i < all; ++i) {
                int maxx = 0, who = -1;

                for(int j = 0; j < 3; ++j)
                    if((only[j] != last and f[only[j]] > maxx) or (only[j] != last and maxx > 0 and (f[only[j]] == maxx and not ans.empty() and ans[0] == only[j]))) {
                        maxx = f[only[j]];
                        who = j;
                    }

                if(who == -1) {
                    bad = true;
                    break;
                }
                
                if(chunks[who] != "") {
                    ans += chunks[who];
                    chunks[who] = "";
                } else {
                    ans += only[who];
                }

                f[only[who]]--;

                last = only[who];
            }
            
            for(int i = 0; i < n; ++i)
                if(ans[i] == ans[(i + 1) % n])
                    bad = true;

            if(bad)
                ans = "IMPOSSIBLE";
            else
                fine = ans;
        }

        cout << fine << "\n";
        cerr << t_case << "\n";
    }
}
