#include<bits/stdc++.h>

using namespace std;

#define mp(x,y) make_pair(x, y)
#define For(i, n) for (int i = 0; i < (int) n; i++)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

// R Y B G V O
map<int, string> convert = {{0, "R"}, {1, "Y"}, {2, "B"}, {3, "RG"}, {4, "YV"}, {5, "BO"}};
int first;

void myprint(int color, vector<int>& remains) {
    if (remains [color + 3] > 0) {
        For(i, remains [color + 3]) cout << convert[color + 3];
        remains [color + 3] = 0;
    }
    if (first == -1) first = color;
    remains [color] --;
    cout << convert [color];
}

int main () {
    int T;
    cin >> T;
    For(cases, T) {
        int n;
        cin >> n;
        vector<int> colors(6);
        cin >> colors[0] >> colors[5] >> colors[1] >> colors[3] >> colors[2] >> colors[4];
        For(i, 3) colors [i] -= colors [i+3];
        bool bad = false;
        For(i, 3) if (colors [i] < 0) {
            bad = true;
        }
        For(i, 3) {
            if (colors [i] == 0 && colors [i + 3] != 0) {
                For(j, 3) {
                    if (j == i) continue;
                    if (colors [j] > 0 || colors [j + 3] > 0) bad = true;
                }
            }
        }
        if (bad || !(colors [0] <= colors [1] + colors [2] && colors [1] <= colors [0] + colors [2] && colors [2] <= colors [0] + colors [1])) {
            printf("Case #%d: IMPOSSIBLE\n", cases + 1);
            continue;
        }
        printf("Case #%d: ", cases + 1);
        first = -1;
        while (colors [0] + colors [1] + colors [2] > 0) {
            if (colors [0] == colors [1] && colors [1] == colors [2]) {
                if (first == -1) first = 0;
                while(colors [0] > 0) {
                    myprint(first, colors);
                    myprint((first + 1) % 3, colors);
                    myprint((first + 2) % 3, colors);
                }
            }
            else {
                int maxcol = 0, mincol = 0;
                For(i, 3) {
                    if (colors [maxcol] < colors [i]) maxcol = i;
                    if (colors [mincol] > colors [i]) mincol = i;
                }
                int midcol = 3 - maxcol - mincol;
                if (colors [maxcol] == colors [midcol] && midcol == first) swap(midcol, maxcol);
                myprint(maxcol, colors);
                myprint(midcol, colors);
            }
        }
        For(i, 3) {
            if (colors [i + 3] > 0) {
                For(j, colors [i + 3]) cout << convert [i + 3];
            }
        }
        printf("\n");
    }
}
