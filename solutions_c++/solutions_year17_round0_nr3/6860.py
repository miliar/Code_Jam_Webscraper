#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#define f first
#define s second

int main()
{
   // 1 1 0 1 0 0 1 0 1 0 0 1
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t;
    cin >>t;
    for (int iii=0; iii<t; iii++)
    {
        int n,k;
        cin >>n>>k;
       /* long long x=0;
        vector < pair < long long , long long > > por;
        por.push_back(make_pair(n,1));
        int pos=0;
        while (x<k)
        {
            long long r=por[pos].f;
            if (r%2==0)
            {
                por.push_back(make_pair(r/2,por[pos].s));
                por.push_back(make_pair((r/2)-1,por[pos].s));
                x+=por[pos].s;
            }
            else
            {
                por.push_back(make_pair(r/2,por[pos].s*2ll));
                x+=por[pos].s;
            }
            pos++;
        }
        pos--;
        long long rr=por[pos].f,ans1,ans2;
        if (rr%2==1)
            ans1=rr/2,ans2=rr/2;
        else
            ans1=rr/2,ans2=(rr/2)-1;*/
        bool mark[1100];
        for (int i=0; i<=n+1; i++)
            mark[i]=false;
        mark[0]=true; mark[n+1]=true;
        int last;
        for (int kk=0; kk<k; kk++)
        {
            int nom,max1=-1,max2=-1;
            for (int i=1; i<=n; i++)
                if (!mark[i])
                    {
                        int kol1=0,j=i-1;
                        while (j>=0 && !mark[j])
                            kol1++,j--;
                        int kol2=0;
                        j=i+1;
                        while (j<=n+1 && !mark[j])
                            kol2++,j++;
                        if (min(kol1,kol2)>max1 || (min(kol2,kol1)==max1 && max(kol1,kol2)>max2))
                        {
                            max1=kol1;
                            max2=kol2;
                            nom=i;
                        }
                    }
            mark[nom]=true;
            last=nom;
        }
        int kol1=0,j=last-1;
        while (j>=0 && !mark[j])
            kol1++,j--;
        int kol2=0;
        j=last+1;
        while (j<=n+1 && !mark[j])
            kol2++,j++;
        int ans1=max(kol1,kol2);
        int ans2=min(kol1,kol2);
        cout <<"Case #"<<iii+1<<": "<<ans1<<" "<<ans2<<"\n";
    }
    //1 0 1 1 0 1 0 1 1 0 1
    return 0;
}
