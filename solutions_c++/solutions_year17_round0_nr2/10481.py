#include <iostream>
#include <string>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {

    int numTests, input, temp, output = 0;
    int digits[32];
    

    
    cin >> numTests;
    
    for(int a = 1; a <= numTests; a++){
        for(int b = 0; b < 32; b++)
            digits[b] = 0;
        
        cin >> input;
        temp = input;
        
        int i = 0;
        
        while(temp > 0){
            digits[i] = temp % 10;
            temp /= 10;
            //cout << digits[i] << endl;
            i++;
        }
        
        if(i == 1){
            cout << "Case #" << a << ": " << input << endl;
            input = 0;
            output = 0;
            continue;
        }
        
        for(int j = i-1; j > 0; j--){
            if(digits[j] <= digits[j-1])
                continue;
                
            digits[j] -= 1;
            if(digits[j+1] > digits[j]){
                digits[j+1] -=1;
                digits[j] = 9;
            }
            for(int k = j-1; k >= 0; k--)
                digits[k] = 9;
            break;
        
        }
        
        for(int x = i-1; x >=0; x--){
            //cout << digits[x] << endl;
            output *= 10;
            output += digits[x];
        }
        
        cout << "Case #" << a << ": " << output << endl;
        
        input = 0;
        output = 0;
    }

}
