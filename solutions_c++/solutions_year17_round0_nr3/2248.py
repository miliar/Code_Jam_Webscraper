#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define xx first
#define yy second
using namespace std;

set<pair<ll,ll> > st;
set<pair<ll,ll> > ::iterator it;

int main()
{

    freopen("C-large.in","r",  stdin);
    freopen("C-large-output.txt","w", stdout);
    int t,cs=1;
    ll n,k;
    scanf("%d",&t);

    while(t--)
    {
        scanf("%lld %lld",&n,&k);

        ll x=k-1;
        st.insert(mp(n,1));
        while(x)
        {
            it= st.end();
            it--;
            pair<ll,ll> p1,p2,p;
            p= *it;
//            printf("<<< %lld %lld %lld\n",x, p.xx,p.yy);
            if(x>= p.yy)
            {
                st.erase(it);
//                printf("a\n");
                x-=p.yy;
                p1= mp((p.xx-1)/2, p.yy);
                p2=p1;
                if((p.xx-1)%2) p2.xx++;
                if(p1.xx>0)
                {
                    it= st.lower_bound(mp(p1.xx,0));
                    p=*it;
                    if(p.xx== p1.xx)
                    {
                        p.yy+= p1.yy;
                        st.erase(it);
                        st.insert(p);
                    }
                    else
                    {
                        st.insert(p1);
                    }
                }
                if(p2.xx>0)
                {
                    it= st.lower_bound(mp(p2.xx,0));
                    p=*it;
                    if(p.xx== p2.xx)
                    {
                        p.yy+= p2.yy;
                        st.erase(it);
                        st.insert(p);
                    }
                    else
                    {
                        st.insert(p2);
                    }
                }
            }
            else
            {
                x=0;
            }
//
//            for(it=st.begin(); it!=st.end(); it++)
//            {
//                printf("      %lld %lld\n",(*it).xx, (*it).yy);
//            }

//            printf("%lld %d\n",x,st.size());
        }

//        for(it=st.begin(); it!=st.end(); it++)
//        {
//            printf("      %lld %lld\n",(*it).xx, (*it).yy);
//        }
        it= st.end();
        it--;
        pair<ll,ll> p;
        p=*it;
        ll l,r;
        l= (p.xx-1)/2;
        r=l;
        if((p.xx-1)%2) r++;
        printf("Case #%d: %lld %lld\n",cs++,r,l);
        st.clear();
    }
}
