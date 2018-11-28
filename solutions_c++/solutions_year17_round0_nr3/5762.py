#include <bits/stdc++.h>

#define lp(i,n) for(long long int i=0; i<n; i++)

#define ll long long
#define pb push_back
#define  mp make_pair
#define pii pair<int,int>
#define ff first
#define ss second
#define nl "\n"

#define EPS 1e-8
#define OO 10000000

#define on(i,n) i=i|(1<<n)
#define off(i,n) i=i& (~(1<<n))

using namespace std;

bool check(pair<int,int>y, pair<int,int>x){
    if(x.ss-x.ff>y.second-y.ff){
        return true;
    }
    if(x.ss-x.ff<y.second-y.ff){
        return false;
    }
    if(x.ff<y.ff) return true;

    return false;


}

pii solve(int l,int r, int target){

   priority_queue<pii,vector<pii>,function<bool(pii,pii)>> q(check);
    q.push({l,r});
    int k=0;

    while(k!=target){
        auto tt=q.top();

        l=tt.first;
        r=tt.second;

        q.pop();if(l>r) continue;
        if(l==r){
            k++;
            continue;
        }
        int middle=(l+r)/2;

        q.push({middle+1,r});
        q.push({l,middle-1});
        k++;





    }
    return {l,r};











}



int main(){
    freopen("C-small-2-attempt2.in","r",stdin);
   freopen("out.out","w",stdout);
   int cs=1;
   int t=0;

  scanf("%d",&t);
   while(t--){
   int n,k;
    scanf("%d%d",&n,&k);

   auto p=solve(1,n,k);

    int pos=(p.first+p.second)/2;
    printf("Case #%d: ",cs++);

   printf("%d %d\n",max(pos-p.first,p.second-pos),min(pos-p.first,p.second-pos));


   }

}
