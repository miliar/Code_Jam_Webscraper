#include<bits/stdc++.h>
#define LL int64_t
#define LD long double;
using namespace std;


void f() {
    vector<int> activity(24*60,0);
    int C,J;
    cin>>C>>J;
    for(int i=0;i<C;i++) {
        int a,b;
        cin>>a>>b;
        for(int j=a;j<b;j++) activity[j] = 1;
    }
    for(int i=0;i<J;i++) {
        int a,b;
        cin>>a>>b;
        for(int j=a;j<b;j++) activity[j] = 2;
    }

    LL sol = INT_MAX;
    for(int first=0;first<2;first++) {
        vector<vector<vector<int> > > dyn(12*60+1,vector<vector<int> >(12*60+1, vector<int>(2,0)));
        dyn[0][0][1-first]=INT_MAX;
        for(int i=0;i<12*60+1;i++) {
            for(int j=0;j<12*60+1;j++) {
                if(i==0&&j==0) continue;
                for(int p=0;p<2;p++) {
                    if(activity[i+j-1]!=(p+1)) {
                        LL best = INT_MAX;
                        if(p==0) {
                            best = min( i > 0 ? 0L + dyn[i-1][j][p] : best,
                                        j > 0 ? 1L + dyn[i][j-1][1-p] : best);
                        } else {
                            best = min( i > 0 ? 1L + dyn[i-1][j][1-p] : best,
                                        j > 0 ? 0L + dyn[i][j-1][p] : best);
                        }
                        if(best>INT_MAX) best = INT_MAX;
                        dyn[i][j][p] = best;
                    } else dyn[i][j][p] = INT_MAX;
                }
            }
        }
        sol = min({
                sol,
                0L+dyn[720][720][first],
                1L+dyn[720][720][1-first]
        });


    }

    cout<<sol<<endl;

}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    int T;
    cin>>T;
    for(int i=1;i<=T;i++) {
        cout<<"Case #"<<i<<": ";
        f();
    }
}
