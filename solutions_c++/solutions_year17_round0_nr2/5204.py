#include <bits/stdc++.h>
using namespace std;

int TC;
char arr[25];

int main() {
    scanf("%d", &TC);
    for (int zz = 1; zz <= TC; zz++) {
        scanf("%s", arr);
        int len = strlen(arr);

        bool change = true;
        while (change) {
            change = false;
            for (int i = 0; i < len-1; i++) {
                if (arr[i] > arr[i+1]) {
                    change = true;
                    arr[i] = arr[i]-1;
                    for (int j = i+1; j < len; j++)
                        arr[j] = '9';
                }
            }
        }
        printf("Case #%d: ", zz);
        bool found = false;
        for (int i = 0; i < len; i++) {
            if (found) printf("%c", arr[i]);
            else{
                if (arr[i] != '0') {
                    found = true;
                    printf("%c", arr[i]);
                }
            }
        }
        printf("\n");
    }
}