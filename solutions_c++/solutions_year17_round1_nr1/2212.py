#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool expand(vector<string> &grid, int r, int start, int end, char current) {
    //Check if expansion is allowed
    for(int c = start; c <= end; c++) {
        if(grid[r][c] != '?') {
            //cerr << "Failed at " << r << "," << c << endl;
            return false;
        }
    }
    //Set them all
    for(int c = start; c <= end; c++) {
        grid[r][c] = current;
    }
    return true;
}

int main() {
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        int R, C;
        cin >> R >> C >> ws;
        vector<string> grid(R);
        for(int r = 0; r < R; r++) {
            string line;
            cin >> line >> ws;
            // Expand left-right
            char current = '?';
            for(int c = 0; c < C; c++) {
                if(line[c] != '?') {
                    //Found first character then fill backwards
                    if(current == '?') {
                        for(int i=0; i < c; i++) {
                            line[i] = line[c];
                        }
                    }
                    current = line[c];
                }
                //Set it to the last seen character
                line[c] = current;
            }
            grid[r] = line;
        }
        // Expand sections vertically
        for(int r = 0; r < R; r++) {
            string &line = grid[r];
            //Find run of letters
            char current = line[0];
            int start = 0;
            for(int c = 1; c <= C; c++) {
                //cerr << "Looking at [" << r << "," << c << "]" << endl;
                char next = line[c];
                if(current == next && c != C) {
                    continue;
                }

                //cerr << "Processing row " << r << " span [" << start << "," << c - 1 << "]" << endl;
                //Process the run
                //Expand Upwards
                for(int rr = r - 1; rr >= 0; rr--) {
                    //cerr << r << " trying to expand into " << rr << endl;
                    if(!expand(grid, rr, start, c - 1, current)) break;
                    //cerr << r << " expanded into " << rr << endl;
                }
                //Expand Downwards
                for(int rr = r + 1; rr < R; rr++) {
                    //cerr << r << " trying to expand into " << rr << endl;
                    if(!expand(grid, rr, start, c - 1, current)) break;
                    //cerr << r << " expanded into " << rr << endl;
                }
                //Update the current and start
                current = next;
                start = c;
            }
        }
        cout << "Case #" << (t + 1) << ":" << endl;
        for(string &r : grid) {
            cout << r << endl;
        }
    }
}
