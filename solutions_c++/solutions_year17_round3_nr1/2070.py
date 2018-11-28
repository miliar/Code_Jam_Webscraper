#include <bits/stdc++.h>
using namespace std;
const double pi=acos(-1);

bool cmp(pair<int,int> a,pair<int,int> b) {
    if (a.first<=b.first)
        return 1;
    else
        return 0;
}

int main () {
    int T,N,K,a,b;
    scanf("%d", &T);
    for (int t=1;t<=T;t++) {
        scanf("%d %d", &N, &K);
        vector<pair<int,int> > pc;
        pc.clear();
        for (int i=0;i<N;i++) {
            scanf("%d %d", &a, &b);
            pc.push_back(make_pair(a,b));
        }
        sort(pc.begin(),pc.end(),cmp);
        
        //debug
        /*for (int i=0;i<N;i++) {
         cout<<pc[i].first<<"   "<<pc[i].second<<endl;
         }
         /*for (int i=0;i<N;i++) {
         for (int j=0;j<N;j++) {
         if (pc[i].first>pc[j].first)
         swap(pc[i],pc[j]);
         }
         }*/
        vector<int> side;
        for (int i=0;i<N;i++)
            side.push_back((2*pc[i].first*pc[i].second));
        int ans=0;
        int sidesum=0;
        vector<int> sidepi=side;
        //cout<<N<<"   "<<K<<endl;
        for (int i=K-1;i<N;i++) {
            sidesum=side[i];
            sidepi=side;
            for (int j=0;j<K-1;j++) {
                int mx=0;
                int pos=0;
                for (int k=0;k<i;k++) {
                    if (mx<=sidepi[k]) {
                        mx=sidepi[k];
                        pos=k;
                    }
                }
                //cout<<pos<<endl;
                sidesum+=mx;
                sidepi[pos]=-1;
            }
            
            sidesum+=pow(pc[i].first,2);
            if (sidesum>=ans)
                ans=sidesum;
            //cout<<endl<<endl<<endl;
        }
        printf("Case #%d: %.9f\n", t, (double)ans*pi);
        //cout<<pi<<endl;
    }
    return 0;
}
