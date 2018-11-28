#include <iostream>
#include <algorithm>
using namespace std;

int checkoddeven(int n)
{
    if(n%2==0)
        return 1;
    else
        return 0;
}
int main() {
    int t;
    
    cin>>t;
    int x=1;
    while(x<=t)
    {   
        int n,k;
        
        cin>>n>>k;
        
        int a[10000],p=1,i=0;
        a[0]=n;
        while(x)
        {       n=a[i];
            if(checkoddeven(n))
            {
                  
                a[i]=(n-1)/2;
                a[++i]=a[i-1]+1;
                   if(p==k)
                {
                     cout<<"case #"<<x<<": "<<max(a[i-1],a[i])<<" "<<min(a[i-1],a[i])<<endl;
                          goto last;
                }
           
                
            }
            else
                {
                    a[i]=n/2;
                    a[++i]=n/2;
                    if(p==k)
                    {
                    cout<<"case #"<<x<<": "<<max(a[i-1],a[i])<<" "<<min(a[i-1],a[i])<<endl;
                          goto last;
                    }
                    
                    
                }
                
                sort(a,a+i+1);
                p++;
        }
     
        last:
        x++;
         
    }
	return 0;
}
