#include <bits/stdc++.h>

using namespace std;

int main(){
    ifstream input("b.in");
    ofstream output;
    output.open ("b.out");
    unsigned long long T;

    input >> T;
    for(unsigned int i = 0; i < T; i++) {
        int N;
        int colors[6]; // R Y B O G V
        input >> N >> colors[0] >> colors[3] >> colors[1] >> colors[4] >> colors[2] >> colors[5];
        int solution[N];
        if(max(max(colors[0], colors[1]), colors[2]) > (N / 2)) {
            output << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
        } else {
            output << "Case #" << (i + 1) << ": ";
            for(int j = 0; j < N; j++) {
                solution[j] = (colors[0] >= colors[1] && colors[0] >= colors[2]) ?  0 : colors[1] >= colors[2] ? 1 : 2;
                if(j && solution[j] == solution[j - 1]) {
                    if(solution[j] == 0) solution[j] = (colors[1] >= colors[2]) ? 1 : 2; else
                    if(solution[j] == 1) solution[j] = (colors[0] >= colors[2]) ? 0 : 2; else
                    if(solution[j] == 2) solution[j] = (colors[0] >= colors[1]) ? 0 : 1;
                }
                if(j && solution[j] != solution[0] && solution[j - 1] != solution[0] && colors[solution[0]] == colors[solution[j]]) {
                    solution[j] = solution[0];
                }
                colors[solution[j]]--;
                if(solution[j] == 0) output << 'R';
                if(solution[j] == 1) output << 'Y';
                if(solution[j] == 2) output << 'B';
            }
            output << endl;
        }
    }
    output.close();
    return 0;
}
