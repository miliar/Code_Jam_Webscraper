#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int _=1; _<=t; _++)
    {
        string n;
        cin>>n;
        int len = n.length();
        int a[len];
        for(int i=0; i< len; i++)
            a[i] = n[i] - '0';
        
        while(1)
        {
            int i;
            for(i=len-1; i>0; i--)
            {
                if(a[i] < a[i-1])
                    break;
            }
            if(i == 0)
                break;
            
            for(int j=i; j<len; j++)
                a[j] = 9;
            for(int j=i-1; j>=0; j--)
            {
                if(a[j] == 0)
                    a[j] = 9;
                else
                {
                    a[j]--;
                    break;
                }
            }
        }
        
        cout<<"Case #"<<_<<": ";
        int i=0;
        while(a[i] == 0)
            i++;
        for(;i<len;i++)
            cout<<a[i];
        cout<<endl;
    }
    return 0;
}
