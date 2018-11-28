#include <bits/stdc++.h>

using namespace std;

typedef struct{
    double max_speed;
    double start;
} horse_t;

void solve(){
    int D, N, n;
    horse_t* horses;
    double last_finish, this_finish;

    cin >> D;
    cin >> N;

    /* Read in all horses */
    horses = (horse_t *) malloc(n * sizeof(horse_t));
    last_finish = 0;
    for (n = 0; n < N; ++n){
        cin >> horses[n].start;
        cin >> horses[n].max_speed;
        this_finish = (D - horses[n].start) / horses[n].max_speed;
        if (this_finish > last_finish)
            last_finish = this_finish;
    }

    printf("%.7lf", D / last_finish);
}

int main(int argc, char** argv){
    int T, t;

    cin >> T;

    for (t = 1; t <= T; ++t){
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
