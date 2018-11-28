#include <iostream>
#include <string>

#include <fstream>

using namespace std;

void tidy (string &s, int i){
    int a = s[i] - '0';
    int b = s[i+1] - '0';

    if (b >= a) return;


}

string tidyNumber(string s){
    int len = s.length();
    if (len == 1){
        return s;
    }
    else {
        for (int i = len-1; i > 0; i--){
            if (s[i] == '0' || s[i] == '1'){
                for (int k = i; k < len; k++) s[k] = '9';
                int k = i-1;
                while (k >= 0 && s[k] <= '1'){
                    s[k] = '9';
                    k--;
                }

                if (k == -1 && s[k+1] == '9'){
                    s.erase(s.begin());
                }
                else {
                    s[k] = s[k] - 1;
                    i = k+1;
                }
            }
            else {
                if (s[i-1] > s[i]){
                    int k = i;
                    while (k < len && s[k] != '9'){
                        s[k] = '9';
                        k++;
                    }
                    s[i-1] = s[i-1] - 1;
                }
            }
        }
    }

    return s;
}

int main(){
    ifstream cin ("B-small-attempt0.in");
    ofstream cout ("output-tidy.txt");

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        string s;
        cin >> s;
        cout << "Case #" << (i+1) << ": " << tidyNumber(s) << endl;
    }
    return 0;
}
