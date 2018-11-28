#include <bits/stdc++.h>
#define max(a,b)   (((a)>(b))?(a):(b))
#define min(a,b)   (((a)>(b))?(b):(a))
#define ulli       unsigned long long int
#define lli        long long int
#define pb         push_back
#define mp         make_pair
#define fi         first
#define se         second
#define all(x)     x.begin(),x.end()
#define rall(x)    x.rbegin(),x.rend()
#define vi         vector<lli>
#define vii        vector<vi>
#define vs         vector<string>
#define pii        pair<lli,lli>
#define pis        pair<lli,string>
#define rep(i,lo,hi) for(lli i=lo;i<hi;i++)
#define MOD        1000000007
#define noof1(x)    __builtin_popcount(x)
#define sievesize  100000000
#define mt         make_tuple
#define eb         emplace_back
#define PI         3.141592653589793238
#define gcd        __gcd
#define digits(n)  (floor(log10(n))+1)
#define mini       INT_MIN
#define maxi       INT_MAX
#define minlli     LONG_LONG_MIN
#define maxlli     LONG_LONG_MAX
#define sz(a)      int((a).size())
#define ios        ios_base::sync_with_stdio(0);cin.tie(NULL)
using namespace std;

int main() {
  freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
   {
    string s;
    int k,cnt=0,des,flag=0;
    cin>>s>>k;
    rep(i,0,s.length())
    {
        if(s[i]=='-')
        {
            if(i+k<=s.length())
            {
                cnt++;
             for(int j=i;j<i+k;j++)
                {
                 if(s[j]=='-')
                        s[j]='+';
                 else
                        s[j]='-';
                }
            }
        }
    }
    rep(h,0,s.length())
    {
        if(s[h]!='+')
        {
            flag=1;
            break;
        }

    }
    if(flag==1)
    cout << "Case #" << i << ": " <<"IMPOSSIBLE"<<endl;
    else
    cout << "Case #" << i << ": " <<cnt<<endl;

  }
  return 0;

}
