#include <iostream>
#include <string>
using namespace std;

int main(){
    int t;
    cin >> t;
    string input;
    
    for(int i = 1; i <= t; ++i){

        cin >> input;

        int left,right;
        for(unsigned int x = 0; x < input.size(); ++x){ // ok i had to eat dinner so lets just do this lol
            left = input[0];
            for(unsigned int j = 1; j < input.size(); ++j){
                right = input[j];
                if(left > right){
                    input[j-1]--;
                    for(unsigned int k = j; k < input.size(); ++k){
                        input[k] = '9';
                    }
                }
                left = input[j];
            }
        }
        while(input[0] == '0'){
            input.erase(0,1);
        }
        cout << "Case #" << i << ": " ;
        cout << input;
        cout << endl;
    }
    return 0;
}
