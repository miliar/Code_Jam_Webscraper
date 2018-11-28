#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef long long int LL;
typedef pair<int,int> pi;
typedef unsigned long long int ull;
#define mp make_pair

int TC,N,P,a;

int main(){
    std::ios::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> TC;
    for (int outi=0;outi<TC;outi++){
        cout << "Case #" << outi+1 << ": ";
        cin >> N >> P;
        int ans = 0;
        int no[5];
        for (int i=0;i<4;i++) no[i] = 0;
        for (int i=0;i<N;i++){
            cin >> a;
            a = a % P;
            no[a]++;
        }
        ans += no[0];
        if (P == 2){
            ans += (no[1]+1)/2;
        }
        else if (P == 3){
            int m = min(no[1],no[2]);
            ans += m;
            ans += ((no[1]+no[2]-m*2)+2)/3;
        }
        else if (P == 4){
            ans += no[2]/2;
            int m = min(no[1],no[3]);
            ans += m;
            no[1] -= m; no[3] -= m;
            m = max(no[1],no[3]);
            if (m>2 && no[2] % 2 == 1) {ans++;m-=2;no[2]=0;}
            ans+= (m + no[2] % 2 + 3)/4;
        }
        cout << ans << "\n";
    }
}
