/**/
#include <bits/stdc++.h>
#define MAX 1002
#define flip(ch) (ch=='-')?'+':'-'
using namespace std;

int main()
{
    freopen("aL.in", "r", stdin);
    freopen("aL.out", "wt", stdout);
    int t, _t=1;
    cin>>t;
    while(_t<=t)
    {
        char pancakes[MAX], ch;
        cin>>pancakes;
        int n = strlen(pancakes), k;
        cin>>k;
        int i = 0, flips = 0;
        while(i<=n-k)
        {
            if(pancakes[i]=='-')
            {
                for(int j=0;j<k;j++)
                    pancakes[i+j]=flip(pancakes[i+j]);
                flips++;
            }
            i++;
        }
        bool flag = false;
        for(i=0;i<n;i++)
            if(pancakes[i]=='-')
                flag = true;
        
        printf("Case #%d: ", _t);
        if(flag==true)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<flips<<endl;
        _t++;
    }
    return 0;
}
/**/