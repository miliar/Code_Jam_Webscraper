#include<bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define lol long long
#define ld long double
#define db double
#define x first
#define y second
#define j1 sdfdsf
#define y0 gjkldf
#define fc cin.tie(NULL);ios_base::sync_with_stdio(false);

using namespace std;

const int N = 1e3+5;
const int M = 1e3;
const int inf = 2e9;
const int md = 1e9+7;
const db eps = 1e-6;

int t,it;
int n,i,R,G,B,Y,O,V;
string s1,s2,s3,ans;

void createS()
{
    while (O > 0)
    {
        s1 += "BO";
        --O;
        --B;
    }
    while (G > 0)
    {
        s2 += "RG";
        --G;
        --R;
    }
    while (V > 0)
    {
        s3 += "YV";
        --V;
        --Y;
    }
}

void addR()
{
    if (R == 0) return;
    if (R > 1) ans += 'R';
    else
    {
        if (s2.size()>0) ans += s2;
        else ans += 'R';
    }
    --R;
}
void addB()
{
    if (B == 0) return;
    if (B > 1) ans += 'B';
    else
    {
        if (s1.size()>0) ans += s1;
        else ans += 'B';
    }
    --B;
}
void addY()
{
    if (Y == 0) return;
    if (Y > 1) ans += 'Y';
    else
    {
        if (s3.size()>0) ans += s3;
        else ans += 'Y';
    }
    --Y;
}

int main()
{
    fc


    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);


    cin>>t;
    it = 0;
    while (t--)
    {
        cin>>n>>R>>O>>Y>>G>>B>>V;
        ++it;
        cout<<"Case #"<<it<<": ";


        if (O > B || G > R || V > Y)
        {
            cout<<"IMPOSSIBLE\n";
            continue;
        }

        ans = "";
        s1 = s2 = s3 = "";
        createS();

        if (s1.size() > 0 && s2.size()+s3.size()+R+O+G+B+V+Y == 0)
        {
            cout<<s1<<"\n";
            continue;
        }
        if (s2.size() > 0 && s1.size()+s3.size()+R+O+G+B+V+Y == 0)
        {
            cout<<s2<<"\n";
            continue;
        }
        if (s3.size() > 0 && s2.size()+s1.size()+R+O+G+B+V+Y == 0)
        {
            cout<<s3<<"\n";
            continue;
        }

        if (s1.size() > 0)
        {
            if (B == 0)
            {
                cout<<"IMPOSSIBLE\n";
                continue;
            }
            s1 += 'B';
        }
        if (s2.size() > 0)
        {
            if (R == 0)
            {
                cout<<"IMPOSSIBLE\n";
                continue;
            }
            s2 += 'R';
        }
        if (s3.size() > 0)
        {
            if (Y == 0)
            {
                cout<<"IMPOSSIBLE\n";
                continue;
            }
            s3 += 'Y';
        }

        if (max(R,max(B,Y)) > (R + B + Y) / 2)
        {
            cout<<"IMPOSSIBLE\n";
            continue;
        }

        /*if (it == 3)
        {cout<<R<<" "<<B<<" "<<Y<<"\n"; return 0;}*/

        while (R + B + Y > 0)
        {
                if (R > B && R > Y)
                {
                    addR();
                    addB();
                    addR();
                    addY();
                } else
                if (B > R && B > Y)
                {
                    addR();
                    addB();
                    addY();
                    addB();
                } else
                if (Y > R && Y > B)
                {
                    addR();
                    addY();
                    addB();
                    addY();
                } else
                {
                    if (ans[ans.size()-1] != 'R') addR();
                    if (ans[ans.size()-1] != 'B') addB();
                    if (ans[ans.size()-1] != 'Y') addY();
                }
        }

        cout<<ans<<"\n";

        /*
        if (R > 0 || Y > 0 || B > 0) {cout<<R<<" "<<Y<<" "<<B<<"\n";return 0;}
        for (i=1; i<ans.size(); ++i)
        if (ans[i] == ans[i-1]) {cout<<"AAA";return 0;}
        if (ans[0] == ans[ans.size()-1]) {cout<<"AAA";return 0;}*/
    }
}
