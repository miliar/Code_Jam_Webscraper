#include<cstdio>
#include<map>
using namespace std;
int main(){
    freopen("small.in","r+",stdin);
    freopen("output.out","w+",stdout);
    long long int t,n,q;
    map<long long int,long long int> m;
    map<long long int,long long int>::iterator it;
    scanf("%lld",&t);
    for(int i=1;i<=t;i++){
        scanf("%lld %lld",&n,&q);
        m.clear();
        m[n]=1;
        while(1){
            it=m.end();
            it--;
            if((it->first)&1)
                m[((it->first)-1)/2]+=(it->second)*2;
            else{
                m[((it->first)/2)]+=it->second;
                m[((it->first)/2)-1]+=it->second;
            }
            q-=(it->second);
            if(q<=0){
                printf("Case #%d: %lld %lld\n",i,(it->first)/2,((it->first)-1)/2);
                break;
            }
            m.erase(it);
        }
    }
    
}
