#include <iostream>
#include <cstdio>

using namespace std;

double timeToFinish(long* S, long* K, int n, int i, long D){
    long distance = D - K[i];
    double timeToArrive = distance/((double)S[i]);

    if(i == n-1){
        return timeToArrive;
    }else{
        double timeNextHorse = timeToFinish(S, K, n, i+1, D);
        return timeNextHorse > timeToArrive? timeNextHorse: timeToArrive;
    }
}

int main(){
    int T;
    cin >> T;

    for (int c = 0; c < T; c++) {
        long D, N;

        cin >> D;
        cin >> N;

        long K[N];
        long S[N];

        for(int i = 0; i < N; i++){
            cin >> K[i];
            cin >> S[i];
        }

        double time = timeToFinish(S, K, N, 0, D);

        double speed = D/time;

        printf("Case #%d: %f \n", c+1, speed);

        // cout << "Case #" << (c+1)<< ": " << speed << endl;
    }
}
