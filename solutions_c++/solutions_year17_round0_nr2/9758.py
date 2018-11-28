#include <bits/stdc++.h>
using namespace std;
#define MI            1000000000
#define clr(i, j)     memset(i, j, sizeof(i))
#define all(v)        ((v).begin(), (v).end())
typedef long long     ll;
typedef long double   ld;
typedef vector<int>   vi;

ll power(int X, int Y)
{
    if(Y == 0)
        return 1;
    ll temp = power(X, Y/2);
    if(Y%2 == 0)
        return temp*temp;
    else
        return temp*temp*X;
}
ll GM(ll L)
{
    return L%1000000007;
}
int to_int(string b)
{
    int in = 0;
    ll p = power(10 , b.size()-1);
    for(int i = 0;i<b.size();i++)
    {
        in += (b[i]-'0')*p;
        p /= 10;
    }
    return in;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ll n;
    cin >> n;
    ll a[n];
    for(int i=0; i<n; i++)
            cin >> a[i];

    for(int i=0; i<n; i++)
    {
        cout << "Case #" << i+1 << ": ";
        stringstream str;
        str << a[i];
        string s = str.str();
        int f = 0;
        char x = '-1';
        char y = '-1';
        for(int j=1 ; j<s.size(); j++)
        {
            if(s[j] < s[j-1] && j >= 1)
            {
                y = s[j];
                x = s[j-1];
                break;
            }
        }
        //cout << x << endl;
        //cout << x << " " << y << endl;
        if (x == '1' && y != x)
        {
            //cout << "b";
            for(int j=0; j<s.size()-1; j++)
            {
                cout << 9;
            }
            cout << endl;
        }
        else if(x == y)
        {
            cout << s << endl;
        }

        else
        {
            //cout << x << " " << y << endl;
            int c = 0;
            int k = 0;
            for(int j=1; j<s.size(); j++)
            {
                int m = 0;
                if(k == 0)
                {
                    while(s[j-1] > s[j])
                    {
                        k = 1;
                        s[j-1]--;
                        s[j] = '9';
                        c = 1;
                        j--;
                        m = j;
                    }
                }
                if(c == 1 && j > m)
                    s[j] = '9';
            }
            cout << s << endl;
        }

    }

}
