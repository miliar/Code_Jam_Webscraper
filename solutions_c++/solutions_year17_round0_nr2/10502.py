    #include <string>
    #include <algorithm>
    #include <math.h>
    #include <vector>
    #include <queue>
    #include <stack>
    #include <stdio.h>
    #include <stdlib.h>
    #include <cstdlib>
    #include <iostream>
    #include <set>
    #include <cstring>
    #include <map>
    #include <iomanip>
    #include <sstream>
    #include <utility>
    #include <iterator>
    #include <ctype.h>
    #include <cmath>


using namespace std;

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    long long int n,t,h,i,j,s;
    cin>>t;
    for (j=0;j<t;j++)
    {
        cin >>n;
        if(n<10) cout<<"Case #"<<j+1<<": "<< n<<endl;
        else if (n==10) cout<<"Case #"<<j+1<<": "<< 9<<endl;
        else
        {
            for(i=n;i>10;i--)
            {
                s=i;
                while (s>10)
                {
                    if((s%10)>=((s%100)/10))
                        {s=s/10;

                        }
                    else break;
                }
                if (s<10)
                    {h=i;
                    break;
                    }

            }

                    cout<<"Case #"<<j+1<<": "<< h<<endl;
        }

    }
    return 0;
}
