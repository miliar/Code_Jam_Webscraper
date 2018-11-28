#include <iostream>
#include <string>

using namespace std;

int tryFlip(string s, int k){
    int a = 0;
    int count = 0;
    while(a+k <= s.size()){
        if(s.at(a) == '-'){
            for(int i=0 ; i<k ; i++){
                if(s.at(a+i) == '-') s.at(a+i) = '+';
                else if(s.at(a+i) == '+') s.at(a+i) = '-';
            }
            count++;
        }
        a++;
    }
    for(int i=a; i<s.size(); i++){
        if(s.at(i) == '-'){
            return -1;
        }
    }
    return count;
}

int main(){
    int testNum;
    string s[100];
    int k[100];
    cin >> testNum;
    for(int i=0; i<testNum; i++){
        cin >> s[i] >> k[i];
    }
    
    for(int i=0; i<testNum; i++){
        int result = tryFlip(s[i], k[i]);
        if(result == -1) cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
        else cout << "Case #" << i+1 << ": " << result << "\n";
    }
    return 0;
}