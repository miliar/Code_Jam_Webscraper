#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<stdio.h>
#include<cmath>
#include<set>
#include<map>

using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T,k,n;

    cin>>T;
    for(int t=1; t<=T; t++) {
        cin>>n>>k;

        set<pair<int,pair<int,int> > > a;

        a.insert( make_pair( -(n+1), make_pair(0, n+1) ) );
        int l, r;
        while(k--) {
            set<pair<int,pair<int,int> > >::iterator it = a.begin();
            int sz = -(*it).first;
            int x = (*it).second.first;
            int y = (*it).second.second;
            a.erase(it);
            int xx;
            if(sz%2==0) {
                xx = x + (sz/2);
                l = (sz/2);
                r = (sz/2);
            }else {
                xx = x + (sz/2);
                l = (sz/2);
                r = (sz/2)+1;
            }
            if(xx-x > 1)
            a.insert(make_pair( - (xx-x), make_pair(x,xx)));
            if(y-xx > 1)
            a.insert(make_pair( - (y-xx), make_pair(xx,y)));
        }
        cout<<"Case #"<<t<<": ";
        cout<<r-1<<" "<<l-1<<endl;
    }
}
