#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>

using namespace std;


int main()
{
    int i,j, k;
    int T;
    int ok;
    char aux;
    long long sub;
    long long res;
    string number;
    cin >> T;
    for(i=1; i<=T; i++){
        cin >> number;
        for (j=0, ok=1; j<number.size() - 1; j++)
            if (number[j] > number[j+1]){
                ok = 0;
                break;
            }
        if (ok)
            cout << "Case #" << i << ": " << number << "\n";
        else {
            for (k=j-1, aux=number[j]; k >=0; k--)
                if (number[k] != aux)
                    break;
            if (k == j-1)
                j++;
            else
                j=k+2;
            res = stol(number);
            sub = stol(number.substr(j,number.size()));
            res = res - sub -1;
            cout << "Case #" << i << ": " << res << "\n";
        }
    }
    return 0;
}
