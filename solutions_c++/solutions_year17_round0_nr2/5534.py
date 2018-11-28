#include <bits/stdc++.h>

#define lp(i,n) for(long long int i=0; i<n; i++)

#define ll long long
#define pb push_back
#define  mp make_pair
#define pii pair<int,int>
#define ff first
#define ss second
#define nl "\n"

#define EPS 1e-8
#define OO 10000000

#define on(i,n) i=i|(1<<n)
#define off(i,n) i=i& (~(1<<n))

using namespace std;
string s;

string dp[10][20][3];

string solve(int last, int idx, bool changed){

    if(idx==s.size()) return "";

    if(dp[last][idx][changed]!="-1") return dp[last][idx][changed];
     string ans="X";

     if(changed==0)
    if(s[idx]-'0'>= last)
        ans=solve(s[idx]-'0',idx+1,0);

                if(ans!="X") {
                string emp;
                emp.pb(s[idx]);
                ans=emp+ans;
                return  dp[last][idx][changed]=ans;
                }


        int i;
        if(changed==0){
            i=s[idx]-'0'-1;
           } else{
                i=9;
            }

        for(; i>=last; i--){
            ans=solve(i,idx+1,1);
              if(ans!="X") {
                string emp;
                emp.pb(i+'0');
                ans=emp+ans;
                return  dp[last][idx][changed]=ans;
                }

        }
        return  dp[last][idx][changed]="X";


}


int main(){
     freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int cs=1;
    int t; cin>>t;
    while(t--){

            lp(i,10){
                lp(j,20){
                    lp(k,3){
                        dp[i][j][k]="-1";

                    }

                }
            }

        cin>>s;
        printf("Case #%d: ", cs++);


        string ans=solve(0,0,0);

        reverse(ans.begin(),ans.end());
        while(ans.back()=='0') ans.pop_back();

        reverse(ans.begin(),ans.end());


        cout<<ans<<endl;;
    }



}
