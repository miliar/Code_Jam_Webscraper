#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int t;
int main(){
    freopen("large.in", "r" , stdin);
    freopen("smalllol.txt", "w" , stdout);
    cin >> t;
    int start=t;
    while(t--){
        string st;
        cin >> st;
        int n;
        cin >> n;

        int an = 0;
       // cout << st << endl;
        for(int i = 0; i < st.length() - n; i++){
            if(st[i] == '-'){
                an++;
                for(int e = i; e < i + n; e++){
                    if(st[e]=='+') st[e]='-';
                    else st[e]='+';
                }
            }
        }
        for(int i = st.length()-1; i >= n - 1; i--){
            if(st[i] == '-'){
                an++;
                for(int e = i; e > i - n; e--){
                    if(st[e]=='+') st[e]='-';
                    else st[e]='+';
                }
            }
        }
       // cout << st << endl;
        for(int i = 0; i < st.length(); i++){
            if(st[i]=='-') an=-1;
        }
        cout << "Case #"  << (start-t) << ": ";
        if(an == -1) cout << "IMPOSSIBLE" << endl;
        else cout << an << endl;
    }

    return 0;
}
