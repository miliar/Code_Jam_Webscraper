#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;



int main() {
    int n,a[10000];
    cin>>n;
 
    for(int i=0;i<n;i++)
        {
        int s1=0;
        string s;
        int k;
        cin>>s;
        
        cin>>k;
      
        int l=s.length();
        int j=0;
        int re=0;
        
        while(j<=l-k)
            {
        
            if(s[j]=='+')
                {
                	j++;
                continue;}
            else
                {
                re++;
                int m=0;
                s1=0;
                int temp=0;
                while(m<k&&m+j<l)
                    {
                    
                    if(s[j+m]=='-')
                        s[j+m]='+';
                    else if(s[j+m]=='+')
                        {
                        
                        s[j+m]='-';
                        if(s1==0)
                            {
                            temp=j+m-1;
                            s1=1;
                        }
                    }
                    
                    m++;
                }
                if(s1==1)
                j=temp;
              
            }
            j++;
              
        }
        for(int j=l-k;j<l;j++)
        {
           if(s[j]=='-')
           {
           	s1=1;
           	break;
           }
        }
        if(s1==0)
        a[i]=re;
        else
            a[i]=-1;
        
    }
    for(int i=0;i<n;i++)
    {
    	if(a[i]==-1)
    	cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
    	else
    	cout<<"Case #"<<i+1<<": "<<a[i]<<endl;
    }
}
