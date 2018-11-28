#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
  
 
    long int t;
    
    cin>>t;
    for(int i=0;i<t;i++)
        {
        int a[10];
        int n;
        char b[]={'R','Y','B'};
        cin>>n;
        char c[n];
        for(int j=0;j<6;j++)
            cin>>a[j];
       
        if(a[0]>a[2]+a[4]||a[2]>a[0]+a[4]||a[4]>a[0]+a[2])
           { cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
            continue;}
        int j=0;
         a[1]=a[2];a[2]=a[4];
        if(a[0]<a[1])
        { 
            swap(a[0],a[1]);
            swap(b[0],b[1]);
        }
        if(a[0]<a[2])
            {
            swap(a[0],a[2]);
            swap(b[0],b[2]);
        }
         if(a[1]<a[2])
            {
            swap(a[1],a[2]);
            swap(b[1],b[2]);
        }
      
        while(j<n)
            {
                if(a[1]==a[2]&&a[0]<a[1]+a[2])
                {
                 if(a[0]!=0)
            {c[j]=b[0];a[0]--;j++;}
             
            if(a[1]!=0)
                {
                c[j]=b[1];a[1]--;j++;
            }
            if(a[2]!=0)
                 {
                 c[j]=b[2];a[2]--;j++;
             }
                }
           else{
            if(a[0]!=0)
            {c[j]=b[0];a[0]--;j++;}
             if(a[2]!=0&&(a[0]==0||a[1]==0))
                 {
                 c[j]=b[2];a[2]--;j++;
             }
            if(a[1]!=0)
                {
                c[j]=b[1];a[1]--;j++;
            }
           }
        }
            
        
        
        
       
        cout<<"Case #"<<i+1<<": ";
    for(j=0;j<n;j++)
        cout<<c[j];
    cout<<endl;
    }

}

