#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("B-small-attempt0.in", ios::in);
    ofstream fout;
    fout.open("B-small-attempt0_output.txt", ios::out);
    int t;
    fin >> t;
    for (int zx = 1; zx <= t; ++zx)
    {
        fout << "Case #" << zx << ": ";
        int n, r, o, y, g, b, v;
        fin >> n >> r >> o >> y >> g >> b >> v;
        if (r + y < b || r + b < y || b + y < r)
        {
            fout << "IMPOSSIBLE" << endl;
            continue;
        }
        vector <pair <int, char> > col;
        col.push_back(pair<int, char> (r, 'R'));
        col.push_back(pair<int, char> (b, 'B'));
        col.push_back(pair<int, char> (y, 'Y'));
        sort(col.rbegin(), col.rend());
        string ans = "";
        int trips = col[1].first + col[2].first - col[0].first;
        for (int i = 0; i < col[1].first - trips; ++i)
            ans = ans + col[0].second + col[1].second;
        for (int i = 0; i < trips; ++i)
            ans = ans + col[0].second + col[1].second + col[2].second;
        for (int i = 0; i < col[2].first - trips; ++i)
            ans = ans + col[0].second + col[2].second;
        fout << ans << endl;
    }
}
