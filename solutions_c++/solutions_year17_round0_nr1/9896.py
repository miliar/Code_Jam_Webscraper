#include <bits/stdc++.h>

using namespace std;

const int INF = 20000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(int a[], int M, int N, int want) {
    
    int s[M]; FOR(i,M) s[i] = 0;
    int sum=0, ans=0;
    
    FOR(i,M) {
        s[i] = (a[i]+sum)%2 != want;
        sum += s[i] - (i>=N-1?s[i-N+1]:0);
        ans += s[i];
        if(i>M-N and s[i]!=0) return INF;
    }

  return ans;
}

int main() {
  
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin>>t;
    string s = "";
    int n;
    for(int i = 0 ; i < t ; i ++){
        cin>>s;
        cin>>n;
        int v[s.size()];
        for(int j = 0 ; j < s.size(); j++){
            if(s[j]=='+'){
                v[j]=1;
            }
            else{
                v[j]=0;
            }
        }
        int x = flips(v,s.size(),n,1);
        if(x == INF){
            cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        }
        else{
            cout<<"Case #"<<i+1<<": "<<x<<endl;
        }
    }

}