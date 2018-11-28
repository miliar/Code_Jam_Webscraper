#include <bits/stdc++.h>
using namespace std;
void solve(int tt)
{
    long long n,ans = 0;
    cin>> n;
    char q[100]={0};
    sprintf(q,"%lld",n);
    cout<<"Case #" << tt << ": ";
    if(strlen(q)==1){cout << n << endl;
    return ;
    }
    int i;
    for(i = 1 ; i < strlen(q) ; i++)
        if( q[i] < q[i-1]) break;
    if(i==strlen(q)){
            cout << n <<endl;
    return ;}


    int cn[3] = {0,0,0};

    for(int i = 0; i < strlen(q) - 1 ; i++)
        ans= ans * 10 + 9;
    for(i = 0 ; i < strlen(q) - 1;i++)
    {
        if(q[i]=='0') cn[0]++;
        else if(q[i]=='1') cn[1]++;
        else cn[2]++;
        if(q[i] == '0' && cn[2] ==0)  break;
    }
    if(cn[2]==0 || i <(strlen(q)-1)) {
            cout<<ans<<endl;
            return;}
     for(i = 0; i < strlen(q)-1;i++)
    {
        if((q[i+1]<q[i])&&q[i]>'1')
        {
            q[i]--;
            for(int j = i + 1 ; j < strlen(q);j++)q[j]='9';
            for(int j = i - 1 ; j >= 0 ; j--)
            {
                if(q[j] <= q[j+1]) break;
                else
                {
                    q[j]--;
                    q[j+1]='9';
                }
            }
             break;
        }

    }
    cout<< q <<endl;
}
int main()
{
   freopen("test.in","r",stdin);
   freopen("res.txt","w",stdout);
   int T;
   cin >> T;
   for(int i = 1 ; i <= T ; i++)
      solve(i);
    return 0;
}
