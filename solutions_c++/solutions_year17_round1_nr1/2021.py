#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int T;

int R, C;
char map[25][25];

void reset_map()
{
    for (int j = 0; j < 25; ++j) {
        for (int k = 0; k < 25; ++k) {
            map[j][k] = '0';
        }
    }
}

class coord
{
public:
    int x;
    int y;
    coord(int i, int j) {
        x = i;
        y = j;
    }
};

bool is_capital(char c)
{
    return c >= 'A' && c <= 'Z';
}

bool check(int x, int y, int dx, int dy)
{
    int new_x = x + dx;
    int new_y = y + dy;
    if (new_x < 0 || new_x >= C) {
        return false;
    }
    if (new_y < 0 || new_y >= R) {
        return false;
    }
    char c = map[y][x];
    if (is_capital(c)) {
        if ( dx == 0 && !is_capital(map[new_y][x]) )
            return true;
        if ( dy == 0 && !is_capital(map[y][new_x]) )
            return true;
    } else {
        cout << "Error, not capital!" << endl;
    }
    return false;
}

int main()
{
	ifstream fin("A-large.in", ifstream::in);
	ofstream fout("result.out", ofstream::out);
	fin >> T;
	//cin >> T;

	vector<coord> init_pos;
	for(int i = 0; i < T; ++i) {
		fin >> R >> C;
        //cin >> R >> C;
        cout << R << " " << C << endl;  // for debug
        reset_map();
        init_pos.clear();

        char temp;
        for (int j = 0; j < R; ++j) {
            for (int k = 0; k < C; ++k) {
                //cin >> temp;
                fin >> temp;
                if (is_capital(temp)) {
                    map[j][k] = temp;
                    init_pos.push_back(coord(k, j));
                }
            }
        }
        for (int j = 0; j < init_pos.size(); ++j) {
            coord pos = init_pos[j];
            int x = pos.x, y = pos.y;
            char c = map[y][x];
            int left_edge = x, right_edge = x;
            int up_edge = y, bottom_edge = y;
            while (check(left_edge, y, -1, 0)) {
                map[y][--left_edge] = c;
            }
            while (check(right_edge, y, 1, 0)) {
                map[y][++right_edge] = c;
            }
            cout << "expand x from " << left_edge << " to " << right_edge << endl;
            while (check(x, up_edge, 0, -1)) {
                bool can_up = true;
                for (int m = left_edge; m <= right_edge; ++m) {
                    if (!check(m, up_edge, 0, -1)) {
                        can_up = false;
                        break;
                    }
                }
                if (can_up) {
                    --up_edge;
                    for (int m = left_edge; m <= right_edge; ++m) {
                        map[up_edge][m] = c;
                    }
                } else {
                    break;
                }
            }
            cout << "expand y from " << up_edge << endl;
            while (check(x, bottom_edge, 0, 1)) {
                bool can_down = true;
                for (int m = left_edge; m <= right_edge; ++m) {
                    if (!check(m, bottom_edge, 0, 1)) {
                        can_down = false;
                        break;
                    }
                }
                if (can_down) {
                    ++bottom_edge;
                    for (int m = left_edge; m <= right_edge; ++m) {
                        map[bottom_edge][m] = c;
                    }
                } else {
                    break;
                }
            }
            cout << "expand y to " << bottom_edge << endl;
        }


        cout << "Case #" << (i+1) << ":" << endl;
        for (int j = 0; j < R; ++j) {
            for (int k = 0; k < C; ++k) {
                cout << map[j][k];
            }
            cout << endl;
        }
        fout << "Case #" << (i+1) << ":" << endl;
        for (int j = 0; j < R; ++j) {
            for (int k = 0; k < C; ++k) {
                fout << map[j][k];
            }
            fout << endl;
        }
	}

	return 0;
}
