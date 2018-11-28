#include<bits/stdc++.h>
#define ll long long int
#define F first
#define S second
#define M 1000000007
#define SI(x) scanf("%d", &x)
#define PI(x) printf("%d\n", x)
#define SL(x) scanf("%I64d", &x)
#define PL(x) printf("%I64d\n", x)
#define PB push_back
#define MP make_pair

using namespace std;

int main()
{
    freopen("gcj1w.txt","w",stdout);
    freopen("A-large.in","r",stdin);
    int t;
    cin >> t;
    int x = 1;
    while(t--)
    {
        char s[10000];
        int k;

        cin >> s >> k;
        int cnt = 0;
        int n = strlen(s);
        cout << "Case #" << x++ << ": ";
        for(int i = 0; i<n; i++)
        {
            if(s[i] == '-' && i+k<=n)
            {
                cnt++;
                for(int j = 0; j<k; j++)
                {
                    if(s[i+j] == '-') s[i+j] = '+';
                    else s[i+j] = '-';
                }
            }
        }
        bool f = 0;
        for(int i = 0; i<n; i++)
        {
            if(s[i] == '-')
            {
                f = 1;
                break;
            }
        }

        if(f) cout << "IMPOSSIBLE" << endl;

        else cout << cnt << endl;

    }
}
