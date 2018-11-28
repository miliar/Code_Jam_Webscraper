
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
#include <iomanip>
#include <cassert>
#include <functional>

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
const long double PI = 3.141592653589793238;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin
//
#define cout fout

//----------------------------

#ifdef cin fin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif


int a[100], b[100];
int main(){
    ios::sync_with_stdio(0);
    

    int t, z = 1;
    cin >> t;
    cout.precision(17);
    while(t--){

        cout << "Case #" << z++ <<": ";
        int n, k;
        cin >> n >> k;
        for(int i = 0; i < n; i++) cin>>a[i] >> b[i];

        string s;
        for(int i = 0; i < n; i++) s.push_back('0');
        for(int i = 0; i < k; i++) s[n - i - 1] = '1';
        string t = s;
        reverse(t.begin(), t.end());
        double ans = 0;
       do{
            vector<pair<double, double> > v;
            for(int i = 0; i < n; i++){
                if(s[i] == '1'){
                    v.push_back(mk(a[i], b[i]));
                }
            }
            sort(v.begin(), v.end());
            reverse(v.begin(), v.end());
            double cur = 0;
            for(int i = 0; i < k; i++){
                cur += 2 * PI * v[i].first * v[i].second;
            }
            cur += v[0].first * v[0].first * PI;
            ans = max(cur, ans);
           
        }  while ( std::next_permutation(s.begin(), s.end()) );
       


cout << ans<<endl;
    }
  
    return 0;
}