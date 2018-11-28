#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;
#define MAX 19

long long toNumber(string s){
    long long n = 0;
    int i, len = s.size();
    for(i = 0; i < len; i++)
        n = n * 10 + (s[i] - '0');
    return n;
}

long long tidyNumber(string s){
    int i, j, k, lenLastNumber, len = s.size();
    char lastDigit;
    string lastNumber = "", aux;
    for(i = 0; i < len; i++)
        lastNumber += "1";

    if(toNumber(lastNumber) > toNumber(s)){
        lastNumber = "";
        for(i = 0; i < len - 1; i++)
            lastNumber += "9";
    }

    lenLastNumber = lastNumber.size();
    lastDigit = lastNumber[0];
    for(i = 0; i < lenLastNumber; i++){
        aux = lastNumber;
        for(j = lastDigit - '0'; j <= 9; j++){
            for(k = i; k < lenLastNumber; k++)
                aux[k] = char(j + '0');
            if(toNumber(aux) <= toNumber(s))
                lastNumber = aux;
            else
                break;
        }
        lastDigit = lastNumber[i];
    }

    return toNumber(lastNumber);
}

void solve(){
    int T, t;
    string number;
    cin >> T;
    for(t = 1; t <= T; t++){
        cin >> number;
        printf("Case #%d: ", t);
        cout << tidyNumber(number) << endl;
    }
}

int main(){
    solve();
    return 0;
}
