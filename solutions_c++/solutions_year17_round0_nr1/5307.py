#include <bits/stdc++.h>
using namespace std;
map <string, bool> m1;
void init(){
    m1.clear();
}
int counter(string strr)
{
    int pl = 0;
    for(int i=0; i<strr.size(); i++)
    {
        if(strr[i] == '+')pl++;
    }
    return pl;
}

string flip(string str1, int i, int k)
{
    for(int j = i; j < i+k; j++)
    {
        if(str1[j] == '-')str1[j] = '+';
        else str1[j] = '-';
    }
return str1;
}

int bfs(int k, string str1)
{
    string str2;
    queue <string> q;
    q.push(str1);
    int stps = -1;
    while(q.size())
    {
        int sz = q.size();
        stps++;

        while(sz--)
        {
            str2 = q.front();
            q.pop();
            if(counter(str2) == str2.size())return stps;

            for(int i=0; i <= str2.size() - k; i++)
            {
                string str3 = flip(str2, i, k);
                if(!m1[str3])
                {
                        m1[str3] = 1;
                        q.push(str3);
                }
            }
        }
    }
return -1;
}

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("out.txt", "wt", stdout);
    int T, sol, k;
    string str1;
    cin>>T;
    for(int tt=1; tt<=T; tt++)
    {
        init();
        cin>>str1;
        scanf("%d", &k);

        sol = bfs(k, str1);
        if(sol != -1)
            printf("Case #%d: %d\n", tt, sol);
        else
            printf("Case #%d: IMPOSSIBLE\n", tt);
    }
return 0;
}
