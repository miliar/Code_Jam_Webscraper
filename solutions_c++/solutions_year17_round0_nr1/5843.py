#include<bits/stdc++.h>
//#include "A-small-practice.in"
#include <fstream>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1L.out","w",stdout);
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        string s;
        int k;
        cin>>s>>k;
        int cnt=0;
        int flag=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                if(i+k <= s.size())
                {
                    for(int j=i;j<i+k;j++)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
                    cnt++;
                }
                else
                {
                    flag=1;
                    break;
                }
               // cout << s << " " << i+k << endl;
            }
        }
        //cout << s << endl;
        if(!flag)
            printf("Case #%d: %d\n",t+1, cnt);

        else
            printf("Case #%d: IMPOSSIBLE\n",t+1);
    }

    return 0;
}
