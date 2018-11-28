#include <bits/stdc++.h>
using namespace std;

int main()
{
     freopen("A-large.in","r+",stdin);
    freopen("out.txt","w+",stdout);
    string str;
    int t,k,i,cas=1;
    cin>>t;

    while(t--)
    {
        cin>>str>>k;
        int len = str.length();
        int cnt2=0,cnt,loc=1;
        for(i=0; i<len; i++)
        {
            if(str[i]=='-')
            {
                if(i+k<=len){
                cnt = 0;
                for(int j=i; cnt<k; j++)
                {
                    if(str[j]=='-')
                        str[j] = '+';
                      else if(str[j]=='+')
                            str[j] = '-';
                    cnt++;
                    if(j>=len)
                        break;
                }
                if(cnt==k)
                    cnt2++;
            }
            }
            //cout<<str<<endl;
        }
        for(i=0; i<len; i++)
        {
            if(str[i]=='-')
                {
                    loc = 0;
                }
        }
        if(!loc)
            cout<<"Case #"<<cas++<<": "<<"impossible"<<endl;
            else
                cout<<"Case #"<<cas++<<": "<<cnt2<<endl;
    }
}
