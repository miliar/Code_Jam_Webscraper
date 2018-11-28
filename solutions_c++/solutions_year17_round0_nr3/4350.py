#include<bits/stdc++.h>

using namespace std;

multiset<pair<int,int> >s;
multiset<pair<int,int> >:: iterator it;

int main(){

    freopen("gcj_in.txt","r",stdin);
    freopen("gcj_out.txt","w",stdout);

    int t;
    cin >> t;
    for(int it1=1;it1<=t;it1++) {
        s.clear();
        int n,i,k,x,y,z,ans1,ans2,mid;
        scanf("%d%d",&n,&k);
        s.insert(make_pair(n,-2));
        while(k--) {
            it = s.end();
            it--;
            x = it->first; y = it->second; z = -y;
            s.erase(it);
            if(x % 2 == 0) {
                mid = (z + z + x - 1) / 2;
                ans1 = x / 2; ans2 = ans1 - 1;
                if(ans1 > 0)
                s.insert(make_pair(ans1,y));
                if(ans2 > 0)
                s.insert(make_pair(ans2,-(mid + 1)));
            }
            else {
                mid = (z + z + x - 1) / 2;
                ans1 = x / 2; ans2 = ans1;
                if(ans1 > 0)
                s.insert(make_pair(ans1,y));
                if(ans2 > 0)
                s.insert(make_pair(ans2,-(mid + 1)));
            }
        }
        cout << "Case #" << it1 << ": " << ans1 << " " << ans2 << "\n";
    }
    return 0;

}
