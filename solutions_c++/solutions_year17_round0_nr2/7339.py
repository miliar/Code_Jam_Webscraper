#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    char a[20];
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        cin>>a;
        int len=strlen(a);
        while(a[len-1]=='0' && a[len-2]=='0')
        {
            a[len-1]='9';
            --len;
        }
        for(int i=len-1;i>0;i--)
        {
            if(a[i]=='0')
            {
                for(int l=i;l<strlen(a);l++)
                    a[l]='9';
                a[i-1]--;
            }
            else if(a[i]<a[i-1])
            {
                a[i]='9';
                a[i-1]--;
                for(int l=i;l<strlen(a);l++)
                    a[l]='9';
            }
        }
        int p=0;
        cout<<"Case #"<<z<<": ";
        if(a[0]=='0')
             p=1;
        for(int j=p;j<strlen(a);j++)
            cout<<a[j];
        cout<<endl;
    }
}
