
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <cstring>
#include <math.h>

using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;
typedef long double ld;

bool wayToSort(lli i, lli j) { return i > j; }

int main() {

    lli t;
    cin >> t;

    for(lli num=0;num<t;num++)
    {
        lli n,k;
        cin >> n >> k;

        lli val[n+5];
        fill_n(val,n+5,0);

        val[1]=n;

        lli v=(n/2);

        for(lli i=1;i<=v;i++)
        {

            if(val[i]&1==1)
            {
                val[2*i]=val[i]/2;
                val[2*i+1]=val[i]/2;
            }
            else
            {
                val[2*i]=val[i]/2;
                val[2*i+1]=(val[i]-1)/2;
            }
            //if((2*i==k)||(((2*i)+1)==k)) break;
        }


        lli max,min;

        sort(val+1,val+n,wayToSort);


        if(val[k]&1==1)
        {
            min=val[k]/2;
            max=val[k]/2;
        }
        else
        {
            max=val[k]/2;
            min=(val[k]-1)/2;
        }

        cout << "Case #" << num+1 << ": " << max << " " << min << endl;

    }

    return 0;
}


