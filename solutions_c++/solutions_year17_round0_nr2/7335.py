#include <iostream>
#include <cstring>
using namespace std;

int main(){
    int n;
    char digits[20];
    int j,k;
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> digits;
        if(strlen(digits) == 1){
            cout << "Case #" << i << ": " << digits << endl;
            continue;
        }
        for(j = 0; j < strlen(digits) - 1; j++){
            if(digits[j] > digits[j + 1]){
                k = j;
                while(digits[k-1] == digits[j] && (k >= 0))
                    k--;
                //update
                digits[k] = digits[k] - 1;
                for(int t = k + 1; t < strlen(digits); t++)
                    digits[t] = '9';


                cout << "Case #" << i << ": ";
                if(digits[0] == '0'){
                    for(k = 1; k < strlen(digits); k++)
                        cout << digits[k];
                    cout << endl;
                }
                else
                    cout << digits << endl;
                break;
            }
        }
        if(j == strlen(digits) - 1)
            cout << "Case #" << i << ": " << digits << endl;
    }

    return 0;
}
