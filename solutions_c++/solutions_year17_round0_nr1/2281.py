#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int test()
{
    string s;
    int k;
    cin >> s >> k;
    int ans = 0;
    for(int i=0;i+k-1<s.size();i++)
    {
        if(s[i]=='-')
        {
            ans++;
            for(int j=i;j<i+k;j++)
            {
                if(s[j]=='-') s[j] = '+';
                else s[j] = '-';
            }
        }
    }
    for(int i=0;i<s.size();i++)
        if(s[i]=='-')
            return -1;
    return ans;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        int a = test();
        cout << "Case #" << i+1 << ": ";
        if(a==-1) cout << "IMPOSSIBLE\n";
        else cout << a << '\n';
    }
    return 0;
}