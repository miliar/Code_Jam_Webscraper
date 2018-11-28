#include <bits/stdc++.h>

using namespace std;


int main()
{
    int t;
    cin >> t;
    
    for(int caso=1;caso<=t;caso++)
    {
        string a ;
        cin >> a;
        int q=0;
        int last=9;
        for(int i=a.size()-1;i>=0;i--)
        {
            if(a[i]-'0'>last)
            {
              a[i]=a[i]-1;
              for(int k=i+1;k<a.size();k++)
              {
                  a[k]='9';
              }
              
            }
            
            last=min(a[i]-'0',last);
            
        }
        
        if(a[0]=='0')
            a=a.substr(1,a.size()-1);
            
        printf("Case #%d: %s\n",caso,a.c_str());
    }
    
    
    return 0;
}