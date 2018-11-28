#include<iostream>
#include<string>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        string s;
        cin >> s;
        for(auto j = s.begin(); j < s.end() - 1; j++){
            if(*j > *(j + 1)){
                if(*j == 1){
                    *s.begin() = '0';
                    for(auto k = s.begin() + 1; k < s.end(); k++)*k = '9';
                    break;
                }
                while(j > s.begin()){
                    if(*j != *(j - 1))break;
                    j--;
                }
                *j = *j - 1;
                for(j += 1;j < s.end(); j++)*j = '9';
                break;
            }
        }
        auto j = s.begin();
        while(*j == '0')j++;
        cout << "Case #" << i << ": ";
        for(;j < s.end(); j++)cout << *j;
        cout << '\n';
    }

    return 0;
}
