//
//  main.cpp
//  CodeJam
//
//  Created by Arup Sarker on 4/8/17.
//  Copyright © 2017 Arup Sarker. All rights reserved.
//

#include <stdio.h>
#include <string.h>

char str[20];
long int len,orginalLen;
void checkIn(int i)
{
    if(i<len-1 && str[i]<=str[i+1])
    {
        checkIn(i+1);
        if(str[i] > str[i+1])
        {
            str[i+1] = '9';
            str[i] = str[i] - 1;
        }
    }
    else
    {
        if ((str[i] > str[i+1]) && i+1 != orginalLen) {
            str[i] = str[i]-1;
            for(int j = i+1; j<len;j++)
            {
                str[j] = '9';
            }
        }
       
        return;
    }
}

int main() {
    // insert code here...
    int testCase, i,j,k;
    freopen("/Users/arupsarker/Desktop/Development/CodeJam/CodeJam/tidy.txt", "rt", stdin);
    freopen("/Users/arupsarker/Desktop/Development/CodeJam/CodeJam/tidy.out", "wt", stdout);
    scanf("%d",&testCase);
    getchar();
    for (i=1; i<=testCase; i++) {
        scanf("%s",str);
        len = strlen(str);
        orginalLen = len;
        int flag =0;
        k = 0;
        for (j=0; str[j]; j++) {
            if (str[j] != '0') {
                flag = 1;
                k = j;
                break;
            }
        }
        len = len-k;
        if(len != 1 && flag == 1)
            checkIn(k);
        printf("Case #%d: ",i);
        if (flag == 0) {
            printf("0");
            
        }
        else
        {
            for (j = k; str[j]; j++) {
                if(j == 0 && str[j] == '0' && len != 1)
                    continue;
                else
                    printf("%c",str[j]);
            }
        }
        printf("\n");
        str[0] = NULL;
    }
    return 0;
}
