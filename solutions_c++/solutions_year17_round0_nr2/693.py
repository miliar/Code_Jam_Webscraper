#include<bits/stdc++.h>
using namespace std;
int main()
{

      freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cases,caseno=0;
    cin>>cases;
    while(cases--)
    {
        char ch[100];
        cin>>ch;

        int len = strlen(ch);
        if(len==1)
          cout<<"Case #"<<++caseno<<": "<<ch<<endl;
          else{

        for( int i=len-2;i>=0;i--)
        {
            int ch1=ch[i]-48;
            int ch2 = ch[i+1]-48;
            if(ch1>ch2)
            {
                ch[i] =ch[i]-1;
                for(int j=i+1;j<=len-1;j++)
                {
                    ch[j]='9';
                }

            }
        }
        cout<<"Case #"<<++caseno<<": ";
        if(ch[0]>'0')
        cout<<ch[0];
        for(int i=1;i<len;i++)
        {
            cout<<ch[i];
        }
        puts("");

          }




    }
    return 0;
}

