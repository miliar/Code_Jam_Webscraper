#include <bits/stdc++.h>

using namespace std;

struct rect {
public:
    int x1 = 100, y1 = 100, x2= -1, y2 = -1; // top left, bottom right
};

int R, C;
char grid[50][50];

vector<char> letters;
map<char, rect> rectangles;

int intersects_rect(int x1, int y1, int x2, int y2, char c1) {
    if(x1 < 0 || x2 >= C || y1 < 0 || y2 >= R) return true;
    for(char c : letters) {
        if(c == c1) continue;
        rect r = rectangles[c];
        if (r.x1 <= x2 && r.x2 >= x1 && r.y1 <= y2 && r.y2 >= y1 ) {
            return true;
        }
    }
    return false;
}

int main() {

    int T;

    scanf("%d", &T);

    for(int t = 1; t <= T; t++) {
        letters.clear();
        rectangles.clear();
        scanf("%d %d", &R, &C);
        for(int i = 0; i < R; i++) scanf("%s", &grid[i]);
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                char c = grid[i][j];
                if(c == '?') continue;
                letters.push_back(c);
                rect r;
                if(rectangles.find(c) != rectangles.end()) {
                    r = rectangles[c];
                }
                if (j < r.x1) r.x1 = j;
                if (j > r.x2) r.x2 = j;
                if (i < r.y1) r.y1 = i;
                if (i > r.y2) r.y2 = i;
                rectangles[c] = r;
            }
        }

        char answer[100][100];
        for(int i = 0; i < letters.size(); i++) {
            rect r = rectangles[letters[i]];
            int x1 = r.x1;
            int y1 = r.y1;
            int x2 = r.x2;
            int y2 = r.y2;
            while(!intersects_rect(x1, y1, x2, y2, letters[i])) {
                x1--;
            }
            x1++;
            while(!intersects_rect(x1, y1, x2, y2, letters[i])) {
                x2++;
            }
            x2--;
            while(!intersects_rect(x1, y1, x2, y2, letters[i])) {
                y1--;
            }
            y1++;
            while(!intersects_rect(x1, y1, x2, y2, letters[i])) {
                y2++;
            }
            y2--;
            r.x1 = x1;
            r.x2 = x2;
            r.y1 = y1;
            r.y2 = y2;
            rectangles[letters[i]] = r;
            //cout << letters[i] << " " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
            for(int row = y1; row <= y2; row++) {
                for(int col = x1; col <= x2; col++) {
                    answer[row][col] = letters[i];
                }
            }
        }
        cout << "Case #" << t << ": " << endl;
        for(int r = 0; r < R; r++) {
            for(int c = 0; c < C; c++) {
                cout << answer[r][c];
            }
            cout << endl;
        }
    }

    return 0;
}