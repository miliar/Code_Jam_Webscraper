#include<bits/stdc++.h>
#define P(x,y) make_pair(x,y)
using namespace std;
int T , Tn;
long long N;
int main(){
  //  freopen("in.in","r",stdin);
    //freopen("codejam.out","w",stdout);
    cin>>T;
    while(T--){
        cin>>N;
        //v.clear();
        vector < int > v;
        while(N > 0){
            v.push_back(N%10);
            N/=10;
        }
        reverse(v.begin() , v.end());
        bool ok = 1;
        int last = 0;
        printf("Case #%d: ",++Tn);
        for(int j = 1 ; j < v.size() ; j++)
            if(v[j] < v[j-1])
                ok = 0;
        if(ok){
            for(auto pp : v) cout<<pp; puts("");
            continue;
        }
        for(int j = 1 ; j < v.size() ; j++){
            if(v[j] != 0 && v[j] > v[j-1])
                last = j;
            if(v[j] < v[j-1]) break;
        }
        v[last]--;
        for(int j = last + 1 ; j < v.size() ; j++)
            v[j] = 9;
        int qq = 0;
        while(v[qq] == 0) qq++;
        for(qq ; qq < v.size() ; qq++)
            cout<<v[qq];
        puts("");
    }
    return 0;
}

