#include <iostream>
#include<string.h>
#include<fstream>
#include<stdlib.h>

using namespace std;

int main()
{
    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("submit.out","w",stdout);
    int t,k,j,l,sz,i;
    cin>>t;
    string a;
    int flg,in,cnt;
    for(l=0;l<t;l++)
    {
        cin>>a>>k;
        sz=k; cnt=0;int f=0;
        for(i=0;i<a.size();i++)
        {
            if(a[i]=='-' && i+k-1<a.size())
            {
                j=i;flg=0;sz=k;
                while(sz!=0)
                {
                    sz--;j++;
                }

                for(sz=i;sz<j;sz++)
                {
                    if(a[sz]=='+') a[sz]='-';
                    else a[sz]='+';

                }cnt++;
            }
        }flg=0;
        for(i=0;i<a.size();i++)
        {if(a[i]=='-') flg=1; }
        if(flg==1) cout<<"Case #"<<l+1<<": "<<"IMPOSSIBLE\n";
        else cout<<"Case #"<<l+1<<": "<<cnt<<"\n";

    }
    return 0;
}
