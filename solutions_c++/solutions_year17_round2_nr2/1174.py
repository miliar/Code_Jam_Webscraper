#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

struct Color {
    char c;
    int count;
    Color (char _c, int _count) {
        c = _c;
        count = _count;
    }
};

bool operator < (const Color& a, const Color& b) {
    return a.count < b.count;
}

int main() {
    int T;
    cin >> T;
    for (int tt = 1; tt<= T; ++tt) {
        int N;
        int R, Y, B;
        int t1, t2, t3;
        cin >> N;
        cin >> R >> t1 >> Y >> t2 >> B >> t3;
        vector<Color> C;
        C.push_back(Color('R', R));
        C.push_back(Color('Y', Y));
        C.push_back(Color('B', B));
        sort(C.begin(), C.end());
        cout << "Case #" << tt << ": ";
        if (C[0].count + C[1].count >= C[2].count) {
            vector<char> table;
            for (int i=0; i<C[2].count; ++i) {
                table.push_back(C[2].c);
            }
            int index = 0;
            for (int i=0; i<C[1].count; ++i) {
                table.insert(table.begin() + index, C[1].c);
                index += 2;
                if (index >= table.size())
                    index = 0;
            }
            for (int i=0; i<C[0].count; ++i) {
                table.insert(table.begin() + index, C[0].c);
                index += 2;
                if (index >= table.size())
                    index = 0;
            }
            for (int i=0; i<table.size(); ++i) {
                cout << table[i];
            }
        } else {
            cout << "IMPOSSIBLE";
        }
        cout << endl;
    }
    return 0;
}
