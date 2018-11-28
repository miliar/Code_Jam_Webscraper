#include <bits/stdc++.h>

using namespace std;

#define READ() 	    freopen("in.txt","r",stdin)
#define WRITE()     freopen("out.txt","w",stdout)
#define sf(n) 	    scanf("%d",&n)
#define sl(x)       scanf("%I64d",&x)
#define lsf(n) 	    scanf("%lld", &n)
#define pb(n) 	    push_back(n)
#define mem(x,y)    memset(x,y,sizeof(x))
#define D(x)      	cout << #x << " = " << x << endl
#define YOLO        cout << "YOLO" << endl
#define NL			printf("\n")
#define EPS 	    1e-10
#define INF         INT_MAX
#define MAX         INT_MAX
#define MOD         1000000007
#define LL          long long
#define endl        "\n"
#define pi          2.0*acos(0.0)
#define cnd         tree[idx]
#define lnd         tree[left]
#define rnd         tree[right]
#define callLeft    left,st,mid
#define callRight   right,mid+1,ed


int main()
{
//	ios_base::sync_with_stdio(false);
//    cin.tie(0); /// use "\n" instead of endl
#ifndef ONLINE_JUDGE
    READ();
    WRITE();
#endif
    int t;
    cin >> t;
    int TC = 0;
    while(t--)
    {
        LL x;
        cin >> x;
        LL k;
        cin >> k;

        multiset <LL> st;
        multiset <LL> :: iterator it;
        st.insert(x);
        int cnt = 0;
        LL l,r;
        while(k--)
        {
            it = st.end();
            it--;
            LL xx = *it;
            st.erase(it);
            if(xx % 2 == 1)
            {
                l = xx/2;
                r = xx/2;
                if(l>0)st.insert(l);
                if(r>0)st.insert(r);
            }
            else
            {
                l = xx/2;
                r = xx/2;
                l--;
                if(l>0)st.insert(l);
                if(r>0)st.insert(r);
            }
        }
        cout << "Case #" << ++TC << ": ";
        cout << max(r,l) << " " << min(l,r) << endl;
    }

    return 0;
}

