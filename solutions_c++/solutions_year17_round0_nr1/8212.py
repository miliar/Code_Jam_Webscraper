#include<bits/stdc++.h>
using namespace std;

int N, K, T;
string nuevo;

bool happysides(string row){
    for(int i=0; i<row.size(); i++){
        if(row[i] == '-') return false;
    }
    return true;
}

int flips(string row){
    int rowsize = row.size();
    int cont = 0;
    for(int i=0; i<=rowsize-K; i++){
        if(row[i] == '-'){
            cont++;
            for(int j=i; j<i+K; j++){
                if(row[j] == '+') row[j] = '-';
                else row[j] = '+';
            }
            if(happysides(row)){
                return cont;
            }
        }

    }
    return -1;
}

int main() {

    ifstream cin("A-large.in");
    ofstream cout("A-output-large.txt");

    string row, nuevo;
    cin >> T;
    for(int t=1; t<=T; t++){
        cin >> row >> K;
        if(happysides(row)){
            cout << "Case #" << t << ": " << 0 << endl;
        } else {
            int res = flips(row);
            if(res > 0){
                cout << "Case #" << t << ": " << res << endl;
            } else {
                cout << "Case #" << t << ": IMPOSSIBLE" << endl;
            }
        }

    }
}
