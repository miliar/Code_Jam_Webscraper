#include <bits/stdc++.h>
#define LL long long
using namespace std;
int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T;
    int n, k;
    cin>>T;
    bool flag;
    priority_queue <LL> q;
    for(int tt=1; tt<=T; tt++)
    {
        while(q.size())q.pop();
        scanf("%d%d", &n, &k);
        int i=-1;
        int x = 0, tot = 0;
        q.push(n);
        while(q.size())
        {
            //i++;
            //x = 1<<i;
            //int sz = q.size();
            //while(sz--)
            //{
                tot++;
                n = q.top();
                q.pop();

                if(n == 1){n = 0; flag = 1; break;}
                flag = 0;

                if((n-1) % 2 != 0){
                    n = (n-1) / 2 + 1;
                    if(n)q.push(n);
                    if(n)q.push(n-1);
                }
                else{
                    n = (n-1) / 2;
                    if(n)q.push(n);
                    if(n)q.push(n);
                    flag = 1;
                }

                //cout<<"now: "<<n<<endl;
              //  if(tot >= k)break;
            //}
            //if(n == 1){n--;flag=1;break;}
            if(tot >= k)break;
        }
        if(!flag)
            printf("Case #%d: %d %d\n", tt, n, n-1);
        else
            printf("Case #%d: %d %d\n", tt, n, n);
    }
return 0;
}
