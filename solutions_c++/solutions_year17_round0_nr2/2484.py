#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main(){
    int T,c=0;
    string S;
    cin >> T;
    while(c++<T){
        cin >> S;
        if(S.length()>1){
            for(int i=S.length()-2;i>=0;i--){
                if(S[i] > S[i+1]){
                    S[i] = S[i]-1;
                    for(int j=i+1;j<S.length();j++)
                        S[j] = '9';
                }
            }
        }
        int x=0;
        while(S[x] == '0') x++;
        printf("Case #%d: %s\n",c,S.substr(x,S.length()).c_str());
    }
    return 0;
}
