#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    string str;
    int n, k;
    cin >> n;
    for(int i=1; i<=n; i++)
    {
        cin >> str;
        for(int j=1; j<str.size(); j++)
        {
            if(str[j]<str[j-1])
            {
                while(j>1){
                    if(str[j-1]==str[j-2])
                        j--;
                    else break;
                }
                str[j-1]=str[j-1]-1;
                for(; j<str.size(); j++)
                    str[j]='9';
                break;
            }
        }
        if(str[0]=='0')
            cout << "Case #" << i << ": " << str.substr(1) << endl;
        else
            cout << "Case #" << i << ": " << str << endl;
    }
    return 0;
}
