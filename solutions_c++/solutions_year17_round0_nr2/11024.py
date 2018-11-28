#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
int main()
{
    char num[20];
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%s", num);
        for (int j = strlen(num) - 1; j >= 0; j--)
        {
           
            if (j >= 1 && (num[j] < num[j - 1] or num[j] + num[j - 1] == '0'+'0'))
            {
                num[j] = '9';
                num[j - 1]--;
                if (num[j - 1] < '0')
                {
                    num[j - 1] = '0';
                }
                if(j < strlen(num) - 1){
                    num[j+1] = '9';
                }
            }
        }
        printf("Case #%d: ",i+1);
        for(int i=0; i<strlen(num); i++){
            if(i==0 && num[i] == '0') continue;
            printf("%c",num[i]);
        }
        printf("\n");
    }
    return 0;
}