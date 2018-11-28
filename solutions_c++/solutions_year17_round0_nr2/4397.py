#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.out","w",stdout);
    int T,i,j,l,v,temp,m,c=0,pos;
    string str;
    cin>>T;
    v=T;
    while(T--)
    {
        c=0;
        cin>>str;
        l=str.length();
        for(i=0;i<20;i++)
        {
            pos=99;
            for(j=0;j<l-1;j++)
                if(str[j]>str[j+1])
                {
                    pos=j;
                    break;
                }
            if(pos!=99)
            {
                int num=(int)str[pos];
                str[pos]=(char)(num-1);
                for(j=pos+1;j<l;j++)
                    str[j]='9';
            }
        }
        cout<<"Case #"<<v-T<<": ";
        for(i=0;i<l;i++)
            if(str[i]!='0')
                break;
        for(;i<l;i++)
            cout<<str[i];
        cout<<endl;
    }
}
