#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t, i, len, j, k;
    cin >> t;
    string num;
    for(int test=1; test<=t; test++){
        cin >> num;
        len = num.length();
        for(k=0; k<18; k++){
            for(i=0; i<len-1; i++){
                if(num[i] > num[i+1]){
                    num[i] = num[i]-1;
                    for(j=i+1; j<len; j++){
                        num[j] = '9';
                    }
                }
            }
        }
        cout << "CASE #" << test << ": " << stol(num) << endl;
    }
    return 0;
}
