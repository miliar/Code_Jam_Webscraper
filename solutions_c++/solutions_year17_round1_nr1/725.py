#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef long long int LL;
typedef pair<int,int> pi;
typedef unsigned long long int ull;

string s[30];
int TC,R,C,k;

int main(){
    std::ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> TC;
    for (int outi=0;outi<TC;outi++){
        cout << "Case #" << outi+1 << ": \n";
        cin >> R >> C;
        for (int i=0;i<R;i++){
            cin >> s[i];
        }
        for (int i=0;i<R;i++){
            for (int j=0;j<C;j++){
                if (s[i][j] != '?'){
                    k = j-1;
                    while (k>=0 && s[i][k] == '?') {s[i][k] = s[i][j];k--;}
                    k = j+1;
                    while (k<C && s[i][k] == '?') {s[i][k] = s[i][j];k++;}
                }
            }
        }
        for (int i = 0;i<R;i++){
            if (s[i][0] == '?'){
                k = i;
                while (k>=0 && s[k][0] == '?') k--;
                if (k==-1){
                    k = 0;
                    while (s[k][0] == '?') k++;
                }
                s[i] = s[k];
            }
        }
        for (int i=0;i<R;i++){
            cout << s[i] << "\n";
        }
    }
}
