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

//#define cin in
//#define cout out

using namespace std;

const int INF = (int)1e9;
typedef int64_t ll;


int main()
{
//    ifstream in;
//    in.open("/home/vlad/QtProjects/ICM/ICMtrain/input.in");
//    ofstream out;
//    out.open("/home/vlad/QtProjects/ICM/ICMtrain/output.txt");
    int n_t;
    cin >> n_t;
    vector<string> ans(n_t);
    for(int test = 0; test < n_t; ++test){
        string s;
        cin >> s;
        int ind = 1;
        for(; ind < s.length() && s[ind - 1] <= s[ind]; ++ind)
            ;
        if(ind != s.length()){
            --ind;
            while(ind > 0 && s[ind - 1] == s[ind])
                --ind;
            s[ind]--;
            ++ind;
            for(;ind < s.length(); ++ind)
                s[ind] = '9';
            if(s[0] == '0')
                s.erase(s.begin());
        }
        ans[test] = s;
    }
    for(int i = 0; i < n_t; ++i){
        cout << "Case #" << i + 1 << ": ";
        cout << ans[i];
        cout << endl;
    }

}




