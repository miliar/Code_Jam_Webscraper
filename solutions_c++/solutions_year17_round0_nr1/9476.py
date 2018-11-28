#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

int main() {
    int t,k,i,n,j,totalCount,possible,l;
    char s[10002];
    ifstream input;
    ofstream output;
    input.open("input.txt");
    output.open("output.txt");
    input >> t;
    for(l = 1;l <= t ; l++) {
        input >> s;
        input >> k;
        totalCount = 0;
        possible = 1;
        n =  strlen(s);
        for(i = 0; i <= n - k; i++) {
            if(s[i] == '-') {
                totalCount++;
                for(j = 0 ; j < k;j++) {
                    if(s[i+j] == '-') {
                        s[i+j] = '+';
                    } else {
                        s[i+j] = '-';
                    }
                }
            }
        }

        for( i = n-k+1; i < n; i++) {
            if(s[i] == '-') {
                possible = 0;
                break;
            }
        }

        if(possible) {
            output <<"Case #" << l << ": " << totalCount << endl;
        } else {
            output<<"Case #" << l << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

