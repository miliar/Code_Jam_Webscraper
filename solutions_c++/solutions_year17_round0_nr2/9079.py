
#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;
int flag=0;
// Returns true if digits of n are sorted in decreasing
// order
bool areSorted(unsigned long long  n)
{
    // Note that digits are traversed from last to first
    int next_digit = n%10;
    n = n/10;
    while (n)
    {
        int digit = n%10;
        if (digit > next_digit)
            return false;
        next_digit = digit;
        n = n/10;
        flag++;
    }

    return true;
}

int main()
{
    int t;
    unsigned long long n;
    FILE * read=fopen("input.txt","r");
    FILE * write=fopen("output.txt","w");
    fscanf(read,"%d",&t);
    for(int j=1;j<=t;j++){
    fscanf(read,"%llu",&n);
    printf("%llu\n",n);

    for(unsigned long long i=n;i>0;i--){
            flag=0;
           if(areSorted(i)){

            fprintf(write,"Case #%d: %llu\n",j,i);
            break;
           }
           else{

                i-=i%(unsigned long long int)pow(10,flag);

            continue;
           }


    }
    }
    return 0;
}
