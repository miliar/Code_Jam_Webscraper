#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;

int main(){
    int n;
    string input;
    int k;
    bool IMPOSSIBLE;
    long long int flip;
    int c_counter = 0;
    cin >> n;
    while (n--) {
        c_counter++;
        cin >> input;
        cin >> k;
        flip = 0;
        for (int i = 0; i < input.length()-k+1; i++) {

            if (input[i] == '-') {
                flip++;
                for (int j = i; j < i+k; j++)
                    if (input[j] == '-')
                        input[j] = '+';
                    else if (input[j] == '+')
                        input[j] = '-';
            }
        }
        IMPOSSIBLE = false;
        for (int i = input.length()-k; i < input.length(); i++)
            if (input[i] == '-') {
                IMPOSSIBLE = true;
                break;
            }
        if (IMPOSSIBLE)
            printf("Case #%d: IMPOSSIBLE",c_counter);
        else
            printf("Case #%d: %lld",c_counter,flip);
    cout<<endl;
    }
}
