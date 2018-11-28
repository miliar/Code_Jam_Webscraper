#pragma comment(linker, ”/STACK:38777216“
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <stack>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <time.h>
#include <map>
#include <set>

using namespace std;

const int N = 1005;
const int inf = 1000 * 1000 * 1000;
const int mod = 1000 * 1000 * 1000 + 7;

int n,q,k;
string s;
int a[1005];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>q;
    for(int i=1;i<=q;i++){
        cin>>s>>k;
        int sum = 0 , answ = 0;
        for(int j=0;j<(int)s.size()-k+1;j++){
            if(j >= k)sum -= a[j - k];
            int x = (s[j] == '+') ? 0 : 1;
            a[j] = (x ^ (sum % 2));
            sum += a[j];
            answ += a[j];
        }
        for(int j=(int)s.size() - k + 1;j<(int)s.size();j++){
            if(j >= k)sum -= a[j - k];
            int x = (s[j] == '+') ? 0 : 1;
            int t = (x ^ (sum % 2));
            if(t == 1){
                answ = -1;
                break;
            }
        }
        if(answ == -1)
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<i<<": "<<answ<<endl;
    }
    return 0;
}
