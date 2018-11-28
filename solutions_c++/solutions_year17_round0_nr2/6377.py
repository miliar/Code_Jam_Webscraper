#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    int t, idx, s, i;
    string n;
    cin>>t;
    for(int tt = 1; tt <=t; tt++)
    {
        cout<<"Case #"<<tt<<": ";
        cin>>n;
        s = n.length();
        idx = -1;
        for(i = 0; i < s-1; i++)
        {
            if(n[i] > n[i+1])
            {
                idx = i;
                break;
            }
        }

        if(idx == -1)
        {
            cout<<n<<"\n";
            continue;
        }

        while(idx > 0 && n[idx] == n[idx-1]) idx--;
        n[idx]--;
        for(i = idx + 1; i < s; i++)
            n[i] = '9';
        for(i = 0; i < s; i++)
            if(n[i] > '0')
                cout<<n[i];
        cout<<"\n";
    }
    return 0;
}
