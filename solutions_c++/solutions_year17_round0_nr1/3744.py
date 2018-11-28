#include <iostream>
#include <string>
using namespace std;

int doJob(string &S, int K);
void flipOnce(string &S, int posi, int K);

int main() {
    int caseN;
    cin >> caseN;
    for(int i = 0; i < caseN; i++){
        string S;
        int K;
        cin >> S;
        cin >> K;
        int result = doJob(S, K);
        cout << "Case #" << i + 1 << ": ";
        if(result >= 0) cout << result << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}


int doJob(string &S, int K) {
    int counter = 0;
    for(int i = 0; i <= S.length() - K; i++){
        if(S[i] == '-') {
            flipOnce(S, i, K);
            counter++;
        }
        else continue;
    }
    if(S.find("-")!= string::npos) return -1;
        else return counter;
}

void flipOnce(string &S, int posi, int K){
    for(int i = posi; i < posi + K; i++){
        (S[i] == '+') ? S[i] = '-' : S[i] = '+';
    }
}