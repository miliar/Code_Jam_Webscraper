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
string s;
int k;

int n;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    freopen("Test.inp","r",stdin);
    freopen("Test.out","w",stdout);
    cin >> n;
    int cnt=0;
    for (int i=1;i<=n;i++)
    {
        cin >> s >> k;
        int cnt=0;
        for (int i=0;i<=s.length()-k;i++)
            if (s[i]=='-')
            {
                for (int j=i;j<=i+k-1;j++)
                    if (s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                cnt+=1;
            }
        for (int i=0;i<s.length();i++)
            if (s[i]=='-')
                cnt=-1;
        cout << "Case #" << i << ": ";
        if (cnt==-1)
            cout << "IMPOSSIBLE\n";
        else
            cout << cnt << "\n";
    }
    return 0;
}
