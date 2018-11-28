#include <iostream>
#include <vector>
#include <fstream>
#include <set>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

class horse {
    public:
        double s_pos;
        int m_spd;
        mutable double time_to_D;

        horse() {}

        horse(double pos, int spd, int D) : s_pos(pos), m_spd(spd), time_to_D((D - pos) / spd) {}
};

class comparisonObj {
public:
    bool operator()(const horse &h1, const horse &h2) const{
        return h1.s_pos > h2.s_pos;
    }
};

int main() {
    ifstream in("A-large.in");
    if(!in.is_open()) {
        cout << "Error opening input file.\n";
        return 1;
    }
    ofstream out("outputAlarge.txt");
    if(!out.is_open()) {
        cout << "Error opening output file.\n";
        return 1;
    }

    int T;
    in >> T;

    for (int c = 0; c < T; ++c) {
        int D, N, m_spd;
        double s_loc;
        in >> D >> N;
        set<horse, comparisonObj> horses;
        for (int i = 0; i < N; ++i) {
            in >> s_loc >> m_spd;
            horses.emplace(s_loc, m_spd, D);
        }
        auto prev = horses.begin();
        for (auto it = horses.begin(); it != horses.end(); ++it) {
            if (it != prev) {
                if (it->time_to_D < prev->time_to_D)
                    it->time_to_D = prev->time_to_D;
                prev = it;
            }
        }
        out << "Case #" << c + 1 << ": " << fixed << D / horses.rbegin()->time_to_D << endl;
    }

    return 0;
}
