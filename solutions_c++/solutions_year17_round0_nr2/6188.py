
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <cstdlib>
#include <iterator>
#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <math.h>
#include <ctime>
#include <cstring>


using namespace std;


typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
 
#define INF                         (int)1e9
#define EPS                         1e-9
int mod = 1000000007;
 
long long pwr(long long a,long long b,long long mod)
{
  if(b==0)
    return 1;
  long long temp=pwr(a,b/2,mod);
  temp=(temp*temp)%mod;
  if(b&1)
    temp=(temp*a)%mod;
  return temp;
}
long long pwr(long long a,long long b)
{
  if(b==0)
    return 1;
  long long temp=pwr(a,b/2);
  temp=(temp*temp);
  if(b&1)
    temp=(temp*a);
  return temp;
}
bool* isPrime;
void generatePrimeSieve(const int lim)
{
  isPrime=(bool *)malloc(lim+1);
  memset(isPrime,true,lim+1);
  isPrime[0]=false;
  isPrime[1]=false;
  for(int i=2;i<=lim;++i)
    if(isPrime[i])
      for(int j=i+i;j<=lim;j+=i)
        isPrime[j]=false;
}

long long modularInverse(long long a,long long m)
{
      return pwr(a,m-2,m);
}
long long q,n;
string str,s;


string makeNines(int len) {
    string temp;
    if(len <= 0)
        return "";
    for (int i = 0; i < len; ++i)
        temp += '9';
    return temp;
}

long long num(string s) {
    std::stringstream sstr(s);
    long long val;
    sstr >> val;
    return val;
}

bool isValid(string s) {
    int flg = 1;
    for (int i = 0; i < s.length()-1; ++i)
        if(s[i] > s[i+1])
            flg = 0;
    return flg;
}

int main()
{
    ios::sync_with_stdio(false);
    // freopen("input.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);

    cin>>q;
    int t = 0;
    while(q--) {
        t++;
        long long ans = 0;
        cin>>s;
        n = num(s);
        if(isValid(s)) {
            cout<<"Case #"<<t<<": "<<n<<"\n";
            continue;
        }

        for (int i = 0; i < s.length(); ++i)
        {
            if(s[i] != '0') {
                string temp = s.substr(0,i);
                temp += s[i] - 1;
                temp += makeNines(s.length() - i - 1);
                // cout<<temp<<endl;
                long long val = num(temp);
                if(val <= n && isValid(temp))
                    ans = max(ans, val);
            }   
        }
        cout<<"Case #"<<t<<": "<<ans<<"\n";
    }

}



