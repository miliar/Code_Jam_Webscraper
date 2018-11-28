
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


int a[5000];
int q = 1440;

int main(){
    ios::sync_with_stdio(0);
    

    int t, z = 1;
    cin >> t;
    while(t--){
        memset(a, 0, sizeof(a));
        cout << "Case #" << z++ <<": ";
        int n, m;
        cin >> n >> m;

        for(int i = 0; i < n; i++){
            int u, v;
            cin >> u >> v;
            for(int j = u; j < v; j++) a[j] = 2;
        }
        for(int i = 0; i < m; i++){
            int u, v;
            cin >> u >> v;
            for(int j = u; j < v; j++) a[j] = 1;
        }
        int u = 0, v = 0;
        for(int i = 0; i < q; i++) {
            if(a[i] == 1) u++;
            else if(a[i] == 2) v++;
        }
        if(u + v == 1){
            cout << 2 << endl;
            continue;
        }
     

        int cur = 1;
        int cnt = 0, h = 0;
        vector<int> b;
        for(int i = 0; i < q; i++){
            if(!h){
                if(a[i] == cur) h = 1;
            } 
            else{
                if(a[i] == 0) cnt++;
                else if(a[i] == cur){
                    if(cnt){
                        b.push_back(cnt);
                        cnt = 0;
                    }
                } 
                else{
                    h = 0;
                }
            }
            
        }
        if(h){
            for(int i = 0; ; i++){
                if(a[i] == 0) cnt++;
                else if(a[i] == cur) {
                    b.push_back(cnt);
                    break;
                }
                else break;
            }
        }


        cur = 2, cnt = 0, h = 0;
        vector<int> c;
        for(int i = 0; i < q; i++){
            if(!h){
                if(a[i] == cur) h = 1;
            } 
            else{
                if(a[i] == 0) cnt++;
                else if(a[i] == cur){
                    if(cnt){
                        c.push_back(cnt);
                        cnt = 0;
                    }
                } 
                else{
                    h = 0;
                }
            }
            
        }
        if(h){
            for(int i = 0; ; i++){
                if(a[i] == 0) cnt++;
                else if(a[i] == cur) {
                    c.push_back(cnt);
                    break;
                }
                else break;
            }
        }

        cur = 1;
        if(c.size() > b.size()){
            cur = 2;
            b.clear();
            for(int i = 0; i < c.size(); i++) b.push_back(c[i]);
        }
        
   
        int ans = 0, k = 0;
        for(int i = 0; i < q; i++){
            if(k == 0) k = a[i];
            else{
                if(a[i] != k && a[i] != 0){
               
                    ans++;
                    k = a[i];
                }
            }
        }
 
        for(int i = 0; ; i++){
            if(a[i] != 0){
                if(a[i] != k) ans++;
                break;
            }
        }
       
        int lft;
        if(cur == 1) lft = 720 - u;
        else lft = 720 - v;


       

        sort(b.begin(), b.end());
        ans += 2 * b.size();
        for(int i = 0; i < b.size(); i++){
            if(lft >= b[i]){
                lft -= b[i];
                ans -= 2;
            } else{
                break;
            }
        }
        cout << ans<<endl;
        
    }
  
    return 0;
}