#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int N;
    cin >> N;
    for (int i = 1; i<=N; i++)
    {
        string s;
        cin >> s;
        printf("Case #%d: ",i);
        int j;
        int flag = s.length();
        flag+=10;
        for (j = s.length()-1; j>0 ; j--)
        {
            if (s[j]<s[j-1])
             {
                 flag = j-1;
                 s[j-1] = s[j-1]-1;
                 s[j]='9';
             }
        }
        int k = 0;
        while (s[k]=='0')k++;
        for (;k<s.length();k++)
        {
            if (k>flag) cout <<9;
            else cout << s[k];
        }
        cout << endl;
    }
}
