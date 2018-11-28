#include <bits/stdc++.h>

#define MAXN 1002

#define cin fin
#define cout fout

using namespace std;

ifstream fin("B-small-attempt1.in");
ofstream fout("B-small-attempt1.out");

int caseno;
int T, N, C, M;
int P, B;
int seat[2][MAXN];

int minRides, minProm;

int findNextSeat(int target) {
    int retidx=0, maxpop=-1;
    for (int i=1; i<=N; i++) if (i != target) {
        if (seat[0][i] > maxpop && seat[1][i] > 0) {
            maxpop = seat[0][i];
            retidx = i;
        }
    }

    if (retidx == 0)
        if (seat[1][target] != 0 && target > 1) {
            retidx = target;
            minProm ++;
        }
    return retidx;
}

void process() {
    minProm = 0;
    minRides = 0;

    for (int i=1; i<=N; i++) {
        while (seat[0][i] > 0) {
            int x = findNextSeat(i);
            seat[1][x] --;
            seat[0][i] --;
            minRides ++;
        }
    }

    for (int i=1; i<=N; i++)
        minRides += seat[1][i];
}

int main()
{
    cin >> T;

    for (caseno=1; caseno<=T; caseno++) {
        memset(seat, 0, sizeof seat);

        cin >> N >> C >> M;
        for (int i=0; i<M; i++) {
            cin >> P >> B;
            seat[B-1][P] ++;
        }

        process();

        cout << "Case #" << caseno << ": " << minRides << " " << minProm << endl;
    }

    return 0;
}
