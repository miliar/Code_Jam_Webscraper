#include <stdlib.h>
#include "stdio.h"
#include "vector"
#include "set"
#include "algorithm"
#include "math.h"

using namespace std;

bool compare(vector<long> a,vector<long> b)
{
    return a[0]<b[0];
}

int main() {
    freopen("A-large.in.txt", "r", stdin);
    freopen("A-large.out.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for (int tt=1;tt<=t;tt++){
        int n,k;
        scanf("%d%d",&n,&k);
        vector<vector<long>> a(n,vector<long>(2,0));
        vector<long long> area(n,0),max(n,0);
        set<long long> cur;
        long long currenttotal=0,ans=0;
        cur.clear();
        for (int i=0;i<n;i++){
            scanf("%ld%ld",&a[i][0],&a[i][1]);
        }
        sort(a.begin(), a.end(), compare);
        for (int i=0;i<k-1;i++){

            long long tmp = a[i][0];
            tmp*=a[i][1];
            cur.insert(tmp);
            currenttotal+=tmp;
        }
        for (int i=k-1;i<n;i++){

            long long tmp = a[i][0];
            tmp *= a[i][1];
            max[i]=currenttotal+tmp;
            if ((cur.begin()!=cur.end())&&(tmp>*cur.begin())){
                currenttotal-=*cur.begin();
                cur.erase(cur.begin());
                cur.insert(tmp);
                currenttotal+=tmp;
            }
            long long tans=max[i]*2+a[i][0]*a[i][0];
            if (tans>ans)
                ans=tans;
        }
        double fans=ans;
        fans*=M_PI;
        printf("Case #%d: %0.9lf\n",tt,fans);
    }
    return 0;
}
