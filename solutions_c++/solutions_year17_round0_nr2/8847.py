#include<iostream>
#include<string>

using namespace std;

int main()
{
    long long int n;
    int t,p,flag;
    int success=0;
    
    cin>>t;
    p=1;
    while(t--)
    {
        cin>>n;
        
        long long int k=n;
        
        if(k<10)
        {
            cout<<"Case #"<<p<<": "<<k<<endl;
        }
        else
        {
        for(long int i=n;i>10;i--)
        {
         
            flag=1;
            long long int h=i;
                 int g=h%10;
              h/=10;
            while(h>0)
            {
                int y=h%10;
                h/=10;
                if(y>g)
                {
                    flag=0;
                    break;
                }
              g=y;  
            }
            
            if(flag==1)
            {
                cout<<"Case #"<<p<<": "<<i<<endl;
                break;
            }
            
        }
        }
        
        p++;
        
    }
    
    
    return 0;
}