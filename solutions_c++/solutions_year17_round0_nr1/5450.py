#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream myfile;
    myfile. open ("1LongOutput.txt");

    int t;
    cin>>t;
    int x=t;
    while(t--)
    {
        char s[1005];
        cin>>s;
        int k,flip=0,len,flag=1;
        len=strlen(s);
        cin>>k;
        for(int i=0;s[i] && flag;i++)
        {
            if(s[i]=='-')
            {
                flip++;
                int count=1;
                for(int j=i;j<len && count<=k;j++)
                {
                    count++;
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                if(count<=k)
                {
                    flag=0;
                    break;
                }
            }
        }
        if(flag)
            myfile<<"Case #"<<x-t<<": "<<flip<<"\n";
        else
            myfile<<"Case #"<<x-t<<": "<<"IMPOSSIBLE\n";

    }

return 0;
}
