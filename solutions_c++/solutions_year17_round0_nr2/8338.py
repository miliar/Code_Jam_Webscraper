#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("tidy.out","w",stdout);
   // freopen("tidyin.in","r",stdin);
    int tc,t,i,j,k,l,m,n;
    string str;
    cin>>tc;
    t=0;
    while(tc--)
    {
        t++;
        cin>>str;
        l=str.length();
        m=l;

        while(m--){
                k=0;
        for(i=0;i<l-1;i++)
        {
            if(k==1)
            {
                str[i]='9';
                str[i+1]='9';
            }

            if((str[i]-48)>(str[i+1]-48))
            {
                str[i]=(str[i]-48-1)+48;
                str[i+1]='9';
                k=1;
            }
        }
        if(k==0)
            break;
        }
        for(i=0;i<l;i++)
        {
            if(str[i]!='0')
                break;
        }
        printf("Case #%d: ",t);
        for(j=i;j<l;j++)
            cout<<str[j];
        cout<<endl;
    }
    return 0;
}
