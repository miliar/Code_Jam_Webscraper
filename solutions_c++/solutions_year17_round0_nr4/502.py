#include <iostream>
#include <vector>
#include <string>
#include <map>

struct PointValue {
    int row;
    int col;
    char val;
    PointValue(int _r, int _c, char _ch) : row(_r), col(_c), val(_ch) {};
};


void print2v(const std::vector< std::vector<char> >& v) {
    for (int i=0; i < v.size(); ++i) {
        for (int j=0; j < v[i].size(); ++j) {
            std::cout << v[i][j];
        }
        std::cout << std::endl;
    }
}


int main() {
    int T;
    std::cin >> T;
    for (int t=1; t <= T; ++t) {
        int N, M;
        std::cin >> N >> M;
        std::vector<std::vector<char> > m(N, std::vector<char>(N,'.'));
        for (int i=0; i < M; ++i) {
            char ch;
            int row, col;
            std::cin >> ch >> row >> col;
            m[row-1][col-1] = ch;
        }

        //Solving for small testcase only
        //The optimal solution is gained when the pattern is as follow:
        // o+++++
        // .x....
        // ..x...
        // ...x..
        // ....x.
        // .++++x
        //
        //
        // ++o+++
        // x.....
        // .x....
        // ...x..
        // ....x.
        // .++++x
        //
        //
        // +++++o
        // ....x.
        // ...x..
        // ..x...
        // .x....
        // x++++.
        //
        //

        //Generating target solution
        std::vector<std::vector<char> > target(N, std::vector<char>(N, '.'));
        /// Locating the 'o' in m
        int loc_o = 0;
        for (int col=0; col < N; ++col) {
            if (m[0][col] == 'o' || m[0][col] == 'x') {
                loc_o = col;
                break;
            }
        }

        int score = 0;
        target[0][loc_o] = 'o';
        score += 2;
        
        /// Generating the target's first row
        for (int col=0; col < N; ++col) {
            if (target[0][col] == '.') {
                target[0][col] = '+';
                score += 1;
            }
        }

        /// Generating the target's diagonal
        for (int row=1; row < N; ++row) {
            int col = row;
            if (loc_o < N-1) {
                col = row;
                if (col <= loc_o) col--;
            }
            else {
                col = N - row - 1;
            }
            target[row][col] = 'x';
            score += 1;
        }

        /// Generating the target's last row
        for (int col=1; col < N-1; ++col) {
            target[N-1][col] = '+';
            score += 1;
        }


        // Get the difference and output solution

        std::vector<PointValue> diff;
        for (int row=0; row < N; ++row) {
            for (int col=0; col < N; ++col) {
                if (m[row][col] != target[row][col]) {
                    diff.push_back( PointValue(row, col, target[row][col]) );
                    // std::cout << row << "," << col << ": " << m[row][col] << " | " << target[row][col] << std::endl;
                }
            }
        }
        int diff_size = diff.size();


        std::cout << "Case #" << t << ": " << score << " " << diff_size << std::endl;
        for (int i=0; i < diff.size(); ++i) {
            const PointValue& pv = diff[i];
            std::cout << pv.val << " " << (pv.row+1) << " " << (pv.col+1) << std::endl;
        }
    }
    //std::cout << "Finished!" << std::endl;
    return 0;
}


