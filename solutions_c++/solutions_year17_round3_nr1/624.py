#include<bits/stdc++.h>

#define ull unsigned long long int
#define lli long long int
#define li long int
#define mp make_pair
#define pb push_back
#define ft first
#define sc second

#define Tr(S) printf(S);

#define PI acos(-1.0)

using namespace std;
const int MAX = 1e5+5;

struct abc{
    lli R, H;
} A[MAX];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T,N,K,i;
    cin>>T;
    for(int z=1;z<=T;z++){

        double res;
        lli ans=-1;
        cin>>N>>K;
        for(int i=0;i<N;i++){
            cin>>A[i].R>>A[i].H;
        }
        for(int i=0;i<N;i++){
            vector<pair<lli,lli> > tmp;
            lli maxR = A[i].R;
            lli tmpAns= 2*A[i].R*A[i].H, cnt = K-1;

            for(int j=0;j<N;j++){
                if(j!=i)
                    tmp.pb(mp(2* A[j].R * A[j].H, A[j].R));
            }
            sort(tmp.begin(),tmp.end());
            for(int j=tmp.size()-1; j>=0 && cnt>0; j--){
                cnt-=1;
                tmpAns += tmp[j].ft;
                if(tmp[j].sc>maxR)
                    maxR = tmp[j].sc;
            }
            tmp.clear();
            tmpAns += (maxR*maxR);
            if(tmpAns>ans)
                ans = tmpAns;
        }

        //cout << ans << "---ans\n";
        res = (double)ans * 1.0000000000;
        res *= PI;
        cout << "Case #" << z << ": ";
        cout << std::fixed;
        cout << std::setprecision(7) << res << '\n';

        //cout << res << "\n";
    }

    return 0;
}
