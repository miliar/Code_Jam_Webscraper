#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;
typedef long long Int;

map<Int,Int> mymap;
map<Int,Int>::iterator myit;
int t;
Int n,k;

void Add(Int sz,Int ctr)
{
    myit=mymap.find(sz);

    if (myit==mymap.end())
    {
        mymap.insert(make_pair(sz,ctr));
    }
    else
    {
        (*myit).second=(*myit).second+ctr;
    }

    return;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int test;
    Int LastSize;
    Int sz,ctr;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%lld %lld",&n,&k);

        mymap.clear();
        mymap.insert(make_pair(n,1));

        while(k>0)
        {
            myit=mymap.end();
            myit--;

            if (k<=(*myit).second)
            {
                LastSize=(*myit).first;
                break;
            }

            sz=(*myit).first;
            ctr=(*myit).second;

            mymap.erase(myit);

            k-=ctr;

            if (sz%2==1)
            {
                Add(sz/2,ctr*2);
            }
            else
            {
                Add(sz/2,ctr);
                Add(sz/2-1,ctr);
            }
        }

        printf("Case #%d: ",test);
        if (LastSize%2==1)
        {
            printf("%lld %lld\n",LastSize/2,LastSize/2);
        }
        else
        {
            printf("%lld %lld\n",LastSize/2,LastSize/2-1LL);
        }
    }

    return 0;
}
