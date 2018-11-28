#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int x, y, z, m, n, t, cs = 1;
string str;

int main()
{

    freopen("inputover.txt", "r", stdin);
    freopen("outputover.txt", "w", stdout);

    cin >> t;

    while(t--){

        cin >> str >> m;
        int ans = 0;

        for(int i = 0; i < str.size(); i++){
//            cout << i << ' ' << str[i] << endl;
            if(str[i] == '+') continue;

            if(i + m > (int)str.size()) break;

            ans++;

            for(int j = i, k = 0; k < m; k++, j++){
                if(str[j] == '+') str[j] = '-';
                else str[j] = '+';
            }

        }
        bool flg = true;

        for(int i = 0; i < str.size(); i++) if(str[i] == '-'){
            flg = false;
        }

        if(flg){
            printf("Case #%d: %d\n", cs++, ans);
        }
        else{
            printf("Case #%d: IMPOSSIBLE\n", cs++);
        }

    }

    return 0;
}
