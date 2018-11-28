#include <iostream>
#include <string>

using namespace std;

int findNeg(const string &s);
void flip(string &s, const int K);
int counter;
bool good;

int main() {

    int T, K;
    string S;

    cin >> T;

    for(int q = 1; q <= T; q++){
        counter = 0;
        cin >> S >> K;


        flip(S, K);
        if(!good){
            cout << "Case #" << q << ": IMPOSSIBLE" << endl;
        }else{
            cout << "Case #" << q << ": " << counter << endl;
        }


    }

    return 0;
}

int findNeg(const string &s){

    for(int i = 0; i < s.length(); i++){
        if(s[i] == '-'){
            return i;
        }
    }

    return -1;
}

void flip(string &s, const int K){

    int k = findNeg(s);
    int x = (s.length() - K);
    if(k > x){
        good = false;
        return;
    }else if(k == -1){
        good = true;
        return;
    }else{
        for(int i = k; i < k + K; i++){
            if(s[i] == '+'){
                s[i] = '-';
            }else{
                s[i] = '+';
            }
        }
        counter++;
    }

    flip(s, K);

}