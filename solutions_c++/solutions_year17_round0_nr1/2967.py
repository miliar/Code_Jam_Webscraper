#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <cmath>
#include <vector>
#include <stack>
#include <bitset>

#define cin in
#define cout out

using namespace std;

const int INF = (int)1e9;
typedef int64_t ll;


int main()
{
    ifstream in;
    in.open("/home/vlad/QtProjects/ICM/ICMtrain/A-large.in");
    ofstream out;
    out.open("/home/vlad/QtProjects/ICM/ICMtrain/output.txt");
    int n_t;
    cin >> n_t;
    vector<int> ans(n_t);
    vector<int> sw;
    vector<bool> cookies;
    for(int test = 0; test < n_t; ++test){
        string s;
        cin >> s;
        vector<int> cookies(s.length());
        for(int i = 0; i < (int)s.size(); ++i){
            if(s[i] == '+')
                cookies[i] = true;
            else cookies[i] = false;
        }
        vector<int> sw(cookies.size());
        int k;
        cin >> k;
        int c_swap = 0;
        int res = 0;
        for(int i = 0; i <= cookies.size() - k; ++i){
            if(((cookies[i] + c_swap) % 2) == 0){
                c_swap++;
                sw[i + k - 1] += -1;
                cookies[i] = true;
                res++;
            }
            c_swap += sw[i];
        }
        bool pos = true;
        for(int i = cookies.size() - k + 1;i >= 0 && i < cookies.size(); ++i){
            pos &= (cookies[i] + c_swap) % 2;
            c_swap += sw[i];
        }
        if(pos)
            ans[test] = res;
        else
            ans[test] = -1;

    }
    for(int i = 0; i < n_t; ++i){
        cout << "Case #" << i + 1 << ": ";
        if(ans[i] == -1)
            cout << "IMPOSSIBLE";
        else cout << ans[i];
        cout << endl;
    }

}




