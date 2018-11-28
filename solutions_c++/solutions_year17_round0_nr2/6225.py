#include <cstdio>
#include <math.h>
#include <string.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        long long int n;
        scanf("%lli",&n);
        
        vector<int> v;
        
        long long int m = n;
        int digits=0;
        while(m != 0)
        {
            v.push_back(m%10);
            m/=10;
            digits++;
        }

        reverse(v.begin(),v.end());

        for(int i=digits-2; i>=0 ;i--)
        {
            if(v[i] <= v[i+1] ) continue;
            else
            {
                v[i]--;
                
                for(int j = i+1; j< digits; j++)
                {
                    v[j] = 9;
                }
                
            }
        }        
        
        printf("Case #%d: ",t);
        for(int i=0; i<digits; i++)
        {
            if(i == 0 && v[i] == 0)
            {
                while(v[i] == 0)
                {
                    i++;
                    continue;
                }
            }
            printf("%d",v[i]);
        }
        printf("\n");
        // for(vector<int>::iterator it=v.begin(); it != v.end(); ++it)
        // {
        //     if(it == v.begin() && *it == 0)
        //     {
        //         while(*it == '0') //dont print leading zeros 
        //         {
        //             ++it;
        //             continue;
        //         } //all can't be zero
        //     }

        //     cout<<*it;
        // }
        // printf("\n");
        
        
    }
}