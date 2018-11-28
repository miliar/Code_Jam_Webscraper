#include<bits/stdc++.h>

using namespace std;
const int INF = 123456789;


int solve(int a[], int M, int N, int want) {
  int s[M]; 
  memset(s,0,sizeof s);
  
  int sum=0, ans=0;
  
  for(int i = 0 ; i < M ; i++)
  {
      s[i] = (a[i]+sum)%2 != want;
      
      sum += s[i] - (i>=N-1?s[i-N+1]:0);
      
      ans += s[i];
      
      if(i>M-N && s[i]!=0) return INF;  
  }

  return ans;
}

int main() {

  freopen("A1.in","r",stdin);
  freopen("A2.out","w",stdout);  
  int t;
  cin>>t;
  for(int tt = 1 ; tt <= t ; tt++)
  {
        cout<<"Case #"<<tt<<": ";
        string s;
        int k;
        cin>>s>>k;
        int M = s.size();
        int a[M];
        for(int i = 0 ; i < M ; i++)
        {
            if(s[i] == '+')
                a[i] = 1;
            else
                a[i] = 0;
        }
        
        //printf("Need %d flips to 0 and and %d flips to 1\n",
        
        int ans = solve(a, M, k, 1);

        if(ans != INF)
            cout<<ans<<endl;
        else
            cout<<"IMPOSSIBLE"<<endl;
  }
  
}