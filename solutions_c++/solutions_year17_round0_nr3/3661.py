#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;

int main(){
    
    int k; scanf("%d", &k);

    for(int case_num = 1;case_num <= k;case_num++){

        priority_queue<int> prc;
        
        int n, k; scanf("%d %d", &n, &k);

        prc.push(n);

        for(int lx = 1;lx < k;lx++){
            int t = prc.top()-1;
            prc.pop();
            prc.push(t/2);
            prc.push(t-t/2);
        }

        int t = prc.top()-1;
        printf("Case #%d: %d %d\n", case_num, t-t/2, t/2);
    }

    return 0;
}
