#include <iostream>
#include <stdio.h>
#include <stdbool.h>

using namespace std;

bool tidy(unsigned long long n){
    if (n<10){
        return true;
    }
    else{
        int lstdig;
        while(true){
            lstdig=n%10;
            n/=10;
            if (n%10>lstdig){
                return false;
            }
            if (n==0){
                return true;
            }
        }

    }
}

unsigned long long tidify(unsigned long long n){
    if (tidy(n)){
        return n;
    }
    else{
        if (n%10==9){
            return tidify(n/10)*10+9;
        }
        else{
            while (n%10!=9){
                n--;
            }
            return tidify(n/10)*10+9;
        }
    }
}

int main()
{
    unsigned long long tstcase,input;
    scanf("%llu",&tstcase);
    for (int i=0;i<tstcase;i++){
        scanf("%llu",&input);
        printf("Case #%d: %llu\n",i+1,tidify(input));
    }
        return 0;
}
