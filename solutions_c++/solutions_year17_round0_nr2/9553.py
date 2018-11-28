#include<iostream>
#include<string.h>
using namespace std;
int main ()
{
    int t,i,j,p=1;
    cin>>t;
    while (t--)
    {
        int k=1,f=0;
        char ch[21];
        cin>>ch;
        int l=strlen(ch);
        for (i=(l-1);i>0;i--)
            {
              if (ch[i]<ch[i-1])
                {
                    for (j=i;j<(i+k);j++){
                ch[j]='9';
                    }
                ch[i-1]=ch[i-1]-1;
              }
              else
                k++;
            }
            for (i=0;i<l;i++)
            {
                if (ch[i]=='0')
                    f=(i+1);
                else
                    break;
            }
        cout<<"Case #"<<p<<": ";
        for (j=f;j<l;j++)
            cout<<ch[j];
            cout<<endl;
        p++;
    }
    return 0;
}
