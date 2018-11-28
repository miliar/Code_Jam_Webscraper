#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}

string get_digs(ll N){
    string res;
    while(N > 0){
        res.push_back((N % 10) + '0');
        N /= 10;
    }
    if(res.size() == 0) res = "0";
    reverse(res.begin(), res.end());
    return res;
}

string dp[21][2];
bool mem[21][2];
string imp = "imp";

string dfs(int pos, bool eql, const string &digs){
    if(mem[pos][eql]){
        return dp[pos][eql];
    }
    else if((int)digs.size() == pos){
        return "";
    }
    string res = imp;
    if(!eql){
        res = "9" + dfs(pos + 1, eql, digs);
    }
    else{
        if(pos == 0 || digs[pos-1] <= digs[pos]){
            string tmp = dfs(pos + 1, true, digs);
            // if(pos == 0){
            //     cout << tmp << endl;
            //     cout << digs[pos] << endl;
            //     cout << digs << endl;
            // }
            if(tmp == imp){
                if(pos == 0 || digs[pos-1] <= digs[pos] - 1){
                    char d = digs[pos] - 1;
                    if(pos != 0 || d != '0'){
                        res = d;
                    }
                    else{
                        res= "";
                    }
                    res += dfs(pos + 1, false, digs);
                }
            }
            else{
                res = digs[pos] + tmp;
            }
        }
        else{
        }
    }
    // もし割り当て不可能な場合、impossible
    mem[pos][eql] = true;    
    return dp[pos][eql] = res;
}

int main(){
    fastStream();
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        ll N;
        cin >> N;
        string digs = get_digs(N);

        ll res = 0;
        {
            // 暫定の最大値を計算
            for(int i = 0; i < (int)digs.size() - 1; i++){
                res = res * 10 + 9;
            }
        }
        memset(mem, 0, sizeof(mem));
        string tmp = dfs(0, 1, digs);
        if(tmp != imp){
            // cout << tmp << endl;
            res = stol(tmp);
        }
        cout << res << endl;
    }
  
    return 0;
}
