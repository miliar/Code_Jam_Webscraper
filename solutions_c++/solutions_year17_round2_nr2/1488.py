#include <bits/stdc++.h>
#define F first
#define S second
typedef long long ll;
using namespace std;

int main()
{
    int tt;
    cin>>tt;
    for(int t = 1; t <= tt; t++)
    {
        int n, num;
        pair<int, char>c[6];
        cin>>n;
        cin>>num;
        c[0] = make_pair(num, 'R');
        cin>>num;
        c[1] = make_pair(num, 'O');
        cin>>num;
        c[2] = make_pair(num, 'Y');
        cin>>num;
        c[3] = make_pair(num, 'G');
        cin>>num;
        c[4] = make_pair(num, 'B');
        cin>>num;
        c[5] = make_pair(num, 'V');
        sort(c, c+6);
        string ans = "";

        num = c[4].F - c[3].F;
        c[5].F -= num;
        c[4].F -= num;
        while(num--)
            ans = ans + c[5].S + c[4].S;

        while(c[3].F > 0 && c[5].F > c[3].F)
        {
            ans = ans + c[5].S + c[4].S + c[5].S + c[3].S;
            c[5].F -= 2;
            c[4].F--;
            c[3].F--;
        }
        // cout<<c[5].F<<' '<<c[4].F<<' '<<c[3].F;
        cout<<"Case #"<<t<<": ";
        if(c[5].F == c[4].F)
        {
            while(c[5].F--)
                ans = ans + c[5].S + c[4].S + c[3].S;
            cout<<ans<<"\n";
        }
        else
        {
            cout<<"IMPOSSIBLE\n";
        }
    }
    return 0;
}
