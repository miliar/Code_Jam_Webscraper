#include <bits/stdc++.h>
using namespace std;
#define INF 1ULL<<30
#define MAXN 1000000000000
#define pb push_back
#define mp make_pair
#define forn(r,a,b) for(int r = a; r<b; r++)
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
#define fst first
#define snd second

typedef long long int lli;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef pair<ii,string> iis;
typedef vector<iii> viii;
typedef vector<int> vi;
priority_queue<iii> pq;
int main(){
    int tc;
    cin >> tc;
    int n,k;
    iii u;
    for(int t = 1; t<=tc; t++){
       cin >> n >> k;
       u.snd.fst = -1;
       u.snd.snd = (n + 1);
       u.fst = (u.snd.snd - (-u.snd.fst));
       pq.push(u);
       iii v;
       int mid;
       iii last1;
       iii last2;
       for( int i = 1; i<= k; i++){
        u = pq.top(),pq.pop();
        mid = (u.snd.snd + (-u.snd.fst) - 1 )  /2;
        v.snd.snd = mid;
        v.snd.fst = u.snd.fst;
        v.fst = ( v.snd.snd - (-v.snd.fst));
        last1 = v;
        pq.push(v);
        v.snd.fst = -(mid +1);
        v.snd.snd = u.snd.snd;
        v.fst = (v.snd.snd - (-v.snd.fst));
        pq.push(v);
        last2 = v;

       }
       int value_1 = last1.snd.snd - (-last1.snd.fst);
       pq.pop();
       int value_2 = last2.snd.snd - (-last2.snd.fst);
       ///printf("Ultima mid = %d %d %d %d %d\n",mid , last1.snd.snd,-last1.snd.fst,last2.snd.snd,-last2.snd.fst);
       printf("Case #%d: %d %d\n",t,max(value_1,value_2),min(value_1,value_2));
       while(!pq.empty()) pq.pop();
    }
    return 0;
    
}