using namespace std;

#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <string.h>
#include <math.h>
#include <stdlib.h>

typedef pair<int, int> ii;
typedef vector<int> vi;

int t;
//long long n;
string line;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.txt", "w", stdout);
    scanf("%d", &t);
    for (int r = 1; r <= t; r++) {
        cin >> line;
        int l = (int)line.size();
        for (int i = l-1; i >= 1; i--) {
            for (int j = i; j >= 0; j--) {
                if (line[j] > line[i]) {
                    //cout << line << " ";
                    for (int k = i; k < l; k++) {
                        line[k] = '9';
                    }
                    //cout << line << endl;
                    line[i-1] = line[i-1] - 1; //attention si 0 ??
                    break;
                }
            }
        }
        printf("Case #%d: ", r);
        int first = 0;
        for (int i = 0; i < l; i++) {
            if (line[i] > '0') {
                first = i;
                break;
            }
        }
        for (int i = first; i < l; i++) {
            printf("%c", line[i]);
        }
        printf("\n");
    }

}

