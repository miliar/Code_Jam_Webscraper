#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <tuple>
#include <cmath>
using namespace std;
typedef pair<int,int> P;
typedef tuple<int,int,int> T;
const double pi = M_PI;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int N,P;
        cin>>N>>P;
        vector<int> cnt(P);
        for(int i=0;i<N;i++){
            int G;
            cin>>G;
            cnt[G%P]++;
        }
        int ans =cnt[0];
        if(P==4){
            ;
        }else if(P==3){
            int p = min(cnt[1],cnt[2]);
            ans +=p;
            cnt[1]-=p;
            cnt[2]-=p;
            if(cnt[1]){
                ans+=(cnt[1]+2)/3;
            }
            if(cnt[2]){
                ans+=(cnt[2]+2)/3;
            }
        }else{
            ans+=(cnt[1]+1)/2;
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}