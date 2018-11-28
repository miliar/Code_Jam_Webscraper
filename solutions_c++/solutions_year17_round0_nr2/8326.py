#include<iostream>
#include<cstring>
using namespace std;

int main()
{
    unsigned long long t,i,j,tt,cnt,n,l;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
        char s[20],tmp[20];
        cin>>s;
        l=strlen(s);
        for(i=1;s[i]!='\0';i++)
        {
            if(s[i-1]>s[i])
            {
                s[i-1]--;
                for(j=i;s[j]!='\0';j++)
                    s[j]='9';
                i=0;
            }
        }
        if(s[0]=='0')
        {
            strncpy(s,s+1,l-1);
            s[l-1]='\0';
        }
        cout<<"Case #"<<tt<<": "<<s<<endl;
    }
    return 0;
}
