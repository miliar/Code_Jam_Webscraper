#include<bits/stdc++.h>
using namespace std;
const int INF = 20000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(vector<int> a, int M, int N, int want) {
  int s[M]; 
  FOR(i,M) s[i] = 0;
  int sum=0, ans=0;
  FOR(i,M) {
    s[i] = (a[i]+sum)%2 != want;
    sum += s[i] - (i>=N-1?s[i-N+1]:0);
    ans += s[i];
    if(i>M-N and s[i]!=0) 
        return INF;
  }
  return ans;
}


int solve(string &str,int k){
    if(str.length()==0){
        return 0;
    }
    vector<int> arr(str.length());
    for(int i=0;i<str.length();i++){
        if(str[i]=='-'){
            arr[i]=0;
        }
        else{
            arr[i]=1;
        }
    }
    return flips(arr, arr.size(), k, 1);
}
int main(){
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("output.txt");
    int tCase;
    in>>tCase;
    for(int t=1;t<=tCase;t++){
        string str;
        int k;
        in>>str>>k;
        int ans = solve(str,k);
        if(ans==INF){
            // string outputa =  + t + ": IMPOSSIBLE";
            out<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        }
        else{
            // string output = "Case #" + t + ": " + ans;
            // cout<<output<<endl;
            out<<"Case #"<<t<<": "<<ans<<endl;
        }
    }
    return 0;
}