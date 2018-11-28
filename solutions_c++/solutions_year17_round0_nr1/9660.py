#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream ifs; ifs.open("A-large.in");
    ofstream ofs; ofs.open("A-large.out");

    int tc, fSize, flip, cur;
    bool isPossible;
    ifs >> tc;
    string cakes;

    for (int t = 1; t <= tc; t++) {
        isPossible = true;
        cur = flip = fSize = 0;
        ifs >> cakes >> fSize;

        if (fSize > cakes.length()) {
            isPossible = false;
        } else {
            while (cur + fSize < cakes.length() + 1) {
                if (cakes[cur] == '-') {
                    flip++;
                    for (int f = cur; f < cur + fSize; f++) {
                        if (cakes[f] == '-') { cakes[f] = '+'; }
                        else { cakes[f] = '-'; }
                    }
                }
                cur++;
            }
        }

        for (int i = (int)(cakes.length() - 1); i >= (int)(cakes.length() - fSize); i--) {
            if (cakes[i] == '-') {  isPossible = false; }
        }

        if (!isPossible) { ofs << "Case #" << t << ": IMPOSSIBLE" << endl; }
        else { ofs << "Case #" << t << ": " << flip << endl; }

        cakes.clear();
    }

    return 0;
}
