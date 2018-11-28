#include <bits/stdc++.h>

using namespace std ;

int main()
{
    freopen("C-small-2-attempt0.in", "r" , stdin);
    freopen("ouput.txt", "w" , stdout);
    int T , N , K , ls , rs ;

    scanf("%d", &T);

    for(int i = 0 ; i < T ; i++)
    {
        scanf("%d %d", &N , &K);

        priority_queue <int> current_pick ;
        current_pick.push(N);

        while(K!=0)
        {
            int current_space = current_pick.top();
            current_pick.pop();

            current_space--;

            ls = current_space / 2 ;
            if(ls*2 != current_space)
            {
                rs = ls+1;
            }
            else
            {
                rs = ls ;
            }

            current_pick.push(rs);
            current_pick.push(ls);
            K--;
        }
        printf("Case #%d: %d %d\n",i+1 ,max(ls,rs) ,min(ls,rs) );

    }
    return 0;
}
