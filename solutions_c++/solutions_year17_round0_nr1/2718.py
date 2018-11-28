#include <bits/stdc++.h>
#define MOD 1000000007
#define MAX 100100
using namespace std;

string str;
int t, k;

bool up[1010];

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    std::ios::sync_with_stdio(false);
    cin.tie(0);

    cin>>t;
    for(int cc = 1; cc <= t; ++cc){
        int cnt = 0;
        cin>>str>>k;
        memset(up, 0, sizeof(up));

        int len = str.size();

        for(int i = 0; i < len; ++i)
            if(str[i] == '+')
                up[i] = true;
            else
                up[i] = false;

        for(int i = 0; i <= len - k; ++i){
            if(up[i] == false){
                for(int j = i; j < i + k; ++j)
                    up[j] = 1 ^ up[j];
                ++cnt;
            }
        }
        bool finished = true;

        for(int i = 0; i < len; ++i)
            if(up[i] == false)
                finished = false;

        if(finished == true){
            cout<<"Case #"<<cc<<": "<<cnt<<endl;
        } else{
            cout<<"Case #"<<cc<<": IMPOSSIBLE"<<endl;
        }

    }

    return 0;
}
