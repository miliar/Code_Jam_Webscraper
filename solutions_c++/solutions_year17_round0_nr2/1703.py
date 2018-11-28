//
//  main.cpp
//  Google
//
//  Created by Mec0825 on 13-4-13.
//  Copyright (c) 2013年 Mec0825. All rights reserved.
//

#include <iostream>

int main()
{
    freopen("/Users/mec/Documents/Competition/Google/2017/Qualification/B-large.in", "r", stdin);
    freopen("/Users/mec/Documents/Competition/Google/2017/Qualification/B-out.txt", "w", stdout);
    
    int numc;
    
    scanf("%d", &numc);
    
    for(int t = 0; t < numc; t++) {
        
        char S[20];
        
        scanf("%s", S);
        
        int len = (int)strlen(S);
        
        for(int i = len-2; i >= 0; i--) {
            if(S[i]-'0' > S[i+1]-'0') {
                S[i] = '0' + (S[i]-'0'-1);
                for(int j = i+1; j < len; j++) {
                    S[j] = '9';
                }
            }
        }
        
        if(S[0] == '0')
            printf("Case #%d: %s\n",t+1, S+1);
        else
            printf("Case #%d: %s\n",t+1, S);
        
    }
    
    return 0;
}
