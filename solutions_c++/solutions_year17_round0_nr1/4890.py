

#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <iostream>
#include <string>

using namespace std;

std::string panCakeFlip(std::string str, int K){
    
    int flipCount = 0;
    
    
    for (int i =0; i<str.size(); i++) {
        if (str.at(i)=='-') {
            if (i+K-1>=str.length()) {
                return "IMPOSSIBLE";
            }
            flipCount++;
            for (int j=i; j<i+K; j++) {
                if (str.at(j)=='-')
                    str.replace(j, 1, 1,'+');
                else
                    str.replace(j, 1, 1,'-');
            }
        }
        
        
    }
    
    return std::to_string(flipCount);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    
    int T;
    std::string S;
    int K;
    cin>> T;
    
    for(int i =1 ; i<=T;i++){
        cin >> S;
        cin >> K;
        cout << "Case #" << i << ": " << panCakeFlip(S,K)  << endl;
        
    }
    
    
    
    
    return 0;
}

