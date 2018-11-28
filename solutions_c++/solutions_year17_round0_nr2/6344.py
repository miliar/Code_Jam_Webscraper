#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;
int main()
{
    //freopen("C:\\Users\\apachoud.ORADEV\\Desktop\\input.txt","r",stdin);
    //freopen("C:\\Users\\apachoud.ORADEV\\Desktop\\output.txt","w",stdout);
    int t, te=1;
    char s[20];
    cin>>t;
    while(te<=t)
    {

        cin>>s;
        int len=strlen(s);
        for(int i=0;i<len-1;i++)
        {
           if(s[i]>s[i+1])
           {
               int j=i;
               while(j>0 && s[j]==s[j-1])
               {
                j--;
               }
               s[j]=(s[j]-'1')+'0';
               int k=j+1;
               while(k<len)
               {
                   s[k]='9';
                   k++;
               }
               break;
           }
        }
        cout<<"Case #"<<te<<": ";
        if(s[0]!='0')
            cout<<s[0];
        for(int i=1;i<len;i++)
        {
            cout<<s[i];
        }
        cout<<endl;
        te++;
    }
}
