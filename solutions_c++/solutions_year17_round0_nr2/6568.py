#include <iostream>
using namespace std;
 
int main() {
    int T;
    cin>>T;
    int t=0;
    while(T--)
    {
        t++;
        char s[19]={0};
        cin>>s;
        int i=0;
        for(i=0;s[i]!=0;i++)
        {
        }
        int j=i;
        int flag=0;
        int p=0;
        for(j=i-1;j>=1;j--)
        {
            if(s[j]<s[j-1])
            {
                flag=1;
                p=j-1;
            }
        }
        while(p>=1 && s[p-1]==s[p])
        {
            p--;
        }
        if(flag==0)
        {
            cout<<"Case #"<<t<<": "<<s<<endl;
        }
        else
        {
            if(p==0 && s[p]=='1')
            {
                int k=p;
                for(k=p;k<i-1;k++)
                {
                    s[k]='9';
                }
                s[k]=0;
                cout<<"Case #"<<t<<": "<<s<<endl;
            }
            else if(s[p]!='0' && s[p]!='1')
            {
                s[p]--;
                for(int k=p+1;s[k]!=0;k++)
                {
                    s[k]='9';
                }
                cout<<"Case #"<<t<<": "<<s<<endl;
            }
            else
            {
                cout<<"Don't know"<<endl;
            }
        }
    }
    return 0;
}
