#include <iostream>
#include <deque>


using namespace std;


int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int n;
    cin >> n;
    for (int ncase = 1; ncase <= n; ++ncase)
    {
        cout << "Case #" << ncase << ": ";
        cerr << "Case #" << ncase << ": ";
        string s;
        cin >> s;
        int ss = s.size();
        deque<pair<int, int>> st;
        st.push_back({0, 0});
        bool modified = 0;
        for (int i = 0; i < ss; i++)
        {
            if (modified || st.back().first == s[i] - '0')
            {
                st.back().second += 1;
                continue;
            }
            if (st.back().first < s[i] - '0')
            {
                st.push_back({s[i] - '0', 1});
            }
            else
            {
                int d = st.back().second;
                st.back().first -= 1;
                st.back().second = 1;
                st.push_back({9, d});
                modified = 1;
            }
        }
        modified = 0;
        while (!st.empty())
        {
            if (st.front().first || modified)
            {
                for (int i = 0; i < st.front().second; i++)
                {
                    cout << st.front().first;
                    cerr << st.front().first;
                }
                modified = 1;
            }
            st.pop_front();
        }
        cout << endl;
        cerr << endl;
    }
}