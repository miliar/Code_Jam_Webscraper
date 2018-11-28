#include<cstdio>
#include<iostream>
#include<sstream>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<string>
#include<cstring>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<ctime>
#include<vector>
#include<fstream>
#include<list>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define ms(s) memset(s,0,sizeof(s))

const double PI = 3.141592653589;
const int INF = 0x3fffffff;

string num;

void judge(int idx) {
    if(num[idx-1] > num[idx] && idx != 0) {
        num[idx-1]--;
        judge(idx-1);
        for(int i = idx; i < num.size(); i++) {
            num[i] = '9';
        }
    }
}

int main() {
//        freopen("/Users/really/Documents/code/B-large.in","r",stdin);
//        freopen("/Users/really/Documents/code/output","w",stdout);
    ios::sync_with_stdio(false);
    
    int t;
    cin >> t;
    for(int cas = 1; cas <= t; cas++) {
        bool flag = false;
        cin >> num;
        for(int i = 1; i < num.size(); i++) {
            judge(i);
        }
        //输出没有前导0的值。
        int now = 0;
        while(num[now] == '0')
            now++;
        
        cout << "Case #" << cas << ": ";
        
        while(now < num.size())
            cout << num[now++];
        cout << endl;
        
    }
    
    return 0;
}
