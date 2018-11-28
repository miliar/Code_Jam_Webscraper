#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int a;
    for(a=1;a<=t;a++)
    {
        string str;
        int k;
        cin>>str>>k;
        int i,j,cnt=0;
        for(i=0;i<=str.size()-k;i++)
        {
            if(str[i]=='-')
            {
                for(j=i;j<i+k;j++)
                {
                    switch(str[j])
                    {
                        case '+':str[j]='-';break;
                        case '-':str[j]='+';break;
                    }
                }
                cnt++;
            }
        }
        int chk=0;
        for(i=0;i<str.size();i++)
        {
            if(str[i]=='-')
                chk=1;
        }
        cout<<"Case #"<<a<<": ";
        if(chk)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<cnt<<endl;
    }
    return 0;
}
