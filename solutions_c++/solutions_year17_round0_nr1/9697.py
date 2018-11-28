#include <iostream>
#include <numeric>
#include <map>
#include <vector>
#include <queue>
using namespace std;

using state = vector<bool>;

int bfs(const state& initial, int k)
{
    queue<pair<state, int>> q;
    q.emplace(initial, 0);

    map<state, bool> visited;
    visited[initial] = true;

    while(!q.empty())
    {
        auto s = q.front();
        q.pop();

        if(accumulate(s.first.begin(), s.first.end(), 0) == s.first.size())
        {
            return s.second;
        }

        for(int i = 0; i <= s.first.size() - k; ++i)
        {
            state new_s = s.first;
            for(int j = 0; j < k; ++j)
            {
                new_s[i + j] = !new_s[i + j];
            }

            if(!visited[new_s]) 
            {
                q.emplace(new_s, s.second + 1);
                visited[new_s] = true;
            }
        }
    }

    return -1;
}

int main(int argc, char *argv[])
{
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        string s;
        cin >> s;

        state st;
        for(auto ch : s)
        {
            st.emplace_back(ch == '+');
        }

        int k;
        cin >> k;

        cout << "Case #" << i + 1 << ": ";

        int res = bfs(st, k);
        if(res == -1)
        {
            cout << "IMPOSSIBLE";
        }
        else 
        {
            cout << res;
        }
        cout << endl;
    }
}
