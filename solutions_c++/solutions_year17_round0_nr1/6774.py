#include <iostream>
#include <string>

using namespace std;

int flip(string pancakes, int K, int acc){
    int L = pancakes.length();

    int i;
    for(i = 0; i < L; i++){
        if(pancakes[i] == '-'){
            break;
        }
    }
    if(i == L){
        return acc;
    }

    if((L - i) < K){
        return -1;
    }

    string newPancakes = pancakes.substr(i);

    for(int j = 0; j < K; j++){
        if(newPancakes[j] == '-'){
            newPancakes[j] = '+';
        }else{
            newPancakes[j] = '-';
        }
    }

    return flip(newPancakes, K, acc+1);
}

int main(){
    int T;

    cin >> T;

    for(int c = 0;c < T; c++){
        string pancakes;
        int K;

        cin >> pancakes;
        cin >> K;

        int flips = flip(pancakes, K, 0);

        if(flips >= 0){
            cout << "Case #" << (c+1) << ": " << flips << endl;
        }else{
            cout << "Case #" << (c+1) << ": IMPOSSIBLE" << endl;
        }
    }
}
