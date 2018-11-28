#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;

int T,N;
char *message = "Case #";
int tidy;
int tempLen;
void checkZero();
void getTidy();

string input;
string result;

int main() {

    cin>>T;
    for(int t=0;t<T;t++){
        cin>>input;
        getTidy();
        cout<<message<<t+1<<": ";
        for(int k=0;k<tempLen;k++) cout<<result[k];
        cout<<endl;
    }
    return 0;
}
void getTidy() {
    result = input;
    int len = input.size();
    tempLen = len;

    for(int i=0; i<len-1; i++) {
        if(input[i] == '1' && input[i+1] == '0') {
            tempLen--;

            for(int t=0;t<tempLen;t++) result[t] = '9';
            break;
        }

        else  {
            int L,R;
            L = input[i] -48;
            R = input[i+1] - 48;

            if(L>R) {
                L-=1;
                result[i] = L+48;

                if(i>0 && result[i] < result[i-1]) {
                    for(int k=i-1; k>=0; k--) {
                            if(result[k] > result[k+1]) {
                                    result[k] -= 1;
                                    result[k+1] = '9';
                            }
                    }
                }

                for(int k=i+1; k<tempLen; k++) result[k] = '9';
                break;
            }
        }
    }
}
