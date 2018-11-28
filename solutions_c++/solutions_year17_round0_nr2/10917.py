//
//  main.cpp
//  pancakes
//
//  Created by Sherwin Joseph on 08/04/17.
//  Copyright © 2017 Sherwin Joseph. All rights reserved.
//

#include <iostream>
#include <string.h>

int main(int argc, const char * argv[])
{
    int T,a,b,c,d;
    int N, max[100];
    std::cin>>T;
    for (int i=1; i<=T; i++)
    {
        std::cin>>N;
        if (N/10==0)
        {
            max[i]=N;
        }
        for (int j=9; j<=N; j++)
        {
            if (N>=11 || N<=99)
            {
                a=j%10;
                b=j/10;
                if (b<=a)
                {
                    max[i]=j;
                }
            }
            if (N>=101 || N<=999) {
                a=j%10;
                b=j/10;
                c=b%10;
                d=b/10;
                if (d<=c && c<=a) {
                    max[i]=j;
                }
                
            }
        }
        

    }
    for (int i=1; i<=T; i++) {
                std::cout<<"Case #"<<i<<": "<<max[i]<<std::endl;
    }
    return 0;
}
