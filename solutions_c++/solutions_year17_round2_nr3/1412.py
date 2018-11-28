#include<iostream>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <climits>
#include <iomanip>

using namespace std;

size_t T, N, Q, U, V;
vector<vector<int>> distances;

double best_duration(size_t position, int restant, double speed, vector<int>& autonomie, vector<double>& vitesse) {
    if(position == V) {
        return 0;
    }

    double best = SIZE_T_MAX;
    for(size_t next = 0; next < N; next++) {
        int dist = distances[position][next];
        if(dist >= 0) {
            //on garde le cheval
            if(dist <= restant) {
                double new_dur = (dist / speed) + best_duration(next, restant - dist, speed, autonomie, vitesse);
                if(new_dur < best) {
                    best = new_dur;
                }
            }
            //on change
            if(dist <= autonomie[position]) {
                int new_autonomie = autonomie[position];
                double new_vitesse = vitesse[position];
                autonomie[position] = restant;
                vitesse[position] = speed;
                double new_dur = (dist / new_vitesse) + best_duration(next, new_autonomie - dist, new_vitesse, autonomie, vitesse);
                autonomie[position] = new_autonomie;
                vitesse[position] = new_vitesse;
                if(new_dur < best) {
                    best = new_dur;
                }
            }
        }
    }

    return best;
}

int main(int argc, const char *argv[]) {
    cin >> T;

    for(size_t t = 1; t <= T; t++) {
        cin >> N >> Q;

        vector<int> autonomie(N);
        vector<double> vitesse(N);
        distances = vector<vector<int>>(N,vector<int>(N));

        for(size_t n = 0; n < N; n++) {
            cin >> autonomie[n] >> vitesse[n];
        }
        for(size_t n = 0; n < N; n++) {
            for(size_t n2 = 0; n2 < N; n2++) {
                cin >> distances[n][n2];
            }
        }

        cout << "Case #" << t << ':';
        for(size_t q = 0; q < Q; q++) {
            cin >> U >> V;
            U--;
            V--;

            cout << ' ' << fixed << setprecision(8) << best_duration(U, 0, 0, autonomie, vitesse);
        }
        cout << endl;

    }

    return 0;
}
