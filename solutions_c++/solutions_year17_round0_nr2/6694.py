#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
    freopen("B-large.in","r", stdin);
    freopen("out.txt","w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; i++){
        string str;
        cin >> str;
        unsigned long long len = str.length();
        for (unsigned long long j = 1; j<len;j++){
            if (str[len-j] < str[len-j-1]){
                for (unsigned long long k = len - j;k < len;k++){
                    str = str.replace(k,1,"9");
                }
                str[len-j-1] = str[len-j-1] - 1;
            }
        }
        if (str[0] == '0')
            str = str.erase(0,1);
        cout << "Case #"<<i+1<<": "<< str << endl;
    }
    return 0;
}
