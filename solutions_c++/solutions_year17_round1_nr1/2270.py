//
//  main.cpp
//  Problem 1
//
//  4/14/17.
//
//

#include <iostream>
#include <fstream>
#include<string.h>
#include<algorithm>
#include <cstdio>
#include <stdio.h>
#define maxlen 30
using namespace std;

int main() {
    int T=0;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    for (int i = 0; i<T; i++)
    {
        int R = 0, C = 0, count = 0;
        char str[maxlen][maxlen];
        int listr[maxlen];
        int listc[maxlen];
        cin>>R>>C;
        
        for (int ri = 0; ri<R; ri++)
        {
            cin>>str[ri];
            for (int ci = 0; ci<C; ci++)
                if (str[ri][ci]!='?')
                {
                    listr[count] = ri;
                    listc[count] = ci;
                    count++;
                }
        }
        
        //cout<<count<<endl;
        for (int j = 0; j<count; j++)
        {
            char letter;
            letter = str[listr[j]][listc[j]];
            //cout<<letter<<endl;
            
            
            
            int right = C-1;
            for (int k = listc[j]+1; k<C; k++)
            {
                if (str[listr[j]][k] !='?')
                {
                    right = k-1; break;
                }
            }
            //cout<<right<<endl;
            for (int ri = 0; ri<=listr[j]; ri++)
                for (int ci = 0; ci<=right; ci++)
                {
                    
                    if (str[ri][ci]=='?')
                    {
                      //  cout<<ri<<' '<<ci<<endl;
                        str[ri][ci] = letter;
                    }
                }
        }
        //leftover
        int lastrow = listr[count-1];
        for (int ci = 0; ci<C; ci++)
        {
            for (int ri = R-1; ri>lastrow; ri--)
                str[ri][ci]=str[lastrow][ci];
        }
        
        //output
        cout<<"Case #"<<i+1<<": "<<endl;

        for (int ri = 0; ri<R; ri++)
             cout<<str[ri]<<endl;
        
    }
    return 0;
}
