

#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <iostream>
#include <string>

using namespace std;

void greatestTidy(std::string& number){
    
    
    int x = 0;
    int y =0;
    int k=-1;
    
    if (number.length()<2) {
        EXIT_SUCCESS ;
    }
    
    
    for(int i=1;i<number.size();i++){
        
        x = number.at(i-1) - '0';
        y = number.at(i)-'0';
        
        if ( y < x ) {
            k=i-1;
            break;
        }
    }
    
    if (k!=-1) {
        
        char ch = '0'+x-1;
        number.replace(k, 1, 1,ch);
        
        for(int i=k+1;i<number.size();i++){
            number.replace(i, 1, 1,'9');
            
        }
        
    }
    
    if(k==-1){
        if (number.at(0) == '0') {
            number.erase(0,1);
        }
        EXIT_SUCCESS;
    
    }
    else
        greatestTidy(number);
    
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    
    int T;
    string N;
    cin>> T;
    
    for(int i =1 ; i<=T;i++){
        cin >> N;
        greatestTidy(N);
        cout << "Case #" << i << ": " << N << endl;
        
    }
    
    
    
    
    return 0;
}

