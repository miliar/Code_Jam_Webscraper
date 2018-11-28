#include <bits/stdc++.h>

using namespace std;

const int N = 1e3+5;
const int INF = 1e9;

int t, k;
string s;

int solve(string st){
      int sz = st.size(), res = 0;
      for(int i=0; i<sz; i++){
            if(st[i]=='-'){
                  res++;
                  if(i+k >sz)
                        return INF;
                  for(int j=i; j<i+k; j++){
                        if(st[j]=='+')
                              st[j] = '-';
                        else
                              st[j] = '+';
                  }
            }
      }
      return res;
}

int main()
{
      ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
      cin>>t;
      for(int ca = 1; ca<=t; ca++){
            cin>>s>>k;
            int a1 = solve(s);
            reverse(s.begin(), s.end());
            int a2 = solve(s);
            //cout<<s<<" "<<k<<" "<<a1<<" "<<a2<<"\n";
            cout<<"Case #"<<ca<<": ";
            if(a1 == INF && a2 == INF){
                  cout<<"IMPOSSIBLE\n";
            }
            else
                  cout<<min(a1, a2)<<"\n";
      }
      return 0;
}
