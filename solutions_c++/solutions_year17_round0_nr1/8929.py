#include<bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
#define all(x)      (x).begin(), (x).end()
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define mp make_pair
#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()
#define StartTime          clock_t begin = clock()
#define EndTime            clock_t end = clock()
#define DisplayTime        (double(end - begin) / CLOCKS_PER_SEC)

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
template<class T> T gcd(T a, T b) {
    return b ? gcd(b, a % b) : a;
}
const double EPS = 1e-7;
const ll MOD = 1000000007;
const db PI = acos(-1);

int solve(vi arr, int k) {
  int n = arr.size(), sum=0, ret=0;
  vi ss(n,0);

  fr(i,n) {
    ss[i] = (arr[i]+sum)%2==0;
    if(i>n-k && ss[i]) 
        return -1;
    ret += ss[i];
    sum += ss[i] - (i>=k-1?ss[i-k+1]:0);
  }
  return ret;
}

int main() {
    int t, k;
    string pancakes;

    cin >> t;

    for(int _t=1;_t<=t;_t++){
        cin >> pancakes;
        cin >> k;

        int n = pancakes.size();
        vi arr(n,0);
        
        fr(i,n){
            arr[i] = (pancakes[i] == '+');
        }

        long ans = solve(arr, k);  

        cout << "Case #"<< _t <<": ";
        if(ans==-1){
            cout << "IMPOSSIBLE";
        }else{
            cout << ans;
        }
        cout << endl;
    }
    return 0;
}
