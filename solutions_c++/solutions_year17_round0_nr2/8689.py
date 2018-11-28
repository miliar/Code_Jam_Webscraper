#include <iostream>
using namespace std;
#define MAX_TEST 100

int main() {
    int T;
    cin >> T;
    string str[MAX_TEST];
    string res_str[MAX_TEST];

    for(int i=0; i<T; i++) {
        cin >> str[i];
        int len = str[i].length();
        res_str[i] = str[i];
        int flg = -1;

        for(int j=0; j<len-1; j++) {
            if(str[i][j] > str[i][j+1]) {
                flg = j;
                break;
            }
        }

        while(flg>0 && str[i][flg] == str[i][flg-1]) {
            flg--;
        } 

        if(flg >=0){
            res_str[i][flg] = res_str[i][flg] - 1;
            for(int k=flg+1; k<len; k++) {
                res_str[i][k] = '9';
            }

            int zero = -1;
            for(int k=0; k<len && res_str[i][k] == '0'; k++) {
                zero = k;
            }

            if (zero != -1) {
                int c=0;
                for(int k=zero+1; k<len ; k++) {
                    res_str[i][c++] = res_str[i][k];
                }
                 res_str[i][c] = '\0';
            }

        }
    } //for(int i=0; i<T; i++)

    for(int p=0; p<T; p++)
        cout << "Case #"<< p+1 << ": " << res_str[p] << "\n";
} // main()



