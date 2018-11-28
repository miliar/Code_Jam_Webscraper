#include <iostream>
#include <string>
using namespace std;



int main()
{
    int t;
    cin>>t;
    int count = 1;
    while(count <= t)
    {
        string S;
        int k;
        cin>>S>>k;

        int len = S.size(), ctr = 0, flag = 0;
        for(int i=0;i<=len-k;i++)
        {
            if(S[i] == '-')
            {
                for(int j=0;j<k;j++)
                {
                    if(S[i+j]=='+')
                        S[i+j]='-';
                    else
                        S[i+j]='+';

                }
                ctr++;
            }
        }
        for(int i=1;i<len;i++)
        {
            if(S[i]!=S[i-1])
            {
                flag = 1;
                break;
            }
        }
        if(flag == 0)

            cout<<"Case #"<<count<<": "<<ctr<<"\n";

        else
            cout<<"Case #"<<count<<": IMPOSSIBLE\n";

        count++;

    }
    return 0;
}
