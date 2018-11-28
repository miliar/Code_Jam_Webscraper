#include <iostream>
#include <algorithm>
#include <climits>
#include <set>

using namespace std;

multiset<int> digitsBefore;

void prepare(string & number){
    int i=0;
    bool ninenine = false;
    for(; i < number.size() -1; ++i){
        if(number[i] > number[i+1]){
            number[i] = number[i] -1;
            ninenine = true;
            break;
        }
    }

    ++i;

    for(; i < number.size(); ++i){
        number[i] = '9';
    }

    if(number[0] == '0'){
        number.erase(0,1);
    }
}

void findLastTidyNumber(string & number){

    prepare(number);

    for(char c : number){
        digitsBefore.insert((c -'0'));
    }

//    auto  eq = digitsBefore.equal_range(1);
//    cout << "dist "<< (distance(eq.first, eq.second) )<< endl;
//
//    digitsBefore.erase(digitsBefore.find(1));
//
//    if(digitsBefore.empty()){
//        cout << "pusty set\n";
//    }

    bool overFlow = false;

    for(int i = number.size() -1; i >=0; --i){
        int currentDigit = number[i] - '0';

        digitsBefore.erase(digitsBefore.find(currentDigit));

        if(overFlow){
            currentDigit-=1;
            overFlow = false;
        }

        int maxFromDigitsBefore = 0;

        if(i > 0) {
            maxFromDigitsBefore = *digitsBefore.rbegin();
        }

        if (currentDigit < maxFromDigitsBefore) {
            overFlow = true;
            currentDigit = 9;

            if(i==0){
                currentDigit=0;
            }
        }

        number[i] = (char) currentDigit + '0';
    }

    if(number[0] == '0'){
        number.erase(0,1);
    }
}

int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    string number;
    for(int caseId = 1; caseId <= t; ++caseId ){
        cin >> number;

        findLastTidyNumber(number);

        cout << "Case #"<< caseId << ": " << number << "\n";

    }

    return 0;
}