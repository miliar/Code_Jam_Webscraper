#include<stdio.h>
#include<algorithm>
using namespace std;

struct A
{
    int st;
    int ed;
    int who;
    bool operator()(A a, A b)
    {
        return a.st<b.st;
    }
}arr[210];

struct B
{
    int time;
    bool chk;//true:ans+2    false:ans
    bool operator()(B a, B b)
    {
        if(a.chk==false && b.chk==true) return true;
        if(a.chk==true && b.chk==false) return false;
        return a.time > b.time;
    }
};
B jft[110], cft[110];
int sj, sc;
int ct, jt, ac, aj;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i, T, tt, ans, ti, ft;
    scanf("%d", &T);
    for(tt=1; tt<=T; ++tt)
    {
        ans=ct=jt=sc=sj=0;
        scanf("%d%d", &ac, &aj);
        for(i=1; i<=ac; ++i)
        {
            scanf("%d%d", &arr[i].st, &arr[i].ed);
            arr[i].who = 1;
        }
        for(i=ac+1; i<=ac+aj; ++i)
        {
            scanf("%d%d", &arr[i].st, &arr[i].ed);
            arr[i].who = 2;
        }
        sort(&arr[1], &arr[ac+aj+1], A());
        for(i=1; i<ac+aj; ++i)
        {
            ti = arr[i+1].st-arr[i].st;
            ft = arr[i+1].st-arr[i].ed;
            if(arr[i].who == 1)
            {
                ct += ti;
                cft[++sc].time = ft;
                if(arr[i+1].who != arr[i].who){ ++ans; cft[sc].chk=false; }
                else cft[sc].chk = true;
            }
            else
            {
                jt += ti;
                jft[++sj].time = ft;
                if(arr[i+1].who != arr[i].who){ ++ans; jft[sj].chk=false; }
                else jft[sj].chk = true;
            }
        }
        ti = arr[1].st - arr[ac+aj].st + 1440;
        ft = arr[1].st - arr[ac+aj].ed + 1440;
        if(arr[ac+aj].who == 1)
        {
            ct += ti;
            cft[++sc].time = ft;
            if(arr[1].who != arr[ac+aj].who){ ++ans; cft[sc].chk=false; }
            else cft[sc].chk = true;
        }
        else
        {
            jt += ti;
            jft[++sj].time = ft;
            if(arr[1].who != arr[ac+aj].who){ ++ans; jft[sj].chk=false; }
            else jft[sj].chk = true;
        }
        sort(&cft[1], &cft[sc+1], B());
        sort(&jft[1], &jft[sj+1], B());
        if(ct > jt)
        {
            int p=1;
            while(ct > jt)
            {
                ct -= cft[p].time;
                jt += cft[p].time;
                if(cft[p].chk) ans+=2;
                ++p;
            }
        }
        else if(ct < jt)
        {
            int p=1;
            while(ct < jt)
            {
                ct += jft[p].time;
                jt -= jft[p].time;
                if(jft[p].chk) ans+=2;
                ++p;
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
}
