#include <vector>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <map>
#include <math.h>
#include <climits>
#include <iomanip>

using namespace std;
typedef vector< vector<char>> GRID;

struct Point {
     
    int lx;
    int rx;
    int ty;
    int by;
    char c;

    Point(int y, int x, char character) {
        rx = x;
        lx = x;
        ty = y;
        by = y;
        c = character;
    }
};

bool solution(vector<vector<char>>& grid, vector<Point>& points)
{
    for (Point& p: points) {

        while (p.ty > 0 && grid[p.ty-1][p.rx] == '?') {
            p.ty -= 1;
            grid[p.ty][p.rx] = p.c;
        } 

        while (p.by < grid.size() - 1 && grid[p.by+1][p.rx] == '?') {
            p.by += 1;
            grid[p.by][p.rx] = p.c;
        } 

    }

    for (Point&p: points) {
        //check left side
        bool good = true;
        while (p.lx > 0 && good) {
            for (int ty = p.ty; ty <= p.by && good; ++ty) {
                if (grid[ty][p.lx-1] != '?') good = false;
            }
            if (good) p.lx--;
        }
        good = true;
        while (p.rx < grid[0].size() - 1 && good) {
            for (int ty = p.ty; ty <= p.by && good; ++ty) {
                if (grid[ty][p.rx+1] != '?') good = false;
            }
            if (good) p.rx++;
        }

        for (int row = p.ty; row <= p.by; ++row) {
            for (int col = p.lx; col <= p.rx; ++col) {
                grid[row][col] = p.c;
            }
        }
    }

    for (int r = 0; r < grid.size(); ++r) {
        for( char c : grid[r]) {
            if (c == '?') return false;
        }
    }

    return true;
}

void printGrid(const GRID& g) {
    for (int row = 0; row < g.size(); ++row) {
        for (int col = 0; col < g[0].size();++col) {
            cout << g[row][col]; 
        }
        cout << endl;
    }
}

int main()
{
    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        int R, C;
        cin >> R >> C;
        cout << "Case #" << i << ":" << endl;

        vector<vector<char>> grid(R, vector<char>(C));
        vector<Point> points;
        for (int row = 0; row < R; ++row) {
            for (int col = 0; col < C; ++col) {
                char c;
                cin >> c;
                grid[row][col] = c;

                if (c != '?') {
                    Point p(row, col, c);
                    points.push_back(p);
                }
            }
        }
        solution(grid,points);
        printGrid(grid);
    }

    return 0;
}
