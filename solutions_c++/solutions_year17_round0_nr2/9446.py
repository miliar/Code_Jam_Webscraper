#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

bool istidy(int n)
{
    ostringstream ss;

    ss<<n;

    string p = ss.str();
    if(p.length()==1)   return true;

    for(int i=1; i<p.size(); i++)
    {
        if(p[i]<p[i-1]) return false;
    }

    return true;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int test, cs = 0;

    scanf("%d", &test);

    while(test--)
    {
        int res = 1, n;

        cin>>n;

        for(int i=1; i<=n; i++)
        {
            if(istidy(i))   res = i;
        }

        cout<<"Case #"<<++cs<<": "<<res<<endl;
    }


    return 0;


}
/*
1
---+-++- 3
*/
