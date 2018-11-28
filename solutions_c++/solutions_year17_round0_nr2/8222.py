#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int main()
{
    int t,l,c=1,count;
    long long int n;
    string s;
    cin>>t;
    while(t--)
    {
        cin>>n;
        char s[30];
        
        for(long long int j=n;j>0;j--)
        {
        	itoa (j,s,10);
            l=strlen(s);
            //cout<<s<<" "<<l<<endl;
            count=0;
            for(int i=l-1;i>=0;i--)
            {
                if(i>0 && s[i]>=s[i-1])
                count++;
                else if(i==0)
                count++;
            }
            if(count==l)
            {
            cout<<"Case #"<<c<<": "<<j<<endl;
            break;
            }
        }
        c++;
    }
    return 0;
}

