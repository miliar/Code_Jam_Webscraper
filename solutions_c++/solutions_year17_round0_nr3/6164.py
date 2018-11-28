#include <bits/stdc++.h>
#define FOR(i,f,t) for(int i=f; i<t; i++)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define pb push_back    
#define SYNC ios_base::sync_with_stdio(false)
#define inf 2248012
#define mp make_pair
#define sci(x) scanf("%d",&x)
#define scii(x,y) scanf("%d %d",&x,&y)
#define sciii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define F first
#define S second
#define MAXN 100005
using namespace std;

typedef long long ll;


int main(){
    int t;
    sci(t);
    FOR(i,0,t){
        pair<int,int> ans;
        priority_queue <int> p;
        int n,k;
        scii(n,k);
        p.push(n);
        ll maxi = 0;
        while(k){
            maxi = max(maxi, (ll)p.size());
            int e = p.top(); p.pop();
            if(e%2){
                p.push(e/2);
                p.push(e/2);
                ans = mp(e/2,e/2);
            }else{
                p.push(e/2);
                p.push(e/2-1);
                ans = mp(e/2,e/2-1);    
            }
            k--;
        }
        printf("Case #%d: %d %d\n",i+1,ans.F,ans.S);
    }
}