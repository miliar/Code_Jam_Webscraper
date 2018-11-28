#include <bits/stdc++.h>
using namespace std;

int main() 
{

    int T;
    scanf("%d", &T);
    int N=1;
    while(N<=T)
    {
        int K, count=0, count1=0;
        char str[1000];
        scanf("%s%d", str, &K);
        
        for(int i=0; i<strlen(str)-K+1; i++)
        {
            if(str[i]== '-')
            {
                for(int j=i; j<i+K; j++)
                {
                    if(str[j]== '-')
                    {
                        str[j] = '+';
                    }
                    else
                    {
                        if(str[j]== '+')
                        {
                            str[j] = '-';
                        }
                    }
                }
                count++;
         //     printf("%s\n", str);
            } 
        }
        for(int i=(strlen(str)-K+1); i<strlen(str); i++)
        {
            if(str[i]== '-' )
            {
                count1++;
          //    printf("%d", count1);
                break;
            }
        }
        
            if(count1>0)
            {
                cout << "Case #" << N << ": " << "IMPOSSIBLE" << endl;
            }
            else if(count1==0)
            {
                cout << "Case #" << N << ": " << count << endl;
            }
        N++;
    }
return 0;
}