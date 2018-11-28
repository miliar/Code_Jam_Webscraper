#include<cstdio>
#include<algorithm>
#include<set>
using namespace std;

set <int> st;
int alln,k;
bool num[1005];
int main()
{
    freopen("C-small-1-attempt0.in" , "r" , stdin);
    freopen("opt.out" , "w" , stdout);
    int allt,nowt = 0;
    scanf("%d",&allt);
    num[0] = true;
    num[1001] = true;
    while(++nowt <= allt){
        printf("Case #%d: ",nowt);
        st.clear();
        scanf("%d%d",&alln,&k);
        for(int i=1;i<=alln;++i)
            num[i] = false;
        num[alln+1] = true;
        st.insert(0);
        st.insert(alln+1);
        set <int> :: iterator it;
        for(int i=1;i<=k;++i){
            int ok = 1000000;
            int mndisok = -1;
            int mxdisok = -1;
            for(int j=1;j<=alln;++j){
                if(num[j])
                    continue;
                it = st.upper_bound(j);
                int near = (*it);
                it--;
                int near2 = (*it);
                int mn = min( near-j-1 , j-near2-1 );
                int mx = max( near-j-1 , j-near2-1 );

                if(mn > mndisok){
                    ok = j;
                    mndisok = mn;
                    mxdisok = mx;
                }
                else if(mn == mndisok){
                    if(mxdisok < mx){
                        ok = j;
                        mxdisok = mx;
                    }
                }
            }
            num[ok] = true;
            st.insert(ok);
            if(i == k){
                printf("%d %d\n",mxdisok,mndisok);
            }
        }


    }


    return 0;
}
