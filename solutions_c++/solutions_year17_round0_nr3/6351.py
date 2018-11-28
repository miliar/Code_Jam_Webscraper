#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define x first
#define y second
#define NMAX 1000005
#define pii pair< pair<int,int>, int> 

int T, n, k;

pii getPair(int left, int right) {
    int index = (left + right) / 2;
    return make_pair(make_pair(index - left, right - index), index);
}

class cmp
{
public:
    bool operator()(const pii& a,const pii& b)
    {
        if(a.x.x == b.x.x){
            if(a.x.y == b.x.y)
                return a.y < b.y;
            return a.x.y > b.x.y;
        }
        return a.x.x > b.x.x;
    }
};

set< pii, cmp > setI;

int main (){

    scanf("%d",&T);
    for(int t = 1; t <= T; t++) {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ", t);
        setI.insert(getPair(1, n));
        
        for(int i = 1; i <= k; i++) {
            pii P = *setI.begin();
            setI.erase(P);
            if(P.x.x) {
                setI.insert(getPair(P.y - P.x.x, P.y - 1));
            }
            if(P.x.y) {
                setI.insert(getPair(P.y + 1, P.y + P.x.y));
            }
            if(i == k){
                printf("%d %d\n", P.x.y, P.x.x);
            }
        }
    }
    
    
    return 0;
}


