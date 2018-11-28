#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long int lld;
void display(lld *a,lld n)
{
    cout<<endl;
    for(lld i=0;i<n;cout<<a[i++]<<" ");
}
int main()
{
    freopen("in2.in","r",stdin);
    freopen("output2.txt","w",stdout);
    lld t,tno=1;
    cin>>t;
    while(t--)
    {
        char a[100];
        cin>>a;
        lld i;
        for(i=0;i<strlen(a)-1 && a[i+1]>=a[i];i++);
        if(i!=(strlen(a)-1))
        {
            while(a[i]>a[i+1])
            {
                a[i+1]='9';
                a[i]--;
                i--;
            }
            for(i+=2;i<strlen(a);a[i++]='9');
        }
        cout<<"Case #"<<tno<<": ";
        if(a[0]=='0')
            cout<<(a+1)<<endl;
        else
            cout<<a<<endl;
        tno++;
    }
    return 0;
}
