#include<bits/stdc++.h>
using namespace std;
int main()
    {
         freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int tt;
    cin>>tt;

    for(int t=1;t<=tt;t++)
    {
       // printf("Case #%d: ",t);
        string s;
        int k;
        int cnt=0,desc=0;
        cin>>s>>k;
        int l=s.length();
        for(int i=0;i<l;i++)
        {
          if(s[i]=='-'){
cnt++;
if(i+k<=l){
        for(int j=i;j<i+k;j++)
        {

            if(s[j]=='-')
                s[j]='+';
            else
                s[j]='-';

        }
          }
        }
        }
        for(int i=0;i<l;i++)
        {
            if(s[i]=='+')
                desc++;

        }
     printf("Case #%d: ",t);
        if(desc==l)
            cout<<cnt<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;

    }
    //cout<<endl;
    return 0;
}
