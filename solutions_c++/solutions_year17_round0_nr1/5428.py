#include <iostream>
#include <string.h>

using namespace std;

int main(){

    int times;
    cin >> times;

    for(int t = 0; t < times; t++){
        
        int flipper;
        string s;
        int counter = 0;
        bool possible = true;

        cin >> s >> flipper;

        cout << "Case #" << t+1 << ": ";

        for(int i = 0; i < s.length() && possible == true; i++){
            if(s[i] != '+' && i+flipper <= s.length()){
                for(int j = i; j < i+flipper; j++){
                    if(s[j] == '-'){
                        s[j] = '+';
                    }else{
                        s[j] = '-';
                    }
                }
                counter++;
            }else if(s[i] != '+' && i+flipper > s.length()){
                possible = false;
            }

        }

        if(possible == true){
            cout << counter << endl;
        }else{
            cout << "IMPOSSIBLE" << endl;
        }
    }

    return 0;
}