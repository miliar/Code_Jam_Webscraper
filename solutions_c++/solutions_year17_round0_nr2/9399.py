#include <bits/stdc++.h>

using namespace std;

int findLowestDecreasingPos(string N){
    int lowestPos = -1;
    for(int i = 1; i < N.length(); i++){
        if(N[i] < N[i-1]){
            lowestPos = i;
            break;
        }
    }
    return lowestPos;
}

string makeIncreasing(string N){
    int indeks = findLowestDecreasingPos(N);

    if(indeks == -1)
        return N;
    else{
        int lowestPos = indeks;
        long long temp = 0;
        for(int i = 0; i < lowestPos; i++){
            temp = temp * 10 + ((int)N[i]-(int)'0');
        }
        temp -= 1;
        string newN = "";
        while(temp > 0){
            newN = (char)(temp%10 + (int)'0') + newN;
            temp /= 10;
        }
        for(int i = lowestPos; i < N.length(); i++) newN += '9';
        indeks = findLowestDecreasingPos(N);
        if(indeks == -1)
            return newN;
        else return makeIncreasing(newN);
    }
}

string removeLeadingZero(string N){
    int i = 0;
    while(N[i] == '0' && i < N.length()-1) ++i;
    return N.substr(i);
}


int main(){
    string N;

    ios_base::sync_with_stdio(false);
    //cin.tie(0);
    int T;
    cin >> T;
    for(int tc = 1; tc <= T; tc++){
        cin >> N;

        cout << "Case #" << tc << ": " << removeLeadingZero(makeIncreasing(N)) << '\n';
    }
    return 0;
}
