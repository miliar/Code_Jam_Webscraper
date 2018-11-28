#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <deque>
#include <vector>

using namespace std;

int seats;
int customers;
int tickets;
int stotal[1001];
int ctotal[1001];

int canBeSolved(int rides) {
    int ans = 0;
    int i;
    int spaces = 0;
    for (i = 1; i <= seats; i++) {
        if (stotal[i] > rides) {
            if (stotal[i] - rides > spaces)
                return -1;
            ans += stotal[i]-rides;
            spaces -= (stotal[i]-rides);
        } else {
            spaces += rides-stotal[i];
        }
        
    }
    return ans;
}
    
int main() {
    int TT, T;
    scanf("%d", &TT);
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        scanf("%d%d%d", &seats, &customers, &tickets);
        
        int i;
        for (i = 0; i <= customers; i++)
            ctotal[i] = 0;
        for (i = 0; i <= seats; i++)
            stotal[i] = 0;
        int cmax = 0;
        for (i = 0; i < tickets; i++) {
            int seat, cust;
            scanf("%d%d", &seat, &cust);
            ctotal[cust]++;
            cmax = max(ctotal[cust], cmax);
            stotal[seat]++;
        }
        while(true) {
            int res = canBeSolved(cmax);
            if (res >= 0) {
                printf("%d %d\n", cmax, res);
                break;
            }
            cmax++;
        }
        

    }
}
        