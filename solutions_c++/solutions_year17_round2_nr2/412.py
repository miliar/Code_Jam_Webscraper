#include <bits/stdc++.h>

using namespace std;

const int MaxN = 1e3 + 15;
const int INF = 1e9;
const int MOD = 1e9 + 7;

int cases;


int n, r, o, y, g, b, v;

pair<long double, long double> a[MaxN];

/**
RY = O
YB = G
RB = V
*/

string prnt(char a, char b, int & A, int & B)
{
    if(!A)
        return "";
    string res;
    res.push_back(b);
    --B;
    for(int i = 1; i <= A; ++i)
    {
        res.push_back(a);
        res.push_back(b);
        --B;
        --A;
    }
    return res;
}

bool bad(string ans)
{
    for(int i = 0; i + 1 < ans.size(); ++i)
        if(ans[i] == ans[i + 1])
            return true;
    return ans[0] == ans.back();
}

void ins(string & s, int pos, char q)
{
    string res;
    for(int i = 0; i <= pos; ++i)
        res.push_back(s[i]);
    res.push_back(q);
    for(int i = pos + 1; i < s.size(); ++i)
        res.push_back(s[i]);
    s = res;
}

void add(string & s, char q)
{
    for(int i = 0; i + 1 < s.size(); ++i)
        if(s[i] == s[i + 1])
        {
            ins(s, i, q);
            return;
        }
    if(s.empty())
    {
        s.push_back(q);
        return;
    }
    if(s[0] == q || s.back() == q)
    {
        for(int i = 0; i + 1 < s.size(); ++i)
            if(s[i] != q && s[i + 1] != q)
            {
                ins(s, i, q);
                return;
            }
        s.push_back(q);
    }else
    {
        reverse(s.begin(), s.end());
        s.push_back(q);
        reverse(s.begin(), s.end());
    }
}

void solve()
{
    ++cases;
    cout << "Case #" << cases << ": ";
    cin >> n >> r >> o >> y >> g >> b >> v;
    /// ob

    if(b + 1 < o || r + 1 < g || y + 1 < v)
    {
        cout << "IMPOSSIBLE\n";
        return;
    }

    string OB = prnt('O', 'B', o, b);
    string GR = prnt('G', 'R', g, r);
    string VY = prnt('V', 'Y', v, y);


    if(OB.size())
        ++b;
    if(GR.size())
        ++r;
    if(VY.size())
        ++y;

    string ans;



    if(b >= r && b >= y)
    {
        for(int i = 0; i < b; ++i)
            ans.push_back('B');
        b = 0;
    }else
    if(r >= b && r >= y)
    {
        for(int i = 0; i < r; ++i)
            ans.push_back('R');
        r = 0;
    }else
    {
        for(int i = 0; i < y; ++i)
            ans.push_back('Y');
        y = 0;
    }

    for(int i = 0; i < b; ++i)
        add(ans, 'B');

    for(int i = 0; i < r; ++i)
        add(ans, 'R');

    for(int i = 0; i < y; ++i)
        add(ans, 'Y');


    bool Y = (VY.empty());
    bool R = (GR.empty());
    bool B = (OB.empty());

    if(bad(ans))
    {
        cout << "IMPOSSIBLE\n";
        return;
    }




    for(int i = 0; i < ans.size(); ++i)
    {
        if(ans[i] == 'Y')
        {
            if(Y)
                cout << 'Y';
            else
            {
                Y = true;
                cout << VY;
            }
        }else
        if(ans[i] == 'B')
        {
            if(B)
                cout << 'B';
            else
            {
                B = true;
                cout << OB;
            }
        }else
        {
            if(R)
                cout << 'R';
            else
            {
                R = true;
                cout << GR;
            }
        }
    }

    cout << '\n';
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
//    ios_base :: sync_with_stdio(false);
//    cin.tie(NULL);
    int t;
    cin >> t;
    while(t --> 0)
        solve();
    return 0;
}
