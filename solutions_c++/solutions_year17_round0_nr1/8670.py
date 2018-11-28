#include <iostream>
#include <stdio.h>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <queue>

using namespace std;


int bfs(int k, vector<bool> initial) {

    set<vector<bool> > visited;
    queue<pair<vector<bool>, int> > q;
    pair<vector<bool>, int> u;

    visited.insert(initial);
    q.push(make_pair(initial, 0));
    int ans = -1;

    while(!q.empty()) {

        u = q.front();
        vector<bool>& pancakes = u.first;
        int& flips = u.second;
        q.pop();

        bool val = 1;
        for(int i = 0; i < pancakes.size(); i++) {
            val &= pancakes[i];
        }

        if (val) {
            ans = flips;
            break;
        }

        for (int i = 0; i < pancakes.size(); i++) {

            if (i + k <= pancakes.size()){
                vector<bool> flipped = pancakes;

                for(int j = i; j < i+k; j++) {
                    flipped[j] = flipped[j]? 0: 1;
                }

                if(!visited.count(flipped)) {
                    visited.insert(flipped);
                    q.push(make_pair(flipped, flips + 1));
                }
            }
        }

    }

    return ans;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;

    cin >> t;

    string s;
    int k;
    for (int i = 0; i < t; i++)
    {
        cin >> s >> k;

        vector<bool> initial (s.length());
        for (int j = 0; j < s.length(); j++){
            initial[j] = s[j] == '+';
        }

        int ans = bfs(k, initial);

        if (ans < 0) {
            cout <<"Case #"<< (i + 1) <<": "<<"IMPOSSIBLE\n";
        } else cout <<"Case #"<< (i + 1) <<": "<<ans << '\n';

    }

    return 0;
}
