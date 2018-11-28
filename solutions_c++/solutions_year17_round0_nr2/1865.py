#include <bits/stdc++.h>

using namespace std;
long long inp;
int dp[20][10][2];
string ip;
string ans;
bool solve(int idx,int last,bool Reduced)
{
    if(idx==ip.size())
        return dp[idx][last][Reduced]=1;
    int &ret=dp[idx][last][Reduced];
    if(ret!=-1)
        return ret;
    ret=0;
    if(ip[idx]<last+'0'&&!Reduced)
        return ret;
    for(int i=9;i>=0;i--){
        if(Reduced)
            ret|=solve(idx+1,9,1);
       else if(i+'0'==ip[idx])
            ret|=solve(idx+1,i,Reduced);
        else if(i+'0'<ip[idx]&&i+'0'>=last+'0')
            ret|=solve(idx+1,i,1);
    }
    return ret;
}
void backtrack(int idx,int last,bool Reduced)
{
    if(idx==ip.size())
        return ;
    for(int i=9;i>=0;i--){
        if(Reduced&&dp[idx+1][9][1]){
            ans.push_back(9+'0');
            backtrack(idx+1,9,1);
            return ;
        }
       else if(i+'0'==ip[idx]&&dp[idx+1][i][Reduced]){
            ans.push_back(i+'0');
            backtrack(idx+1,i,Reduced);
            return ;
       }
        else if(i+'0'<ip[idx]&&i+'0'>=last+'0'&&dp[idx+1][i][1]){
            ans.push_back(i+'0');
            backtrack(idx+1,i,1);
            return;
        }
    }
    return;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int cases=0;
    while(T--){
        cases++;
        memset(dp,-1,sizeof dp);
        cin>>inp;
        ip.clear();
        while(inp){
            ip.push_back(inp%10+'0');
            inp/=10;
        }
        reverse(ip.begin(),ip.end());
        solve(0,0,0);
        ans.clear();
        backtrack(0,0,0);
        reverse(ans.begin(),ans.end());
        while(ans.back()=='0'&&ans.size()>1)
        ans.pop_back();
        reverse(ans.begin(),ans.end());
        cout<<"Case #"<<cases<<": "<<ans<<endl;
    }
}
