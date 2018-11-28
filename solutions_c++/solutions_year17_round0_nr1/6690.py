#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T,cnt=1;
    cin>>T;
    while(T--)
    {
        int flag=0,count=0;
        string str;
        cin>>str;
        int k,n;
        cin>>k;
        n=str.size();
        for(int i=0 ; i<n ; i++)
        {
            if(str[i]=='-')
            {
                count++;
                for(int j=i;j<(i+k);j++)
                {
                    if(j>(n-1))
                    {
                        cout<<"Case #"<<cnt<<":"<<" "<<"IMPOSSIBLE"<<endl;
                        flag=1;
                        break;
                    }
                    else
                    {
                        if(str[j]=='-')
                            str[j]='+';
                        else
                            str[j]='-';
                    }
                }
                if(flag==1)
                    break;
            }
        }
        if(flag!=1)
            cout<<"Case #"<<cnt<<":"<<" "<<count<<endl;
        cnt++;
    }
    return 0;
}
