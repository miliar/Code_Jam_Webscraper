#include <iostream>
#include <string.h>

using namespace std;


int main(void) {
    int T;
    unsigned long long N;
    char str[32];
    int len;
    char str_tidy[32];
    unsigned long long tidy;
    unsigned long long tmp;
    
    cin >> T;
    for (int t = 0; t < T; t++) {
        cin >> N;
        sprintf(str, "%llu", N);
        
        len = strlen(str);
        
        if (len == 1) {
            tidy = N;
            cout << "Case #" << t+1 << ": " << tidy << endl;
            continue;
        }
        
        for (int i = 0; i < len-1; i++) {
            str_tidy[i] = '9';
        }
        str_tidy[len-1] = '\0';
        tidy = atoi(str_tidy);
        
        for (int i = 0; i < len; i++) {
            str_tidy[i] = '1';
        }
        str_tidy[len] = '\0';
        tmp = atoi(str_tidy);
        if (tmp <= N) {
            tidy = tmp;
        }
        
        int start = 0;
        while (start < len) {
            if (str_tidy[start] == '9') break;
            
            for (int j = start; j < len; j++) {
                str_tidy[j]++;
            }
            tmp = atoi(str_tidy);
            if (tmp <= N) {
                tidy = tmp;
            } else {
                for (int j = start; j < len; j++) {
                    str_tidy[j]--;
                }
                start++;
            }
        }
        
        cout << "Case #" << t+1 << ": " << tidy << endl;
    }
    
    return 0;
}
