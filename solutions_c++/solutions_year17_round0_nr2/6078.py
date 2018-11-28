#include <iostream>
#include <string.h>
using namespace std;

#define ll long long

int main()
{
    ll t;
    cin>>t;
    ll z;
    for(z=1;z<=t;z++)
    {
        char n[20];
        cin>>n;
        if(strlen(n)==1)
        {
            cout<<"Case #"<<z<<": "<<n<<endl;
        }
        else
        {
            ll i;
            for(i=1;i<strlen(n);i++)
            {
                if(n[i]<n[i-1])
                {
                    n[i-1]--;
                    n[i] = '9';
                    ll j = i-1;
                    while(j!=0 && n[j]<n[j-1])
                    {
                        n[j-1]--;
                        n[j] = '9';
                        j--;
                    }
                    break;
                }
            }
            while(i<strlen(n))
            {
                n[i] = '9';
                i++;
            }
            
            ll flag = 0;
            
            cout<<"Case #"<<z<<": ";
            
            for(i=0;i<strlen(n);i++)
            {
                if(n[i]=='0' && flag == 0)
                {
                    continue;
                }
                else if(n[i]!='0' && flag==0)
                {
                    flag = 1;
                    cout<<n[i];
                }
                else if(flag==1)
                {
                    flag = 1;
                    cout<<n[i];
                }
                
            }
            cout<<endl;
        }
    }
    return 0;
}