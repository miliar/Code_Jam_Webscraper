#include <bits/stdc++.h>

using namespace std;
string arr;
int n, k;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int t = 1;
    cin >> T;
    while(T--){
        cout << "Case #"<<t<<": ";

        cin >> arr >> k;
        if(arr.size() < k){
            cout << "IMPOSSIBLE";
        }else{
            int ans = 0;
            for(int i = 0 ; i < arr.size()-k+1 ; i++){
                if(arr[i] == '+')continue;
                for(int j = 0 ; j < k ; j ++){
                    arr[j+i] = arr[j+i]=='+'?'-':'+';
                }
                ans++;
            }
            for(int i = arr.size()-k ; i < arr.size() ;i++){
                if(arr[i] == '-'){
                    ans = -1;
                    break;
                }
            }
            if(ans == -1)cout << "IMPOSSIBLE";
            else cout << ans;
        }

        cout << endl;
        t++;
    }
    return 0;
}
