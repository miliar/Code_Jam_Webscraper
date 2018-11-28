#include <bits/stdc++.h>
using namespace std;

int n[1100]={0};
int dp[1100]={0};

int main()
{

    int t,k,i,j,swaps_occ;
    string str;
    ifstream fin ("C:\\Users\\ADMIN\\Desktop\\CodeJam17\\input.txt");
    ofstream fout ("C:\\Users\\ADMIN\\Desktop\\CodeJam17\\sol.txt");
    fin>>t;
    for(j=1;j<=t;j++)
    {
        fin>>str>>k;
        n[0]=0;
        dp[0]=0;
        swaps_occ=0;
        for(i=0;str[i]!='\0';i++)
        {
            swaps_occ=dp[i];
            if(i>=k){
                swaps_occ-=dp[i-k+1];
            }
            if(str[i]=='+'){
                    dp[i+1]=dp[i]+(swaps_occ%2);
            }
            else{
                    dp[i+1]=dp[i]+(1-(swaps_occ%2));
            }
        }
        if(dp[i]==dp[i-k+1])
            fout<<"Case #"<<j<<": "<<dp[i]<<"\n";
        else
            fout<<"Case #"<<j<<": IMPOSSIBLE\n";
    }

    return 0;
}
