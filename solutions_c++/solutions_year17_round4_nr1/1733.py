#include <bits/stdc++.h>

#define M_PI 3.14159265358979323846

using namespace std;

int main(){
    ifstream input("a.in");
    ofstream output;
    output.open ("a.out");
    unsigned long long T;

    input >> T;
    for(unsigned int i = 0; i < T; i++) {
        cout << "Progress " << i << " / " << (T - 1) << endl;
        int result = 0;
        int N, P;
        input >> N >> P;
        int next;
        int G[P];
        for(int j = 0; j < P; j++) G[j] = 0;
        for(int j = 0; j < N; j++) {
            input >> next;
            G[next % P]++;
        }
        result += G[0];
        G[0] = 0;
        if(P == 2) {
            result += ceil((double)(G[1]) / 2.);
        } else if(P == 3) {
            if(G[1] > G[2]) {
                result += G[2];
                G[1] -= G[2];
                result += ceil((double)(G[1]) / 3.);
            } else {
                result += G[1];
                G[2] -= G[1];
                result += ceil((double)(G[2]) / 3.);
            }
        } else {
            if(G[2] % 2) {
                result += floor((double)(G[2]) / 2.);
                if(G[1] > G[3]) {
                    result += G[3];
                    G[1] -= G[3];
                    if(G[1] >= 2) {
                        result += 1;
                        G[1] -= 2;
                    }
                    result += ceil((double)(G[1]) / 4.);
                } else {
                    result += G[1];
                    G[3] -= G[1];
                    if(G[3] >= 2) {
                        result += 1;
                        G[3] -= 2;
                    }
                    result += ceil((double)(G[3]) / 4.);
                }
            } else {
                result += G[2] / 2;
                if(G[1] > G[3]) {
                    result += G[3];
                    G[1] -= G[3];
                    result += ceil((double)(G[1]) / 4.);
                } else {
                    result += G[1];
                    G[3] -= G[1];
                    result += ceil((double)(G[3]) / 4.);
                }
            }
        }
        cout << "Case #" << (i + 1) << ": " << result << endl;
        output << "Case #" << (i + 1) << ": " << result << endl;
    }
    output.close();
    return 0;
}
