#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inputl.txt","r",stdin);
    freopen("outputl.txt","w",stdout);
    int t,k,l,c,i,j,m,flag=0,n;
    char str[1001];
    cin>>t;
    for(n=1;n<=t;n++)
    {
        c=0;
        flag=0;
        cin>>str;
        cin>>k;
        l=strlen(str);
        for(i=0;i<=(l-k);i++)
        {
            if(str[i]=='-')
            {
                c++;
                for(j=i;j<(i+k);j++)
                {
                    if(str[j]=='-')
                        str[j]='+';
                    else if(str[j]=='+')
                        str[j]='-';
                }
            }
        }
        for(m=i;m<l;m++)
        {
            if(str[m]=='-')
            {
                flag=1;
                break;
            }
        }
        if(flag==1)
            cout<<"Case #"<<n<<":"<<" "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<n<<":"<<" "<<c<<endl;
    }
    return 0;
}


