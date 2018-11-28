//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;

#define MAXN 1005
#define ii pair<int,int>
#define iii pair<ii,int>
#define ff first
#define ss second
#define ll long long

vector<int> v(MAXN);
int n;

bool cmp(iii a, iii b){
    if(a.ff.ff!=b.ff.ff) return a.ff.ff>b.ff.ff;
    else if(a.ff.ss!=b.ff.ss) return a.ff.ss>b.ff.ss;
    else return a.ss<b.ss;
}

void occupy(bool flag = false){
    int i,j,curr,maxi=-1;
    vector<int> left_fill(MAXN,0);
    vector<int> right_fill(MAXN,0);
    curr = 0;
    for(i=1;i<=n;i++){
        if(v[i]==1) curr = i;
        else left_fill[i] = curr;
    }   
    curr = n+1;
    for(i=n;i>=0;i--){
        if(v[i]==1) curr = i;
        else right_fill[i] = curr;
    }

    vector<iii> temp;
    for(i=1;i<=n;i++)
        if(v[i]==0)
            temp.push_back(iii(ii(min(i-left_fill[i],right_fill[i]-i),max(i-left_fill[i],right_fill[i]-i)),i));
    
    sort(temp.begin(), temp.end(),cmp);    
    if(flag) printf("%d %d\n",temp[0].ff.ss-1,temp[0].ff.ff-1);
    v[temp[0].ss] = 1;
}

void printv(){
    for (int i = 0; i <= n+1; ++i)
        printf("%d",v[i]);
    printf("\n");
}

int main(){
    freopen ("C-small-1-attempt0.in","r",stdin); 
    freopen ("C-small-1-attempt0.out","w",stdout);
    int i,j,t,k;
    scanf("%d",&t);
    for (int tester = 1; tester <= t; ++tester){
        scanf("%d %d",&n,&k);
        for(i=0;i<n+2;i++) v[i] = 0;
        v[0] = 1;
        v[n+1] = 1;
        k--;
        while(k--)
            occupy();
        printf("Case #%d: ",tester);
        occupy(true);
    } 

    return 0;
}