#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
struct node{int l, r, color;};

bool cmp(node a, node b){return a.l < b.l;}

const int N=10000;
int tot,nc,nj,n,sc,sj,ans;
node tnode[N];
vector<node> ca, ja;
vector<int> tc, tj;

void solve(int test){
    tc.clear(); tj.clear();
    scanf("%d%d",&nc,&nj);
    sc=sj=ans=0;
    n=nc+nj;
    for (int i=1;i<=nc;i++){
        scanf("%d%d",&tnode[i].l,&tnode[i].r);
        tnode[i].color=0;
        sc+=tnode[i].r-tnode[i].l;
        ca.push_back(tnode[i]);
    }
    for (int i=1;i<=nj;i++){
        scanf("%d%d",&tnode[i+nc].l,&tnode[i+nc].r);
        sj+=tnode[i+nc].r-tnode[i+nc].l;
        tnode[i+nc].color=1;
        ja.push_back(tnode[i+nc]);
    }
    sort(tnode+1,tnode+1+n,cmp);
    for (int i=1;i<n;i++)
        if (tnode[i].color!=tnode[i+1].color) ans++;
            else{
                if (tnode[i].color==0)
                    tc.push_back(tnode[i+1].l-tnode[i].r);
                else
                    tj.push_back(tnode[i+1].l-tnode[i].r);
            }

    if (tnode[1].color!=tnode[n].color) ans++;
        else{
            if (tnode[n].color==0)
                tc.push_back(24*60-tnode[n].r+tnode[1].l);
            else
                tj.push_back(24*60-tnode[n].r+tnode[1].l);
        }
    sort(tc.begin(),tc.end());
    sort(tj.begin(),tj.end());

    for (int i=0;i<tc.size();i++)
        if (sc+tc[i]<=720) sc+=tc[i]; else {ans+=(tc.size()-i)*2; break;}

    for (int i=0;i<tj.size();i++)
        if (sj+tj[i]<=720) sj+=tj[i]; else {ans+=(tj.size()-i)*2; break;}
    printf("Case #%d: %d\n",test,ans);
}

int main(){
    scanf("%d",&tot);
    for (int i=1;i<=tot;++i) solve(i);
}
