//#pragma comment(linker, "/STACK:500000000")
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <stdlib.h>
#include <ctime>
#include <queue>
#include <set>
#include <iostream>
#include <stack>
#include <list>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
//#include <WinDef.h>
//#include <iterator> map<string,int>::iterator i;
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<ll> vc;
typedef unsigned int ui;
#define mp make_pair
#define forn(i,n)	for(ll i = 0; i < n; i++)
#define forn2(i,n)	for(ll i = 1; i <= n; i++)
#define forn3(i,n,s) for(ll i = s; i <= n; i++)
#define forn4(i,n)	for(ll i = n; i >= 1; i--)
#define forn5(i,n)	for(ll i = n - 1; i >= 0; i--)
#define bad {cout<<"-1"<<endl;return 0;}
//#define push(x,g) {cin>>x;g.push_back(x);}
int F(const void* l, const void* r) {
  return (*(int*)l - *(int*)r);
}
const ll INF = 1000000000000000003;
const ll MAXN = 50000;
const ll dd = 1000000007;

const int INF2 = 1000000000;
vector<int> best;
vector<int> fun(long long x) {
  vector<int> ans;
  while (x) {
    ans.push_back(x % 10);
    x /= 10;
  }
  reverse(ans.begin(), ans.end());
  return ans;
}

int main()
{
  //FILE **fp = new FILE*;              99999999999999999
  //freopen_s(fp,"in.txt", "rx", stdin);99999999999999999
  //freopen_s(fp,"output.txt", "w", stdout);
  ifstream cin("inx2.in");
  ofstream cout("out.txt");
  int t;
  cin >> t;
  int h = 1;
  while (h <= t) {
    long long x;
    cin >> x;
    vector<int> num = fun(x);
    for (int i = 1; i < num.size(); i++) {
      if (num[i] < num[i - 1]) {
        i--;
        while (i >= 0 && num[i] > num[i + 1]) {
          num[i]--;
          i--;
        }
        for (int j = i + 2; j < num.size(); j++) {
          num[j] = 9;
        }
        break;
      }
    }
    long long ans = 0;
    for (int i : num) {
      ans *= 10;
      ans += i;
    }
    cout << "Case #" << h << ": " << ans << endl;
    h++;
  }
  return 0;
}