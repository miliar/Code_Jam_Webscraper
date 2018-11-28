#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <map>
using namespace std;

int main()
{
    int n;
    scanf("%d",&n);
    if(n%2){
        for(int i=2;i<n;i+=2)
            printf("%d ",i);
        for(int i=i=n-1;i>0;i-=2)
            printf("%d ",i);
        for(int i=1;i<=n;i+=2)
            printf("%d ",i);
        for(int i=n-2;i>0;i-=2)
            printf("%d ",i);
        printf("%d\n",n);
    }
    else{
        for(int i=1;i<n;i+=2)
            printf("%d ",i);
        for(int i=i=n-1;i>0;i-=2)
            printf("%d ",i);
        for(int i=2;i<=n;i+=2)
            printf("%d ",i);
        for(int i=n-2;i>0;i-=2)
            printf("%d ",i);
        printf("%d\n",n);
    }
    return 0;
}
