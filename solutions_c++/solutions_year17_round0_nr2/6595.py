#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void setNines(string &number, int idx) {
    for(; idx<number.length(); idx++)
        number[idx] = '9';
}

string findMaxTidyNumber(string number) {
    int length = number.length();
    int l = number.length()-1;
    while(l>0) {
        if(number[l] < '0') {
            number[l] = '9';
            if(l+1 < length && number[l+1]!='9')
                setNines(number, l+1);
            number[l-1]--;
        }
        if(number[l] < number[l-1]){
            number[l] = '9';
            if(l+1 < length && number[l+1]!='9')
                setNines(number, l+1);
            number[l-1]--;
        }
        l--;
    }
    while(number[0] == '0') {
            number = number.substr(1, number.length());
    }
    return number;
}

int main()
{
    int T;
    ifstream input("input.txt");
    ofstream output("output.txt");

    input >> T;

    string N;
    for(int i=0; i<T; i++){
        input >> N;
        output << "Case #" << i+1 << ": " << findMaxTidyNumber(N) << endl;
    }
    return 0;
}
