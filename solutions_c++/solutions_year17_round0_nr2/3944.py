#include <bits/stdc++.h>

using namespace std;



string solve()
{
    string s;
    cin >> s;
    long long int n = s.size();

    long long i = n-1;
    while(i>0)
    {
        if(s[i]>=s[i-1])
        {
            i--;
            continue;
        }
        for(int k=i;k<n;++k) s[k] = '9';
        i--;
        while(s[i]=='0')    {s[i]='9';i--;}
        s[i]--;
    }

    if(s[0]=='0')
    {
        s.erase(s.begin());
        for(int i=0;i<s.size();++i) s[i] = '9';
    }

    return s;
}

int main()
{


    long long T;
    cin >> T;
    for(long long t=1;t<=T;++t)
    {
        cout << "Case #" << t << ": " << solve() << "\n";
    }
    return 0;
}
