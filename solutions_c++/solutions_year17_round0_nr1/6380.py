#include<iostream>
#include<cstdio>
#include<string.h>
using namespace std;
int main()
{
    //freopen("C:\\Users\\apachoud.ORADEV\\Desktop\\input.txt","r",stdin);
    //freopen("C:\\Users\\apachoud.ORADEV\\Desktop\\output.txt","w",stdout);
    int t, k;
    char s[2000];
    cin>>t;
    int te=1;
    while(te<=t)
    {
       cin>>s;
       cin>>k;

        int i=0;
        int counter=0;
        int len= strlen(s);
        int impossible =0;
        while(i<len)
        {
            if(s[i]=='+')
            {
                i++;
            }
            else
            {
                counter++;
                int x=k;
                int j=i;
                while(j<len && x>0)
                {
                    if(s[j]=='+')
                    {
                        s[j]='-';
                    }
                    else
                    {
                        s[j]='+';
                    }
                    x--;
                    j++;
                }
                if(x>0)
                {
                    impossible=1;
                }
            }
        }
        if(impossible==1)
        {
            cout<<"Case #"<<te<<": "<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<"Case #"<<te<<": "<<counter<<endl;
        }
        te++;
    }
}
