#include <fstream>

using namespace std;


ifstream fin ("input.in");
ofstream fout ("output.out");
int t;
long long n, k, val;
long long p[5][5], v[5][5];

int main()
{
    int i, nrt, act=1, next=0;
    fin>>t;
    for(nrt=1; nrt<=t; ++nrt)
    {
        fin>>n>>k;
        if(n==k)
            {fout<<"Case #"<<nrt<<": 0 0\n"; continue;}

        p[act][0]=p[act][1]=p[next][0]=p[next][1]=v[act][0]=v[act][1]=v[next][0]=v[next][1]=0;
        ++p[act][n%2];
        v[act][n%2]=n;

        while(1)
        {
            if(v[act][1]>v[act][0])
            {
                val=v[act][1]/2;
                if(k<=p[act][1])
                    {fout<<"Case #"<<nrt<<": "<<val<<' '<<val<<'\n'; break;}
                else if( p[act][1])
                {
                    k=k-p[act][1];
                    p[next][val%2]+=2*p[act][1];
                    v[next][val%2]=val;
                }

                val=v[act][0]/2;
                if(k<=p[act][0])
                    {fout<<"Case #"<<nrt<<": "<<val<<' '<<val-1<<'\n'; break;}
                else if( p[act][0])
                {
                    k=k-p[act][0];
                    p[next][val%2]+=p[act][0];
                    v[next][val%2]=val;

                    p[next][(val-1)%2]+=p[act][0];
                    v[next][(val-1)%2]=val-1;
                }
            }
            else
            {
                val=v[act][0]/2;
                if(k<=p[act][0])
                    {fout<<"Case #"<<nrt<<": "<<val<<' '<<val-1<<'\n'; break;}
                else if( p[act][0])
                {
                    k=k-p[act][0];
                    p[next][val%2]+=p[act][0];
                    v[next][val%2]=val;

                    p[next][(val-1)%2]+=p[act][0];
                    v[next][(val-1)%2]=val-1;
                }

                val=v[act][1]/2;
                if(k<=p[act][1])
                    {fout<<"Case #"<<nrt<<": "<<val<<' '<<val<<'\n'; break;}
                else if( p[act][1])
                {
                    k=k-p[act][1];
                    p[next][val%2]+=2*p[act][1];
                    v[next][val%2]=val;
                }
            }
            p[act][0]=p[act][1]=0;
            act=1^act;
            next=1^next;
        }
    }
    return 0;
}
