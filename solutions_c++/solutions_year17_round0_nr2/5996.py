#include <iostream>
#include <string>

using namespace std;


int main() {
    int T;
    string s;

    cin >> T;

    for(int q = 1; q <= T; q++){

        cin >> s;

        int max = 0;

        for (int i = 0; i < s.length(); i++){

            if(s[i] > s[max]){
                max = i;
            }else if(s[i] < s[max]){

                s[max] =  (char)((int)s[max] -1);

                for(int j = max+1; j < s.length(); j++){
                    s[j] = '9';
                }
            }
        }

        char* ptr;
        for(int i = 0; i < s.length(); i++){
            if(s[i] != '0'){
                ptr = &s[i];
                break;
            }
        }
        cout << "Case #" << q << ": " << ptr << endl;


    }

    return 0;
}

