#include <bits/stdc++.h>

using namespace std;

int main(){
    ifstream input("a.in");
    ofstream output;
    output.open ("a.out");
    unsigned long long T;

    input >> T;
    for(unsigned int i = 0; i < T; i++) {
        int D, N;
        input >> D >> N;
        double times[N];
        int K[N];
        int S[N];
        input >> K[0] >> S[0];
        times[0] = (double)(D - K[0]) / (double)S[0];
        for(int j = 1; j < N; j++) {
            input >> K[j] >> S[j];
            times[j] = max(times[j - 1], (double)(D - K[j]) / (double)S[j]);
        }
        cout.precision(6);
        output << "Case #" << (i + 1) << ": " << fixed << ((double)D / times[N - 1]) << endl;
    }
    output.close();
    return 0;
}
