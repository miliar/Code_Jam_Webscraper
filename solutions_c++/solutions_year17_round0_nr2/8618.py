//
//  CJ2.cpp
//  
//
//  Created by udita johri on 08/04/17.
//
//

#include <stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    int T,x=1,i,j;
    cin>>T;
    vector<string> v;
    while(x<=T)
    {
        string N;
        cin>>N;
        int len =N.length(),f=0;
        i=1;
        while(i<len)
        {
            if(N[i-1]>N[i])
            {
                f=1;
                break;
            }
            i++;
        }
        //cout<<i<<endl;
        if(f==0)
            v.push_back(N);
        else
        {
            j=len-1;
            while(j>=i)
            {
                N[j]='9';
                //cout<<j<<" = "<<N[j]<<endl;
                j--;
            }
            
            while(j>=0)
            {
                if(N[j]!='1' && N[j]!='0')
                {
                    N[j]=N[j]-1;
                   // cout<<j<<" = "<<N[j]<<endl;
                    j--;
                    while(j>=0)
                    {
                        if(N[j]>N[j+1])
                        {
                            N[j]=N[j]-1;
                            N[j+1]='9';
                        }
                        //cout<<j<<" = "<<N[j]<<endl;
                        j--;
                    }
                    break;
                }
                else
                {
                    //cout<<"1/0"<<endl;
                    if(j!=0)
                        N[j]='9';
                    else
                        N[j]='0';
                    //cout<<j<<" = "<<N[j]<<endl;
                    j--;
                }
            }
            string str="";
            j=0;
            while(j<len)
            {
                if(j==0 && N[0]=='0')
                {
                    j++;
                    continue;
                }
                else
                    str+=N[j];
                j++;
            }
            v.push_back(str);
        }
        x++;
        //cout<<x<<endl;
    }
    //cout<<"Out";
    for(x=1;x<=T;x++)
        cout<<"Case #"<<x<<": "<<v[x-1]<<endl;
    return 0;
}
