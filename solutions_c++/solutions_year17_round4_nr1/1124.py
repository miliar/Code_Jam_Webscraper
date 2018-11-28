#include <bits/stdc++.h>
using namespace std;
int test,n,p,a[105];
int cnt[5];
int main(){
   freopen("A-large.in","r",stdin);
   freopen("Aout.txt","w",stdout);
   cin >> test;
   for(int id=1;id<=test;id++){
      cin >> n >> p;
      memset(cnt,0,sizeof(cnt));
      for(int i=1;i<=n;i++)   cin >> a[i], cnt[a[i] % p]++;
      if (p == 2){
         cout << "Case #" << id << ": " << cnt[0] + (cnt[1]+1)/2 << endl;
      }
      else if (p == 3){
         cout << "Case #" << id << ": " << cnt[0] + min(cnt[1],cnt[2]) + (cnt[1] + cnt[2] - 2 * min(cnt[1],cnt[2]) + 2) / 3 << endl;
      }
      else if (p == 4){
         int ans = cnt[0] + cnt[2] / 2 + min(cnt[1],cnt[3]);
         cnt[2] %= 2;
         int x = min(cnt[1],cnt[3]);
         cnt[1] -= x;
         cnt[3] -= x;
         if (!cnt[2]){
            cout << "Case #" << id << ": " << ans + (cnt[1] + cnt[3] + 3) / 4 << endl;
         }
         else{
            ans++;
            cout << "Case #" << id << ": " << ans + (max(cnt[1], cnt[3])-2 + 3) / 4 << endl;
         }
      }
   }
}
