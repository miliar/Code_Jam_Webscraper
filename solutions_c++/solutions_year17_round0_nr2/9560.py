/* <3 <3 <3 */
#include  <bits/stdc++.h>

using namespace std;

#define ii pair <int,int>
#define iii pair <ii,int>
#define fi first
#define se second
#define ll long long
#define ull unsigned long long

const int dx[4]={0,1,0,-1};
const int dy[4]={1,0,-1,0};
const int oo = 1e9;
int t;
string s;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("Test.inp","r",stdin);
    freopen("Test.out","w",stdout);
    cin >> t;
    int u;
    for (int t_=1;t_<=t;t_++)
    {
        cin >>s;
        u=-1;
        if (s.length()==1)
        {
            cout << "Case #" << t_ << ": ";
            cout << s << endl;
            continue;
        }
        for (int j=s.length()-2;j>=0;j--)
        {
            if (s[j]>s[j+1])
            {
                u=j;
                break;
            }
        }
        cout << "Case #" << t_ << ": ";
        if (u==-1)
        {
            cout << s << endl;
            continue;
        }
        while (s[u]<=s[u-1] && u>0)
            u-=1;
        s[u]-=1;
        for (int i=u+1;i<s.length();i++)
            s[i]='9';
        if (s[0]!='0')
            cout << s ;
        else
            for (int i=1;i<s.length();i++)
                cout << s[i];
        cout << endl;
    }
    return 0;
}
