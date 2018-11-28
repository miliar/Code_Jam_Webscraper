#include <bits/stdc++.h>
using namespace std;
bool inp[1005];
int n,k;

void flip(int ind)
{
    for(int i = ind;i<ind+k;i++) inp[i] = !inp[i];
}
int main()
{
    freopen ("A-large (2).in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    //ifstream F("prefix.in");   //for eof problem
    char c;
    int T;
    string s;
    cin>>T;
    for(int t = 1; t<=T;t++)
    {
        cin>>s>>k;
        n = s.length();
        for(int i = 1;i<=n;i++)
        {
            c = s[i-1];
            if(c=='-') inp[i] = 0;
            else inp[i] = 1;
        }
        bool impos = false;
        int co = 0;
        for(int i = 1;i<=n;i++)
        {
            if(inp[i] == 0)
            {
                if(i>n-k+1)
                {
                    impos = true;
                    break;
                }
                flip(i);
                co++;
            }
        }
        if(impos)
            printf("Case #%d: IMPOSSIBLE\n",t);
        else
            printf("Case #%d: %d\n",t, co);

    }
    return 0;
}
