#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <set>
#include <math.h>       /* log10 */
using namespace std;






bool checkTidy(long long number){
    int lastDigit,lastLastDigit;
    lastLastDigit = number%10;
    if (!lastLastDigit) return false;
    while (number) {
        lastLastDigit = number%10;
        number/=10;
        lastDigit =  number%10;
        if (lastDigit%10>lastLastDigit) return false;

    }
    return true;
}


int main() {
    freopen("B-small-attempt0.in", "r", stdin);


//    freopen("A-large-practice.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int caseNum;
    long long N;

    cin >> caseNum;
    for (int i = 0; i < caseNum; i++) {
        cin >> N;
        for (long long j=N; j>=0; j--){
            if (checkTidy(j)){
                cout<<"Case #" << i + 1 << ": " << j << endl;
                break;
            }
        }
    }




//
//    cout<<checkTidy(132)<<endl;
//    cout<<checkTidy(1000)<<endl;
//    cout<<checkTidy(7)<<endl;
//    cout<<checkTidy(111111111111111110)<<endl;
    return 0;
}
