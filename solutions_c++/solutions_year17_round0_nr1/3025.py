#include<bits/stdc++.h>
using namespace std;
int tt,i,k,lens,cnt,tmp;
string str;
int main()
{
    freopen("input.txt","r",stdin);
    
    freopen("output.txt","w",stdout);
    cin>>tt;
    for(int t=1;t<=tt;t++)
    {
        cin>>str;
        cin>>k;
        lens=str.size();
        i=0;
        cnt=0;
        while(i<lens)
        {
            while(i<lens && str[i]=='+')i++;
            if(i<lens && lens-i>=k)
            {
                tmp=k;
                int x=i;
                while(tmp--)
                {
                    if(str[i]=='+')
                        str[i]='-';
                    else
                        str[i]='+';
                    
                    i++;
                }
                i=x;
                cnt++;
            }
            else
                break;
        }
        if(i==lens)
            cout<<"Case #"<<t<<": "<<cnt<<endl;
        else
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
    }
    return 0;
}
