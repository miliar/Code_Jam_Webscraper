#include <iostream>
#include <vector>
#include <string>

int main(int argc, char** argv) {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        int R;
        int C;
        std::cin >> R >> C;
        std::vector<std::string> rows(R);
        std::vector<std::vector<bool> > dones(R, std::vector<bool>(C, false));
        for (int j = 0; j < R; ++j) {
            std::cin >> rows[j];
        }
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                //if (rows[r][c] == '?') {
                if (!dones[r][c]) {
                    // find the first one
                    bool found(false);
                    int selectedR(r);
                    for (int r2 = r; r2 < R; ++r2) {
                        for (int c2 = c; c2 < C && !found; ++c2) {
                            if (rows[r2][c2] != '?') {
                                rows[r][c] = rows[r2][c2];
                                dones[r][c] = true;
                                found = true;
                                selectedR = r2;
                                //std::cerr << "![" << r << "][" << c << "] = " << rows[r][c] << std::endl;
                            }
                        }
                    }
                    // find the last one
                    int lastR = r;
                    int lastC = c;
                    bool goodCol(true);
                    for (; lastC < C && goodCol; ++lastC) {
                        for (int r2 = r; r2 < R && r2 <= selectedR && goodCol; ++r2) {
                            if (rows[r2][lastC] != '?' && rows[r2][lastC] != rows[r][c])
                                goodCol = false;
                        }
                    }
                    if (!goodCol)
                        lastC--;
                    bool goodRow(true);
                    for (; lastR < R && goodRow; ++lastR) {
                        for (int c2 = 0; c2 < c && goodRow; ++c2) {
                            if (!dones[lastR][c2])
                                goodRow = false;
                        }
                        for (int c2 = c; c2 < lastC && goodRow; ++c2) {
                            //std::cerr << c2 << ": " << rows[lastR][c2] << std::endl;
                            if (rows[lastR][c2] != '?' && rows[lastR][c2] != rows[r][c])
                                goodRow = false;
                        }
                    }
                    if (!goodRow)
                        lastR--;
                    //std::cerr << "  $[" << r << "][" << c << "] -> [" << lastR << "][" << lastC << "] = " << rows[r][c] << std::endl;
                    // paint
                    for (int r2 = r; r2 < lastR; ++r2) {
                        for (int c2 = c; c2 < lastC; ++c2) {
                            rows[r2][c2] = rows[r][c];
                            dones[r2][c2] = true;
                        }
                    }
                }
            }
        }
        std::cout << "Case #" << (i + 1) << ":" << std::endl;
        for (int r = 0; r < R; ++r) {
            std::cout << rows[r] << std::endl;
        }
    }
}
