#include<bits/stdc++.h>
#define MX 1005
using namespace std;
typedef long long ll;

pair< int, char > ara[MX], tmp[MX];

int main(){
     freopen("input4.txt", "r", stdin);
     freopen("output4.txt", "w", stdout);
     int i, j, k;
     int n, t, T, flag;
     char prev;
     string ans;
     cin >> T;
     for(t=1; t<=T; ++t){
          cin >> n;
          cin >> ara[0].first; cin >> ara[3].first;
          cin >> ara[1].first; cin >> ara[4].first;
          cin >> ara[2].first; cin >> ara[5].first;
          ara[0].second='R'; ara[3].second='O';
          ara[1].second='Y'; ara[4].second='G';
          ara[2].second='B'; ara[5].second='V';
          cout << "Case #" << t << ": ";
          for(i=0; i<6; ++i) tmp[0]=ara[0];
          if(ara[0].first){
               flag=0;
               ara[0].first--;
               ans="R";
               prev='R';
               for(i=0; i<n-1; ++i){
                    sort(ara, ara+3);
                    for(j=2; j>=0; --j){
                         if(ara[j].first && ara[j].second!=prev){
                              ans+=ara[j].second;
                              prev=ara[j].second;
                              prev=ara[j].second;
                              ara[j].first--;
                              break;
                         }
                    }
                    if(j<0) flag=1;
               }
               k=ans.length();
               if(ans[0]==ans[k-1]) flag=1;
               if(!flag){
                    cout << ans << endl;
                    continue;
               }
               for(i=0; i<6; ++i) ara[0]=tmp[0];
          }
          if(ara[1].first){
               flag=0;
               ara[1].first--;
               ans="Y";
               prev='Y';
               for(i=0; i<n-1; ++i){
                    sort(ara, ara+3);
                    for(j=2; j>=0; --j){
                         if(ara[j].first && ara[j].second!=prev){
                              ans+=ara[j].second;
                              prev=ara[j].second;
                              ara[j].first--;
                              break;
                         }
                    }
                    if(j<0) flag=1;
               }
               k=ans.length();
               if(ans[0]==ans[k-1]) flag=1;
               if(!flag){
                    cout << ans << endl;
                    continue;
               }
               for(i=0; i<6; ++i) ara[0]=tmp[0];
          }
          if(ara[2].first){
               flag=0;
               ara[2].first--;
               ans="B";
               prev='B';
               for(i=0; i<n-1; ++i){
                    sort(ara, ara+3);
                    for(j=2; j>=0; --j){
                         if(ara[j].first && ara[j].second!=prev){
                              ans+=ara[j].second;
                              prev=ara[j].second;
                              ara[j].first--;
                              break;
                         }
                    }
                    if(j<0) flag=1;
               }
               k=ans.length();
               if(ans[0]==ans[k-1]) flag=1;
               if(!flag){
                    cout << ans << endl;
                    continue;
               }
               for(i=0; i<6; ++i) ara[0]=tmp[0];
          }
          cout << "IMPOSSIBLE" << endl;
     }
     return 0;
}
