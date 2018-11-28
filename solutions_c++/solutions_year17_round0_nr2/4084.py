#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int t;
    char a[20];
    cin>>t;
    for(int k=0;k<t;k++)
    {
        int i=0,n,j;
        cin>>a;
        n=strlen(a);
        while(i<n-1)
        {
            if(a[i]>a[i+1])
            {
                a[i]--;
                for(j=i+1;j<n;j++)
                a[j]='9';
                i=0;
            }
            else
            i++;
        }
        cout<<"Case #"<<k+1<<": ";
        for(i=0;i<n;i++)
        {if(a[i]!='0')break;}
        for(;i<n;i++)
            cout<<a[i];cout<<endl;
    }
    return 0;
}
