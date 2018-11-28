#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    freopen("in1.in","r", stdin);
    freopen("out.txt","w", stdout);
    int t;
    cin>>t;
    for(int i = 1; i<=t;i++)
    {
        int q = 0;
        string s;
        int k;
        cin>>s>>k;
        int len = s.length();
        for (int j=0;j<len-k+1;j++)
        {
            if(s[j]=='-')
            {
                for(int r=0;r<k;r++){
                    if(s[j+r]=='+')
                        s[j+r] = '-';
                    else s[j+r] = '+';
                }
                q++;
            }
        }
        int p = 0;
        for(int j = 0;j<k;j++ )
        {
            if (s[len-j] == '-'){
                cout << "Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
                p = 1;
                break;
            }
        }
        if(p ==1) continue;
        cout << "Case #"<< i<<": "<<q<<endl;
    }
    return 0;
}
