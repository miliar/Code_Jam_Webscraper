#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define place first
#define id second
#define NMAX 1005

int n, c, m, tests;
int ticketsOn[NMAX];
pair<int,int> ticket[NMAX];
int viz[NMAX], mark[NMAX];

int main (){
    int a, b;
    
    scanf("%d",&tests);
    for(int t = 1; t <= tests; t++) {
        scanf("%d%d%d",&n,&c,&m);
        for(int i = 1; i <= m; i++) {
            scanf("%d%d",&a,&b);
            ticket[i] = make_pair(a, b);
            ticketsOn[a]++;
        }
        sort(ticket + 1, ticket + m + 1);
        int rides = 0, used = 0;
        memset(mark, 0, sizeof(mark));
        while(used < m) {
            rides++;
            int taken = 0;
            for(int i = 1; i <= m; i++) {
             //   printf("hah %d %d %d\n", i, taken + 1, ticket[i].place);
                if(!mark[i] && !viz[ticket[i].id] && taken + 1 <= ticket[i].place) {
                    mark[i] = 1;
                    viz[ticket[i].id] = 1;
                    taken++;
               //     printf("luat\n");
                }
            }
            memset(viz, 0, sizeof(viz));
            used += taken;
        }
        int promo = 0;
        for(int i = 1; i <= n; i++)
            if(ticketsOn[i] > rides)
                promo += ticketsOn[i] - rides;
        printf("Case #%d: %d %d\n", t, rides, promo);
        memset(ticketsOn, 0, sizeof(ticketsOn));
    }
    
    return 0;
}

#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<map>

using namespace std;

#define place first
#define id second
#define NMAX 1005

int n, c, m, tests;
int ticketsOn[NMAX];
pair<int,int> ticket[NMAX];
int viz[NMAX], mark[NMAX];

int main (){
    int a, b;
    
    scanf("%d",&tests);
    for(int t = 1; t <= tests; t++) {
        scanf("%d%d%d",&n,&c,&m);
        for(int i = 1; i <= m; i++) {
            scanf("%d%d",&a,&b);
            ticket[i] = make_pair(a, b);
            ticketsOn[a]++;
        }
        sort(ticket + 1, ticket + m + 1);
        int rides = 0, used = 0;
        memset(mark, 0, sizeof(mark));
        while(used < m) {
            rides++;
            int taken = 0;
            for(int i = 1; i <= m; i++) {
             //   printf("hah %d %d %d\n", i, taken + 1, ticket[i].place);
                if(!mark[i] && !viz[ticket[i].id] && taken + 1 <= ticket[i].place) {
                    mark[i] = 1;
                    viz[ticket[i].id] = 1;
                    taken++;
               //     printf("luat\n");
                }
            }
            memset(viz, 0, sizeof(viz));
            used += taken;
        }
        int promo = 0;
        for(int i = 1; i <= n; i++)
            if(ticketsOn[i] > rides)
                promo += ticketsOn[i] - rides;
        printf("Case #%d: %d %d\n", t, rides, promo);
        memset(ticketsOn, 0, sizeof(ticketsOn));
    }
    
    return 0;
}

