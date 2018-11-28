#include <vector>
#include <algorithm>
#include <iostream>
#include<fstream>
#include<iostream>
#include<math.h>
#include<string>
#include<list>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

void fun()
    {
     string s;
    cin>>s;
    
    long long int i,k,n,x,count=0,flag=0;
    cin>>n;
 vector<char>arr;
    arr.assign(s.begin(),s.end());
    //for(i=0;i<arr.size();i++)
       // {
      //  cout<<arr[i];
    //}
   // cout<<endl;
    for(i=0;i<arr.size();i++)
        {
        if(arr[i]=='-')
            {
           // cout<<"pos at "<<i<<endl;
            if((i+n)>arr.size())
                {
                cout<<"IMPOSSIBLE\n";
                flag=1;
                break;
            }
            count++;
            for(k=i;k<i+n;k++)
                {
                
                if(arr[k]=='+')
                    arr[k]='-';
                else
                    arr[k]='+';
            }
                
        }
       
    }
    if(flag==0)
     cout<<count<<endl;
    
}
int main()
    {
   long long int t,k=0;
    cin>>t;
    while(t--)
        {
        k++;
        	cout << "Case #" << (k) << ": " ;
        fun();
      
    }
    return 0;
}
