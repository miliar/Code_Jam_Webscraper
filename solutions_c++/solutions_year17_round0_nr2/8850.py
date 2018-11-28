#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void getDigits (std::vector<int>& digits, unsigned int num);
bool isSorted (std::vector<int>& numbers);

int main() {
    int t,N;
    bool tidy;
    vector<int> Numbers;
    
    cin >> t;
    for (int i =1 ; i<=t; ++i){
        
        cin>> N;
        for (int j = N ; j >=1; j--){
            tidy = false;
            getDigits(Numbers, j);
            tidy = isSorted(Numbers);
            if (tidy){
                cout << "Case #"<<i<<": "<<j<<endl;
                break;
            }
        }
        if (!tidy){
            cout << "Case #"<<i<<": no tidy numbers"<<endl;
        }
    }
	return 0;
}

bool isSorted (std::vector<int>& numbers){
    int prevN;
    prevN = numbers[0];
    for(std::vector<int>::size_type i = 1; i != numbers.size(); i++) {
        if( numbers[i] < prevN) return false;
        prevN = numbers[i];
    }
    return true;
}

void getDigits (std::vector<int>& digits, unsigned int num){
    digits.clear();
    if(num > 9){
        getDigits(digits, num/10);
    }
    digits.push_back(num%10);
}
