/*  ^^ ====== ^^
ID: meixiuxiu
PROG: test
LANG: C++11
*/
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int ,int> pii;
#define MEM(a,b) memset(a,b,sizeof a)
#define CLR(a) memset(a,0,sizeof a);
#define pi acos(-1.0)
#define maxn 40000
#define maxv 100005
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
ll type[2][2];
int main(){
    freopen("C:\\Users\\meixinyu\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\meixinyu\\Desktop\\out.txt","w",stdout);
    int t;cin >>t;
    int kase = 1;
    while(t--){
        printf("Case #%d: ",kase++);
        MEM(type,0);
        ll n;cin >> n;
        ll k;cin >> k;
        type[0][0] = n;
        type[0][1] = 1;
        ll tot = 0;
        //cout<< n <<' '<< k << endl;
        while(tot < k){
            tot += type[0][1] + type[1][1];
           /* cout << tot << endl;
            cout << type[0][0] << ' ' << type[0][1] << endl;
            cout << type[1][0] << ' ' << type[1][1] << endl;*/
            if(tot >= k){
                ll whomax = -1;
                if(type[0][1] && type[1][1]){
                    whomax = type[0][0]>type[1][0] ? 0:1;
                }
              //  cout << whomax << endl;
                if(whomax != -1){
                    if(type[whomax][1]+tot-(type[0][1]+type[1][1]) < k)cout << (type[1-whomax][0])/2 <<' '<< (type[1-whomax][0]-1)/2  << endl;
                    else cout << (type[whomax][0])/2 <<' '<< (type[whomax][0]-1)/2  << endl;
                }   
                else{
                    if(type[0][1]){
                        whomax = 0;
                        cout << (type[whomax][0])/2 <<' '<< (type[whomax][0]-1)/2  << endl;
                    }
                    else{
                        whomax = 1;
                        cout << (type[whomax][0])/2 <<' '<< (type[whomax][0]-1)/2  << endl;
                    }
                }
                break;
            }
            else{
                ll one = (type[0][0]-1)/2;
                ll tmp0 = (type[0][0]-1)/2;
                ll tmp1 = (type[0][0])/2;
                ll tmp3 = type[0][1];
                ll tmp00 = (type[1][0]-1)/2;
                ll tmp11 = (type[1][0])/2;
                ll tmp33 = type[1][1];
                MEM(type,0);
                if(tmp3){
                   // cout << tmp0 << tmp1 << endl;
                    if(tmp0){
                        if(tmp0 == one)type[0][0] = one,type[0][1] += tmp3;
                        else type[1][0] = tmp0,type[1][1] += tmp3;
                    }
                    if(tmp1){
                        if(tmp1 == one)type[0][0] = one,type[0][1] += tmp3;
                        else type[1][0] = tmp1,type[1][1] += tmp3;
                    }
                }
                
                if(tmp33){
                    if(tmp00){
                        if(tmp00 == one)type[0][0] = one,type[0][1] += tmp33;
                        else type[1][0] = tmp00,type[1][1] += tmp33;
                    }
                    if(tmp11){
                        if(tmp11 == one)type[0][0] = one,type[0][1] += tmp33;
                        else type[1][0] = tmp11,type[1][1] += tmp33;
                    }
                }
            }
        }
    }
}