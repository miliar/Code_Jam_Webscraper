#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long tmp[40];
long result[40];
char digits[200];
char sequare[200];

int isP(char *str, int len){
    for (int i = 0; i + i < len; i ++){
        if (str[i] != str[len - i - 1]) return 0;
    }
    return 1;
}

int getSequare(char *s, int len){
    memset(result, 0, sizeof(result));
    int tmpLen = 0;
    for (int i = 0; i < len; i += 8){
        long mul = 1, number = 0;
        for (int j = 0; j < 8 && i + j < len; j ++){
            number += mul * (s[i + j] - '0');        
            mul *= 10;
        }
        tmp[tmpLen ++] = number;
    }
    for (int i = 0; i < tmpLen; i ++)
        for (int j = 0; j < tmpLen; j ++)
            result[i + j] += tmp[i] * tmp[j];
    memset(sequare, '0', sizeof(sequare));
    long remainder = 0;
    for (int i = 0; i < 20; i ++){
        result[i] += remainder;
        remainder = result[i] / 100000000LL;
        result[i] %= 100000000LL;
        long t = result[i];
        for (int j = 0; j < 8; j ++){
            sequare[i * 8 + j] = t % 10 + '0';
            t /= 10;
        }
    }
    for (int i = 199; i >= 0; i --)
        if (sequare[i] != '0') return i + 1;
    return 0;
}

int checkAndOutput(int len){
    int seqLen = getSequare(digits, len);
    if (isP(sequare, seqLen)){
        for (int i = 0; i < len; i ++) printf("%c", digits[i]);
        printf("\n");
    }
}

int getNumber(int l, int r, int c1, int len){
    if (l >= r){
        checkAndOutput(len);    
    }  else if (c1 <= 4){
        digits[l] = digits[r] = '0';
        getNumber(l + 1, r - 1, c1, len);
        digits[l] = digits[r] = '1';
        getNumber(l + 1, r - 1, c1 + 1, len);
    }
    return 0;
}

int main(void){
    for (int i = 1; i <= 120; i ++){
        memset(digits, '0', sizeof(digits));
        digits[0] = digits[i - 1] = '1';
        getNumber(1, i - 2, 1, i);
        if (i % 2 == 1){
            memset(digits, '0', sizeof(digits));
            digits[0] = digits[i - 1] = digits[i / 2] = '1';
            getNumber(1, i - 2, 1, i);
            
            memset(digits, '0', sizeof(digits));
            digits[0] = digits[i - 1] = '1';
            digits[i / 2] = '2';
            getNumber(1, i - 2, 1, i);

            memset(digits, '0', sizeof(digits));
            digits[0] = digits[i - 1] = '1';
            digits[i / 2] = '3';
            getNumber(1, i - 2, 1, i);
        }
        if (i > 1){
            if (i % 2 == 0){
                memset(digits, '0', sizeof(digits));
                digits[0] = digits[i - 1] = '2';
                checkAndOutput(i);
            }  else {
                memset(digits, '0', sizeof(digits));
                digits[0] = digits[i - 1] = '2';
                checkAndOutput(i);
                digits[i / 2] = '1';
                checkAndOutput(i);
            }
        }
    }
    return 0;
}
