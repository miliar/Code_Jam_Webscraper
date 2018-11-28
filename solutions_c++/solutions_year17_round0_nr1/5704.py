#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin >> test;
    for (int i = 1; i <= test; ++i)
    {
        char s[1001];
        int k,count=0,flag=0;
        cin>>s>>k;
        for(int j=0; j<strlen(s); j++)
        {
            if(s[j]=='-'&&j+k<=strlen(s))
            {
                    for(int p=j; p<j+k; p++)
                    {
                        if(s[p]=='+')
                            s[p]='-';
                        else
                            s[p]='+';
                         //   cout<<"p="<<p<<endl;
                    }
                    count++;

            }
        }
        for(int j=0; j<strlen(s); j++)
            if(s[j]=='-')
            {
                flag=1;
                break;
            }

        if(flag)
            cout << "Case #" << i << ": " <<"IMPOSSIBLE"<< endl;
        else
            cout << "Case #" << i << ": " <<count<< endl;
    }
    return 0;
}
