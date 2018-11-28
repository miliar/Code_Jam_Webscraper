///my sister wrote this

#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl
#define pb push_back
using namespace std;
typedef long long ll;

#define zal1 hj[0].first
#define zal2 hj[1].first
#define zal3 hj[2].first


const int MAXN = 100005;

string s[3];
bool bf, rf, yf;
void print(char c)
{
    if (c == 'B' && !bf)
    {
        cout << s[0];
        bf = true;
    }
    else if (c == 'R' && !rf)
    {
        cout << s[1];
        rf = true;
    }
    else if (c == 'Y' && !yf)
    {
        cout << s[2];
        yf = true;
    }
    else cout << c;
}


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        int N, R, RY, Y, YB, B, RB;
        cin >> N >> R >> RY /*O*/ >> Y >> YB /*G*/ >> B >> RB /*V*/;
        cout << "Case #" << tt << ": ";

        if (RY == B && RY + B == N)
        {
            for (int i = 0;  i < B; i++)
            {
                cout << "OB";
            }
            cout << endl;
            continue;
        }
        if (RB == Y && RB + Y == N)
        {
            for (int i = 0;  i < Y; i++)
            {
                cout << "VY";
            }
            cout << endl;
            continue;
        }
        if (YB == R && YB + R == N)
        {
            for (int i = 0;  i < R; i++)
            {
                cout << "GR";
            }
            cout << endl;
            continue;
        }
        if ((RY && RY >= B) || (YB && YB >= R) || (RB && RB >= Y))
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }


        vector <pair <int, char> > hj;
        s[0].clear();
        s[1].clear();
        s[2].clear();
        bf = false;
        rf = false;
        yf = false;

        s[0].pb('B');
        for (int i = 0; i < RY; i++)
        {
            s[0].pb('O');
            s[0].pb('B');
        }
        B -= RY;

        s[1].pb('R');
        for (int i = 0; i < YB; i++)
        {
            s[1].pb('G');
            s[1].pb('R');
        }
        R -= YB;

        s[2].pb('Y');
        for (int i = 0; i < RB; i++)
        {
            s[2].pb('V');
            s[2].pb('Y');
        }
        Y -= RB;

        hj.pb({B, 'B'});
        hj.pb({R, 'R'});
        hj.pb({Y, 'Y'});

        sort(hj.begin(), hj.end());

        if (zal3 > zal1 + zal2)
        {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        while(zal1 + zal2 + zal3)
        {
            print(hj[2].second);
            zal3--;
            if (zal2 > zal3)
            {
                print(hj[1].second);
                zal2--;
            }
            if (zal1)
            {
                print(hj[0].second);
                zal1--;
            }
        }
        cout << endl;
    }

    return 0;
}


