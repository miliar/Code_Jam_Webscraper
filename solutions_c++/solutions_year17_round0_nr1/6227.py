#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i = 0; i < t; ++i){
        string input;
        int flip;
        cin >> input;
        cin >> flip;
        int impossible = 0;
        int flip_count = 0;
        cout << "Case #" << i+1 << ": ";
        for(unsigned int j = 0; j < input.size(); ++j){
            if(input[j] == '-'){
                for(int k = 0; k < flip; ++k){
                    if(j+k >= input.size()){
                        impossible = 1;
                        j = input.size();
                        break;
                    }
                    if(input[j+k] == '+'){
                        input[j+k] = '-';    
                    } else if (input[j+k] == '-'){
                        input[j+k] = '+';
                    }
                    
                }
                flip_count++;
            }
        }
        if(impossible){
            cout << "IMPOSSIBLE";
        } else {
            cout << flip_count;
        }
        cout << endl;
    }
}
