#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int tCase,nCase;
    cin>>tCase;
    for(nCase=1;nCase<=tCase;nCase++)
    {
        char str[10000];
        memset(str,0,sizeof(str));
        int k;
        cin>>str>>k;
        //cout<<str<<" "<<k<<endl;
        int len = strlen(str);
        int counter=0;
        for(int i=0;i<=len-k;i++)
        {
            if(str[i]=='-')
            {
                counter++;
                for(int j=i;j<=i+k-1;j++)
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else
                        str[j]='+';
                }
                //cout<<str<<endl;
            }
        }
        for( int i=len-1;i>=0;i--)
        {
            if(str[i]=='-')
                counter=-1;
        }
        if(counter!=-1)
        {
            cout<<"Case #"<<nCase<<": "<<counter<<endl;

        }
        else
        {
            cout<<"Case #"<<nCase<<": IMPOSSIBLE"<<endl;
        }
    }
    return 0;
}
