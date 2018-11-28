#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll n, k, t, lft, rgt, lftcnt, rgtcnt, ans;

int main(){
      ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
      cin>>t;
      for(int ca = 1; ca <=t; ca++){
            cin>>n>>k;
            ll tmp, cnt = 0, lftCnt = 0, rgtCnt = 0;
            if(!(n&1LL)){
                  lft = n;
                  lftCnt = 1;
                  rgt = 0;
                  rgtCnt = 0;
            }
            else{
                  rgt = n;
                  rgtCnt = 1;
                  lft = 0;
                  lftCnt = 0;
            }
            /*if(n&1LL){
                  lft = rgt = n/2;
                  lftCnt = rgtCnt = 1;
            }
            else{
                  lft = n/2; //even
                  rgt = lft - 1; //odd
                  lftCnt = rgtCnt = 1;
            }*/
            tmp = k;
            while(tmp){
                  cnt++;
                  tmp>>=1;
            }
            ll df = k - ((1<<(cnt-1))-1);
            //cout<<"dif: "<<df<<" "<<(1<<(cnt-1))<<" "<<cnt<<"\n";
            for(int i=1; i<cnt; i++){
                  ll a = lft/2;
                  ll b = max(0LL, a - 1);
                  ll c = rgt/2;
                  ll nl = 0, nr = 0;
                  //cout<<lft<<" "<<rgt<<" : "<<a<<" "<<b<<" "<<c<<"\n";
                  nl = lftCnt;
                  nr = lftCnt;
                  if(c&1)
                        nr += 2*rgtCnt;
                  else
                        nl += 2*rgtCnt;
                  lftCnt = nl;
                  rgtCnt = nr;
                  if(lft != 0)
                        if(a&1){
                              lft = b;
                              rgt = a;
                        }
                        else{
                              lft = a;
                              rgt = b;
                        }
                  else
                        if(c&1)
                              rgt = c;
                        else
                              lft = c;
            }
            //cout<<lft<<" "<<lftCnt<<" : "<<rgt<<" "<<rgtCnt<<"\n";
            cout<<"Case #"<<ca<<": ";
            if(lft >= rgt)
                  if(lftCnt >= df){
                        ans = lft/2;
                        cout<<ans<<" "<<max(0LL, ans-1)<<"\n";
                  }
                  else{
                        ans = rgt/2;
                        cout<<ans<<" "<<ans<<"\n";
                  }
            else
                  if(rgtCnt >= df){
                        ans = rgt/2;
                        cout<<ans<<" "<<ans<<"\n";
                  }
                  else{
                        ans = lft/2;
                        cout<<ans<<" "<<max(0LL, ans-1)<<"\n";
                  }
      }
      return 0;
}
