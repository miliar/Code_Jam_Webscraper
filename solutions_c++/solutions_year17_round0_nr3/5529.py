#include <iostream>
#include <set>
using namespace std;

struct node
{
    unsigned long long s, e;
};

bool operator < (node a, node b)
{

    unsigned long long diff1= (a.e- a.s),diff2= (b.e- b.s);
    if(diff1 != diff2) return diff1 > diff2;
    return a.s < b.s;
}

int main() {
    unsigned long long range,k,cent,sum,diff;
    int T,t ;node sol,temp1,temp2;
    set<node> S;
    /*freopen("s.txt", "r", stdin);
    freopen("ss.txt", "w", stdout);*/
    scanf("%d", &T);

    for (t=0 ;t < T;t++) {
        cin >> range>>k;
        sol.s=1,sol.e=range;
        S.insert(sol);
        while(k--){
            sol = *S.begin();
            S.erase(S.begin());
            if(sol.e-sol.s ==1)  temp1.s=sol.s+1,temp1.e=sol.e,S.insert(temp1);
            else if(sol.e != sol.s){
                cent = (sol.e+ sol.s)/2;
                temp1.s=sol.s,temp1.e=cent-1, temp2.s=cent+1,temp2.e=sol.e,S.insert(temp1),S.insert(temp2);
            }
        }

        diff=sol.e-sol.s;
        printf("Case #%d: %llu %llu", t+1,((diff)&1?diff/2+1:diff/2),diff/2);
        if(t != T-1)
            printf("\n");

        S.clear();
    }
}