#include <iostream>
#include <string.h>

using namespace std;

int main(){

    int times;
    cin >> times;
    for(int t = 0; t < times; t++){
        string s;
        cin >> s;

        cout << "Case #" << t+1 << ": ";
        for(int i = 1 ; i < s.length(); i++){
            if(s[i] < s[i-1]){
                for(int j = i; j < s.length(); j++){
                    s[j] = '9';
                }

                bool exit = false;
                for(int j = i-1; j >= 0 && exit == false; j--){
                    if(j == 0){
                        s[j]--;
                        exit = true;
                    }else{
                        if(s[j]-1 < s[j-1]){
                            s[j] = '9';
                        }else{
                            s[j]--;
                            exit = true;
                        }
                    }
                }
            }
        }

        bool done = false;

        for(int i = 0; i < s.length(); i++){
            if(s[i] != '0' && done != true){
                cout << s[i];
                done = true;
            }else if(done == true){
                cout << s[i];
            }
    }
    cout << endl;
    }

    return 0;
}