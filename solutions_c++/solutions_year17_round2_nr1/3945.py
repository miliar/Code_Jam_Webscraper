#include<iostream>
#include<string>
#include <queue>
#include <fstream>
#include<iomanip>

using namespace std;

int main() {
    ofstream cop("op1.txt");
    ifstream cinp("in1.txt", ios::binary);
    int T, t=1;
    cinp >> T;
    for(;t <= T;t++){
        fflush(stdin);
        long D;
        int N;
        long K[N], S[N];
        cinp >> D >> N;
        double times[N], max = 0;
        for(int i=0; i<N; i++) {
            cinp >> K[i] >> S[i];
            times[i] = (1.0 * (D - K[i]))/S[i];
            if(max < times[i])
                max = times[i];
        }
        cop << "Case #" << t << ": " << std::setprecision(6) << std::fixed << D/max << endl;
    }
    return 0;
}
