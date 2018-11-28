/*
    Problem A: Oversized Pancake Flipper
    @author: Christopher W. Frost
*/

#include<iostream>
#include<string>
using namespace std;

bool isHappy(const string& s){
    for(auto z : s)
        if(z == '-')
            return false;
    return true;
}

string makeFlip(string& s){
    for(auto &z : s){
        if(z == '-')
            z = '+';
        else
            z = '-';
    }
    return s;
}

void numFlips(string& stack, int K, int count){
    if(isHappy(stack)){
        cout << count << '\n';
        return;
    }
    if(K > stack.length()){
        cout << "IMPOSSIBLE\n";
        return;
    }
    
    int i = stack.length() - 1;
    while(stack[i] == '+')
        i--;
    
    if(i != stack.length() - 1){
        stack = stack.substr(0, i+1);
        if(K > stack.length()){
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    string temp = stack.substr(stack.length()-K, K);
    stack = stack.substr(0, stack.length()-K) + makeFlip(temp);
    numFlips(stack, K, count+1);
}

int main(){
    int t, K;
    string stack;
    cin >> t;
    for(int i = 1; i <= t; i++){
        cin >> stack >> K;
        cout << "Case #" << i << ": ";
        numFlips(stack, K, 0);
    }
}
