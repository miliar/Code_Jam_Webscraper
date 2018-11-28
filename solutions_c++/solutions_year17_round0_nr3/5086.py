#include <cstdio>
#include <set>

using namespace std;

int main(){
    int n,k,t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
    scanf("%d%d",&n,&k);
    multiset<int> l;
    l.insert(n);
    for(int i=0;i<k-1;i++){
        int x=*(--l.end());
        l.erase(--l.end());
        l.insert((x-1)/2);
        l.insert(x-1-(x-1)/2);
    }
    int x = *(--l.end());
    printf("Case #%d: %d %d\n",cas,x-1-(x-1)/2,(x-1)/2);
    }
return 0;
}
