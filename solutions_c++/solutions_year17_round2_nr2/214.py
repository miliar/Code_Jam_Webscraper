#include <bits/stdc++.h>
using namespace std;

void solve_small(array<vector<string>, 3> groups)
{
    const auto compare = [](const vector<string>& a, const vector<string>& b) { return a.size() < b.size(); };
    sort(begin(groups), end(groups), compare);

    const auto place = [&](const int i)
    {
        cout << groups[i].back();
        groups[i].pop_back();
    };

    if (groups[2].size() <= groups[0].size() + groups[1].size())
    {
        while (groups[1].size() > groups[0].size())
        {
            place(2);
            place(1);
        }
        for (auto i = 0; groups[i].size(); i = 1-i)
        {
            if (groups[2].size()) place(2);
            place(i);
        }
        cout << endl;
    }
    else cout << "IMPOSSIBLE" << endl;
}

void solve_case()
{
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;

    if (R == G && R+G == N)
    {
        for (auto i = 0; i < R; i++)
            cout << "RG";
        cout << endl;
        return;
    }
    if (Y == V && Y+V == N)
    {
        for (auto i = 0; i < Y; i++)
            cout << "YV";
        cout << endl;
        return;
    }
    if (B == O && B+O == N)
    {
        for (auto i = 0; i < B; i++)
            cout << "BO";
        cout << endl;
        return;
    }

    auto groups = array<vector<string>, 3>{};

    if (G)
    {
        R -= G+1;
        auto name = string();
        for (auto i = 0; i < G; i++)
            name += "RG";
        name += "R";
        groups[0].push_back(name);
    }
    if (V)
    {
        Y -= V+1;
        auto name = string();
        for (auto i = 0; i < V; i++)
            name += "YV";
        name += "Y";
        groups[1].push_back(name);
    }
    if (O)
    {
        B -= O+1;
        auto name = string();
        for (auto i = 0; i < O; i++)
            name += "BO";
        name += "B";
        groups[2].push_back(name);
    }

    if (R < 0 || Y < 0 || B < 0)
    {
        cout << "IMPOSSIBLE" << endl;
        return;
    }

    for (auto i = 0; i < R; i++)
        groups[0].push_back("R");
    for (auto i = 0; i < Y; i++)
        groups[1].push_back("Y");
    for (auto i = 0; i < B; i++)
        groups[2].push_back("B");

    solve_small(groups);
}

int main()
{
    int T; cin >> T;
    for (auto t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        solve_case();
    }
}
