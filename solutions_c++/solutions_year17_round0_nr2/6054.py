#include <bits/stdc++.h>
using namespace std;

bool isTidy(string s)
{
    int n = s.size();
    for(int i = 1; i < n; i++)
        if(s[i] < s[i - 1])
            return false;
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int T,n,ntest=1;
    string s;
    cin >> T;
    while(T--)
    {
        cin >> s;
        if(!isTidy(s))
        {
            n = s.size();
            for(int i = n-2; i >= 0; i--)
                if(s[i] > s[i+1])
                {
                    for(int j = i+1; j < n; j++)
                        s[j] = '9';
                    s[i]--;
                }
            if(s[0] == '0')
                s = s.substr(1);
        }
        cout << "Case #" << ntest++ << ": " << s << '\n';
    }
    return 0;
}
