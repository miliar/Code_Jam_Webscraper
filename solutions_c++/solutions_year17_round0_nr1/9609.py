#include <bits/stdc++.h>
#include <string>
using namespace std;

int main(){
int loop;
string characters;
int flip;
int check = 0;
int minuses = 0;
int result[100];

cin >> loop;

for(int i = 0; i < loop; i++){
    cin >> characters;
    cin >> flip;
    size_t minuses = count(characters.begin(), characters.end(), '-');
    check = 0;
    if(size_t(minuses) == 0){
        result[i] = 0;
    }
    while(size_t (minuses) > 0){
        size_t found = characters.find("-");

        for(int j = 0; j < flip; j++){
            if ((found + j) >= characters.size()){
                if (characters[found + j - flip] == '+'){
                characters[found + j - flip] = '-';
                }
                else{ characters[found + j] = '+';
                }
            }
            else{
                if (characters[found + j] == '+'){
                characters[found + j] = '-';
                }
                else{ characters[found + j] = '+';
                }
            }
        }
        check++;
        size_t minuses = count(characters.begin(), characters.end(), '-');
        if(minuses == 0){
            result[i] = check;
            break;
        }
        if(check == 2000){
            result[i] = check;
            break;
        }
    }
}

for(int m = 0; m < loop; m++){
    cout << "Case #" << (m + 1) << ": ";
    if (result[m] == 2000){
        cout << "IMPOSSIBLE" << endl;
    }
    else {cout << result[m] << endl;
    }
}
}
