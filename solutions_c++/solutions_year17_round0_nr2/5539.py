#include <vector>
#include <algorithm>
#include <iostream>
#include<fstream>
#include<iostream>
#include<math.h>
#include<string>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

long long  int check(vector<int>arr)
    {
   // cout<<"in ckeck\n";
    long long int i;
    for(i=0;i<arr.size()-1;i++)
        {
        if(arr[i]>arr[i+1])
            return i;
    }
    return -1;
}
void fun()
    {
    string s;
    int flag=0;
    cin>>s;
    //cout<<s<<"-- ";
   vector<int>arr;
    arr.assign(s.size(),-1);
    
    long long int i,k,pos,i_9,e;
    for(i=0;i<s.size();i++)
        arr[i]=s[i]-'0';
     
    e=arr.size();
  
    while((pos=check(arr))!=-1)
          {
        s.clear();
         for(i=0;i<arr.size();i++)
        s+=string(to_string(arr[i]));
             int x=atoi(s.c_str());
        x--;
        s=to_string(x);
        arr.clear();
         arr.assign(s.size(),-1);
              for(i=0;i<s.size();i++)
        arr[i]=s[i]-'0'; 
          }
    string s2;
    //for(i=0;i<s.size();i++)
   //     s2+=arr[i]+'0';
    //cout<<stoi(s2)<<endl;
    long long int st=0;
   while(arr[0+st]==0)
       st++;
    	if(flag==0)
    for(i=st;i<s.size();i++)
       {
       
       cout<<arr[i];    
   }
    //cout<<endl;
}
int main()
    {
    long long int k,t;
    cin>>t;
     k=1;
    while(t--)
        {
       
      cout << "Case #" << (k++) << ": ";
          fun();
        cout<< endl;  
    }
    return 0;
}
