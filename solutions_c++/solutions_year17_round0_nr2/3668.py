#include<iostream>
#include<cstring>
#define N 20
using namespace std;

int main()
{
    int t,i,j,k;
    char s[N];
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s;
        int len = strlen(s);
        if(len==1) cout<<"Case #"<<i<<": "<<s<<endl;
        else
        {
            for(k=1;k<len;k++)
            {
          //      cout<<"kello"<<endl;
                if(s[k-1]>s[k]) break;
            }
            if(k<len)
            {
                for(j=k-1;j>0&&s[j]==s[j-1];j--);
                if(j==0 && s[j]=='1' ) {
                    cout<<"Case #"<<i<<": ";
                    for(k=0;k<len-1;k++) cout<<'9';
                    cout<<endl;
                }
                else if(j==0)
                {
                    s[j]=s[j]-1;
                    for(j=j+1;j<len;j++) s[j]='9';
                    cout<<"Case #"<<i<<": "<<s<<endl;
                }
                else
                {
                    s[j]=s[j]-1;
                    for(j=j+1;j<len;j++) s[j]='9';
                    cout<<"Case #"<<i<<": "<<s<<endl;
                }
            }
            else
            {
                cout<<"Case #"<<i<<": "<<s<<endl;
            }
        }
    }
    return 0;
}
