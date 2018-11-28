#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("largeoutput.txt", "w", stdout);
    int T;
    cin >> T;
    for(int r=0;r<T;r++){
        string s;
        cin >> s;
        string z = "";
        if(s.size() == 1) z = s;
        else{
            for(int i=0;i<s.size()-1;i++){
                if(s[i] > s[i+1]){
                    if(s[i] == '1'){
                        for(int j=0;j<s.size()-1;j++) z += '9';
                        break;
                    }
                    else{
                        if(i == 0){
                            z += (s[i] - 1);
                            for(int j=0;j<s.size()-1;j++) z += '9';
                            break;
                        }
                        else {
                            int j = i;
                            while(s[j] == s[j-1]) j--;
                            for(int k = 0;k<j;k++) z += s[k];
                            z += (s[j] - 1);
                            for(int k=j+1;k<s.size();k++) z+= '9';
                            break;
                        }
                    }
                }
            }
        }
        if(z == "") z = s;
        cout << "Case #" << r+1 << ": " << z << endl;
    }
    
    return 0;
}
