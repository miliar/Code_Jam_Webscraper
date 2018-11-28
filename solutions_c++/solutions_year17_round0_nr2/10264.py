#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

int main() {
    int t, n, m;
    bool flag = true;
    ifstream input;
    input.open("B-small-attempt0.in");
    ofstream output;
    output.open("Output.out");
    if(input.is_open()) {
        input >> t;
        for(int l = 1; l <= t; l++) {
            input >> n;
            for(int i = n; i > 0; i--) {
                if(i == 1000) {
                    i--;
                }
                flag = true;
                if(n <= 9) {
                    m = n;
                    break;
                }
                int digit[3] = { 0 };
                int tmp = i;
                int s = 0;
                while(tmp > 0) {
                    int d = tmp % 10;
                    digit[s] = d;
                    s++;
                    tmp = tmp/10;
                }
                for(int j = 0; j < s - 1; j++) {
                    if(digit[j] >= digit[j + 1]) {
                        flag = true;
                        continue;
                    }
                    if(digit[j] < digit[j + 1]) {
                        flag = false;
                        break;
                    }
                }
                if(flag) {
                    m = i;
                    break;
                }
            }
            if (output.is_open()) {
                output << "Case #" << l << ": " << m << endl;
            }
            else
                cout << "No output";
        }
    }
    else
        cout << "No Input";
    input.close();
    output.close();
    return 0;
}
