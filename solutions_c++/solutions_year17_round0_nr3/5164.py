#include<bits/stdc++.h>
#define ull unsigned long long
using namespace std;

map<ull, ull>mp;

int main()
{
    //cout<<mp[0]<<endl;
    ull x= 0;
    for(ull i=0; i<63; i++)
    {
        x+= (1llu<<(i));

        mp[i+1]= x;

        //cout<<x<<" msk : "<<i+1<<endl;
    }

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ull t, cs= 0, n, k, z;
    ull boro, choto, rest, m;

    scanf("%llu", &t);

    while(t--)
    {
        scanf("%llu %llu", &n, &k);

//        if(k==1)
//        {
//            n--;
//            choto= n/2;
//            boro= n - choto;
////            if(choto>boro)
////                swap(boro, choto);
//        }
//        else if(k>(n/2))
//        {
//            boro= 0;
//            choto= 0;
//        }
        //else
        //{
            z= log2(k);

            n-= mp[z];

            m= (1<<(z+1))-(1<<(z));

            rest= n%m;

            m= n/m;

            if(rest>=(k-mp[z]))
                m++;

            m--;

            choto= m/2;
            boro= m - choto;
//            if(choto>boro)
//                swap(boro, choto);
        //}

        printf("Case #%llu: %llu %llu\n", ++cs, boro, choto);
    }

    return 0;
}
