#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

#define N 1010
pii uma[N];
bool ou[N];

double jikan(int i){
    return (double)(uma[i+1].first-uma[i].first)/(uma[i].second-uma[i+1].second);
}

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        int d, n;
        scanf("%d%d", &d, &n);
        for(int i=1; i<=n; i++){
            scanf("%d%d", &uma[i].first, &uma[i].second);
        }
        uma[n+1] = make_pair(d, 0);
        sort(uma+1, uma+n+2);
        memset(ou, false, sizeof(ou));
        vector<int> loli;
        for(int i=1; i<=n; i++){
            if(uma[i].second > uma[i+1].second){
                loli.push_back(i);
                ou[i] = true;
            }
        }
        double t;
        while(!loli.empty()){
            int i0 = 0;
            for(int i=1; i<(int)loli.size(); i++){
                if(jikan(loli[i0]) > jikan(loli[i])){
                    i0 = i;
                }
            }
            int i = loli[i0];
            loli.erase(loli.begin()+i0, loli.begin()+i0+1);
            t = jikan(i);
            uma[i] = uma[i+1];
            if(i>=1 && !ou[i-1] && uma[i].second<uma[i-1].second){
                loli.push_back(i-1);
            }
        }
        printf("Case #%d: %f\n", kase, (double)d/t);
    }
    return 0;
}
