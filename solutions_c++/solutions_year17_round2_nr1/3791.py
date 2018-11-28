#include <bits/stdc++.h>

using namespace std;

int main()
{
    ofstream myfile ("example.txt");
    ifstream ip ("A-large.txt");
    int k=1;
      int t;
      ip>>t;
      if (myfile.is_open())
      {
        while(t--)
        {
        int d,n;
        ip>>d>>n;
        float mn=FLT_MIN;
        while(n--)
        {
            int a,b;
            ip>>a>>b;
            float dist=d-a;
            dist/=(float)b;

            mn=max(mn,dist);
        }
        float ans=(float)d/mn;
        // printf("%6f",d);
        // printf("\n");
         myfile<<"Case #"<<k<<": ";


        myfile<<fixed<<setprecision(8)<<ans<<endl;

        k++;
        }
      }

    return 0;
}
