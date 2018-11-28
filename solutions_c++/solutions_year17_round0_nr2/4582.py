#include <bits/stdc++.h>

using namespace std;

const int N = 50;

int t, dat[N], sz;
string n;

string solve(string num){
      //cout<<num<<" : "<<sz<<"\n";
      bool change = 1;
      int cnt = 0;
      while(change){
            cnt++;
            if(cnt > 100)
                  break;
            change = 0;
            for(int i=0; i<sz-1; i++){
                  if(num[i] > num[i+1]){
                        change = 1;
                        num[i]--;
                        for(int j=i+1; j<sz; j++){
                              num[j] = '9';
                        }
                  }
            }
      }
      //cout<<num<<"\n";
      return num;
}

int main(){
      ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
      cin>>t;
      for(int c = 1; c<=t; c++){
            cout<<"Case #"<<c<<": ";
            cin>>n;
            sz = n.size();
            if(sz==1){
                  cout<<n<<"\n";
                  continue;
            }
            string ans = solve(n);
            int i=0;
            while(ans[i]=='0')
                  i++;
            for(; i<sz; i++){
                  cout<<ans[i];
            }
            cout<<"\n";
      }
      return 0;
}
