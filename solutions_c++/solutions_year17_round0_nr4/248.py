// Compile with MinGW-64 (6.3.0) in MSYS2

#include <stdint.h>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int getSlashRow(int x, int y) { return x + y; }
int getBSlashRow(int x, int y, int n) { return x - y + (n - 1); }

class fieldState {
  public:
    fieldState(int n) {
        size = n;
        field = vector<vector<char>>(n, vector<char>(n, '.'));
        o_vert = vector<bool>(n, false);
        o_horiz = vector<bool>(n, false);
        o_slash = vector<bool>(2*n-1, false);
        o_bslash = vector<bool>(2*n-1, false);
        style_points = 0;
    }
    
    void Set(char ch, int x, int y) {
        field[x][y] = ch;
        if (ch == 'x' || ch == 'o') {
            o_vert[x] = true;
            o_horiz[y] = true;
            style_points++;
        }

        if (ch == '+' || ch == 'o') {
            o_slash[getSlashRow(x, y)] = true;
            o_bslash[getBSlashRow(x, y, size)] = true;
            style_points++;
        }
    }

    void SetToMax(int x, int y) {
        bool upped = false;
        char ch = field[x][y];
        if ((ch == '.' || ch == '+') && !o_vert[x] && !o_horiz[y]) {
            ch = (ch == '.') ? 'x' : 'o';
            
            o_vert[x] = true;
            o_horiz[y] = true;
            style_points++;
            upped = true;
        }

        if ((ch == '.' || ch == 'x') &&
            !o_slash[getSlashRow(x, y)] &&
            !o_bslash[getBSlashRow(x, y, size)]) {
            ch = (ch == '.') ? '+' : 'o';

            o_slash[getSlashRow(x, y)] = true;
            o_bslash[getBSlashRow(x, y, size)] = true;
            style_points++;
            upped = true;
        }

        if (upped)
            models_added.push_back(make_tuple(ch, x, y));
    }

    int size;
    vector<vector<char>> field;
    vector<bool> o_vert;
    vector<bool> o_horiz;
    vector<bool> o_slash;
    vector<bool> o_bslash;
    vector<std::tuple<char, int, int>> models_added;
    int style_points;
};

void solve(int caseNo) {
    std::cout << "Case #" << caseNo << ": ";

    int n, m;
    cin >> n >> m;

    fieldState field(n);
    
    for (int i = 0; i < m; i++) {
        char ch;
        cin >> ch;
        int x, y;
        cin >> x >> y;
        x--; y--;
        field.Set(ch, x, y);
    }

    for (int i = 0; i <= n / 2; i++) {
        for (int x = i; x < n - i; x++)
            field.SetToMax(x, i);

        for (int y = i+1; y < n - i; y++) {
            field.SetToMax(i, y);
            field.SetToMax((n-1)-i, y);
        }

        for (int x = i+1; x < n - (i+1); x++)
            field.SetToMax(x, (n-1)-i);
    }

    if (n % 2 != 0) {
        field.SetToMax(n/2, n/2);
    }

    //std::sort(models_added.begin(), models_added.end());
    cout << field.style_points << " " << field.models_added.size() << "\n";
    for (auto model : field.models_added) {
        cout << std::get<0>(model) << " " << (std::get<1>(model) + 1) << " "
             << (std::get<2>(model) + 1) << "\n";
    }
}

int main(int argc, char** argv) {
    int N;
    std::cin >> N;
    std::string str;
    std::getline(std::cin, str);

    for(int i = 0; i < N; ++i) {
        solve(i + 1);
    }

    return 0;
}