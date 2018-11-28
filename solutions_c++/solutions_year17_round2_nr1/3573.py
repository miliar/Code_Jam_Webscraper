#include <bits/stdc++.h>
using namespace std;

#define MAXN 1005
int K[MAXN],S[MAXN],N,D;
int tc;
vector <pair<int,int> > vp;
long double nt[MAXN];

void clearmem(){
    memset(K,0,sizeof K);
    memset(S,0,sizeof S);
    N = D = 0;
    vp.clear();
}

void solve(){
    scanf ("%d%d",&D,&N);
    for (int i=1;i<=N;i++){
        scanf ("%d%d",&K[i],&S[i]);
        vp.push_back(make_pair(K[i],S[i]));
    }
    sort(vp.begin(),vp.end());

    for (int i=N-1;i>=0;i--){
        nt[i] = (long double) (D - vp[i].first )/ (long double)(vp[i].second);
        if (i!=N-1) nt[i] = max(nt[i],nt[i+1]);
        //printf ("%LF ",nt[i]);
    }
    printf ("%LF\n",(long double) D/nt[0]);
}

int main(){
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int TC;
    scanf ("%d",&TC);
    for (tc=1;tc<=TC;tc++){
        printf ("Case #%d: ",tc);
        clearmem();
        solve();
    }

    return 0;
}
