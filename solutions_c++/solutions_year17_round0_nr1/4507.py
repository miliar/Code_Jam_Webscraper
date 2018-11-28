#include<bits/stdc++.h>



using namespace std;

int cnt =0;
string str;

int modify(int x,int k)
{
    if(x+k>str.length())
        return 0;
    for(int i=x;i<k+x;i++)
    {
       if(str[i]=='+')
       str[i]='-';
       else
       str[i]='+';
    }
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int d =0;

    int k,t;
    cin>>t;
    while(t--)
    {
        ++cnt;
        cin>>str>>k;
        int ans =0;

        for(int i=0;i<str.length();i++)
        {
            if(str[i]=='-')
            {
                modify(i,k);
                ++ans;
            }
        }
        int flag=1;
        for(int i=0;i<str.length();i++)
        {
            if(str[i]=='-')
                flag=0;
        }
        if(flag==1)
            cout<<"Case #"<<cnt<<": "<<ans<<"\n";
        else
            cout<<"Case #"<<cnt<<": "<<"IMPOSSIBLE"<<"\n";



    }
}

