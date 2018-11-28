#include<cstdio>
#include<algorithm>
#include<map>
using namespace std;
long long n, K;
map<long long, long long>Map;
int main(){
    freopen("/Users/joseunghyeon/Downloads/C-large (1).in","r",stdin);
    freopen("/Users/joseunghyeon/Desktop/code2/output.txt","w",stdout);
    int TT, TC, i;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ",TT);
        scanf("%lld%lld",&n,&K);
        Map.clear();
        Map[n] = 1;
        while(1){
            auto it = Map.end();
            it--;
            long long a = it->first, c = it->second;
            Map.erase(it);
            if(K <= c){
                printf("%lld %lld\n",a/2, (a-1)/2);
                break;
            }
            K-=c;
            Map[a/2] += c;
            Map[(a-1)/2] += c;
        }
    }
}
