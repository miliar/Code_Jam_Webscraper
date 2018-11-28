#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
using namespace std;

#define MEMSET(x) memset(x, 0, sizeof(x))

//bool debug = true;
bool debug = false;

int main(void){
    int T;
    int N, K;
    int tmp, L, R;


    scanf("%d", &T);
    for(int t=1; t<=T; t++){
        // initial
        priority_queue <int> pq;

        // input
        scanf("%d%d", &N, &K);

        //  solve
        pq.push(N);
        while( K>0 ){
            tmp = pq.top();
if(debug)printf("%d\n", tmp);
            pq.pop();

            tmp--;
            L = tmp/2;
            R = tmp/2;
            if( tmp!=0 )
                R += tmp%2;

            pq.push( L );
            pq.push( R );

            K--;
        }

        //  output
        printf("Case #%d: %d %d\n", t, R, L);

    }

    return 0;
}
