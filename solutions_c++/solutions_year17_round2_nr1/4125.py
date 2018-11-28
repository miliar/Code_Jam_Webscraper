
#include<iostream>
#include<algorithm>
#include<memory.h>
#include<stdio.h>
#include<string>
#include<vector>
#include<bitset>
#include<climits>
#include<list>
#include<set>
#include<fstream>
#include<iomanip>

using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;

struct st
{
    long double k;
    long double s;
};

bool acompare(st lhs, st rhs) { return lhs.k < rhs.k; }

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    ofstream aout("a.txt");
    ifstream ain("A-small-attempt2.in");

    int t,n;
    ain>>t;
    long double d,flag;
    long double time,pt;

    for(int tc=1;tc<=t;tc++)
    {
        ain>>d>>n;
        time=0;
        pt=0;
        flag=0;

        st  ks[n];
        for(int i=0;i<n;i++)
        {
            ain>>ks[i].k;
            ain>>ks[i].s;
        }

        sort(ks,ks+n,acompare);

        for(int i=1;i<n;i++)
        {
            //cout<<ks[i].k<<' '<<ks[i].s<<endl;
            if(ks[i].s<ks[i-1].s)
            {
                if(tc==26)
                cout<<"d="<<d;
                pt=time;
                time+=(ks[i].k-ks[i-1].k)/(ks[i-1].s-ks[i].s);
                if((ks[i].k+(time*ks[i].s))>d)
                {
                    if(tc==26)
                    cout<<"if";
                    time=pt+(d-ks[i-1].k-(pt*ks[i-1].s))/ks[i-1].s;
                    if(i==n-1)
                        flag=1;
                }

            }
            else
            {
                if(tc==26)
                cout<<"else"<<i;
                pt=time;
                time+=pt+(d-ks[i-1].k-(pt*ks[i-1].s))/ks[i-1].s;
                if(tc==26)
                    cout<<time;
                flag=1;
                break;
            }
        }

        if(flag==0)
        {

        if(tc==26)
            cout<<"if"<<time;
            time+=(d-ks[n-1].k-(time*ks[n-1].s))/ks[n-1].s;
        }


        aout<<fixed<<"Case #"<<tc<<": "<<setprecision(6)<<d/time<<endl;





    }



    return 0;
}



