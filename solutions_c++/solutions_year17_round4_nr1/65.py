#include <iostream>
#include <vector>
#include <limits>

using namespace std;

static const int kMaxChocolate = 100;

template<class T>
void precalc(T& mat, int P) {
    mat[0][0][0] = 0;

    for (int i = 0; i <= kMaxChocolate; ++i)
        for (int j = 0; j <= kMaxChocolate; ++j)
            for (int k = 0; k <= kMaxChocolate; ++k) {
                int next = mat[i][j][k];
                if ((i * 1 + j * 2 + k * 3) % P == 0)
                    ++next;
                if (i < kMaxChocolate)
                    mat[i + 1][j][k] = max(mat[i + 1][j][k], next);
                if (j < kMaxChocolate)
                    mat[i][j + 1][k] = max(mat[i][j + 1][k], next);
                if (k < kMaxChocolate)
                    mat[i][j][k + 1] = max(mat[i][j][k + 1], next);
            }
}

int main() {
    vector< vector< vector<int> > > max_groups3(kMaxChocolate + 1, vector< vector< int > >(kMaxChocolate + 1, vector<int>(kMaxChocolate + 1, 0))), max_groups4 = max_groups3, max_groups2 = max_groups3;

    precalc(max_groups2, 2);
    cerr << "Done precalculating 2\n";
    precalc(max_groups3, 3);
    cerr << "Done precalculating 3\n";
    precalc(max_groups4, 4);
    cerr << "Done precalculating 4\n";

    int T; cin >> T;
    for (int test = 1; test <= T; ++test) {
        int N, P; cin >> N >> P;
        vector<int> rests(4, 0);
        for (int i = 0; i < N; ++i) {
            int x; cin >> x;
            rests[x % P]++;
        }

        auto &mat = (P == 3 ? max_groups3 : (P == 2 ? max_groups2 : max_groups4));
        cout << "Case #" << test << ": " << rests[0] + mat[rests[1]][rests[2]][rests[3]] << "\n";
    }
}
