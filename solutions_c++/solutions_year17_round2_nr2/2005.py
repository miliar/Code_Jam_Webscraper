#include <cstdio>
#include <map>
#include <queue>
#include <vector>
#include <limits>
#include <cassert>
using namespace std;

#define LL int64_t

int test_case = 0;

#define IN(...) fscanf(stdin, ##__VA_ARGS__)
#define OUT(...) fprintf(stdout, ##__VA_ARGS__)


//4 X   X   X
//N R O Y G B V
//6 2 0 2 0 2 0 Case #1: RYBRBY
//3 1 0 2 0 0 0 Case #2: IMPOSSIBLE
//6 2 0 1 1 2 0 Case #3: YBRGRB
//4 0 0 2 0 0 2 Case #4: YVYV

#define N_MANES 6
#define OPPOSITE(x) ((x + N_MANES / 2) % N_MANES)
#define IMPOSSIBLE OUT("Case #%d: IMPOSSIBLE\n", test_case + 1); return;
#define SOLUTION(x) OUT("Case #%d: ", test_case + 1); print(x); if (!check(x)) { assert(false); }  OUT("\n"); return;

int characters[] = { 'R', 'O', 'Y', 'G', 'B', 'V' };

int hex[] =  { 0x1, 0x1 & 0x2, 0x2, 0x2 & 0x4, 0x4, 0x4 & 0x1 };

bool check(vector<int> &values) {
    for (auto i = values.begin(); i < values.end() - 1; ++i) {
        if ((hex[*i] & hex[*(i + 1)]) != 0) {
            return false;
        }
    }

    if (values.size() > 0) {
        if ((hex[*values.begin()] & hex[*(values.end() - 1)]) != 0) {
            return false;
        }
    }

    return true;
}

void print(vector<int> &indexes) {
    for (auto i: indexes) {
        OUT("%c", characters[i]);
    }
}

#define RING_INDEX(x, values) ((x) % (values.size()))
#define POSITION_VALID(x, values) values[RING_INDEX(x)] != values[RING]

void best_place_rgb(vector<int> &values, int value) {
    for (int i = 0; i < values.size(); ++i) {
        if (values[RING_INDEX(i, values)] == values[RING_INDEX(i + 1, values)]) {
            values.insert(values.begin() + RING_INDEX(i + 1, values), value);
            return;
        }
    }

    for (int i = 0; i < values.size(); ++i) {
        if (values[RING_INDEX(i, values)] != value && values[RING_INDEX(i + 1, values)] != value) {
            values.insert(values.begin() + RING_INDEX(i + 1, values), value);
            return;
        }
    }

    values.push_back(value);
}

void inject(vector<int> &colors, int target, vector<int> &inject) {
    for (auto i = colors.begin(); i < colors.end(); ++i) {
        if (*i == target) {
            colors.insert(i + 1, inject.begin(), inject.end());
            return;
        }
    }

    assert(0);
}

int mane_colors[N_MANES];

void solve() {
    vector<int> solutions_for_mixtures[N_MANES / 2];

    // mixtures
    for (int i = 1; i < 6; i += 2) {
        if (mane_colors[i] > 0) {
            if (mane_colors[OPPOSITE(i)] < mane_colors[i]) {
                IMPOSSIBLE;
            }

            for (int j = 0; j < mane_colors[i]; ++j) {
                solutions_for_mixtures[i / 2].push_back(i);
                solutions_for_mixtures[i / 2].push_back(OPPOSITE(i));
            }
            mane_colors[OPPOSITE(i)] -= mane_colors[i];
            mane_colors[i] = 0;

        }
    }

    int are_all_zero_now = true;

    for (int i = 0; i < N_MANES; ++i) {
        if (mane_colors[i] != 0) {
            are_all_zero_now = false;
        }
    }

    int how_many_different = 0;

    for (int i = 0; i < N_MANES / 2; ++i) {
        if (!solutions_for_mixtures[i].empty()) {
            how_many_different += 1;
        }
    }
    
    for (int i = 0; i < N_MANES / 2; ++i) {
        if (!solutions_for_mixtures[i].empty()) {
            if (mane_colors[OPPOSITE(i * 2 + i)] == 0) {
                if (are_all_zero_now && how_many_different == 1) {
                    // print solution
                    SOLUTION(solutions_for_mixtures[i])
                }
                else {
                    IMPOSSIBLE
                }
            }
        }
    }

    vector<int> rgb_solution;

    for (int i = 0; i < N_MANES; i += 2) {
        while (mane_colors[i] > 0) {
            best_place_rgb(rgb_solution, i);
            mane_colors[i] -= 1;
        }

    }

    if (!check(rgb_solution)) {
        IMPOSSIBLE
    }

    for (int i = 0; i < N_MANES / 2; ++i) {
        if (!solutions_for_mixtures[i].empty()) {
            inject(rgb_solution, OPPOSITE(2 * i + 1), solutions_for_mixtures[i]);
        }
    }

    SOLUTION(rgb_solution);
}

int main(int argc, const char * argv[]) {

#if DEBUG
    freopen("/Users/kzaher/Projects/codejam/CodeJam1/unicorn/input.txt", "rb", stdin);
    freopen("/Users/kzaher/Projects/codejam/CodeJam1/unicorn/output.txt", "wb", stdout);
#endif

    int count;
    IN("%d\n", &count);

    for (test_case = 0; test_case < count; ++test_case) {
        int n;
        IN("%d %d %d %d %d %d %d\n", &n, &mane_colors[0], &mane_colors[1], &mane_colors[2], &mane_colors[3], &mane_colors[4], &mane_colors[5]);

        solve();

    }

    return 0;
}
