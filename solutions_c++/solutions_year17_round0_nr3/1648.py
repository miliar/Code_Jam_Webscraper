#include <iostream>
using namespace std;

long* get_ls_rs(long no_of_stalls, long no_of_people) {
    long ls_rs[2];

    // find no of empty stalls on both sides after the person chose one
    long rs = no_of_stalls / 2;
    --no_of_stalls;
    long ls = no_of_stalls / 2;

    if (no_of_people == 1) {
        ls_rs[0] = rs;
        ls_rs[1] = ls;
    } else {
        long people_rs = no_of_people / 2;
        --no_of_people;
        long people_ls = no_of_people / 2;

        long* res;
        if (no_of_people&1) {
            res = get_ls_rs(rs, people_rs);
        } else {
            res = get_ls_rs(ls, people_ls);
        }
        ls_rs[0] = res[0];
        ls_rs[1] = res[1];
    }

    return ls_rs;
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        long N, K;
        cin >> N >> K;
        long* ls_rs = get_ls_rs(N, K);
        long rs = ls_rs[0];
        long ls = ls_rs[1];
        cout << "Case #" << test << ": " << rs << " " << ls << endl;
    }

    return 0;
}