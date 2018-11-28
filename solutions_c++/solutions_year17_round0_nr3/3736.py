#include <bits/stdc++.h>
using namespace std;

int main()
{

    long long int t,n,k,i,j;
    long long int ops,rs,cr,sp1,sp2,np1,np2,mx,mn,flr;

    ifstream fin ("C:\\Users\\ADMIN\\Desktop\\CodeJam17\\input.txt");
    ofstream fout ("C:\\Users\\ADMIN\\Desktop\\CodeJam17\\sol.txt");

    fin>>t;

    for(j=1;j<=t;j++)
    {
        fin>>n>>k;
        k=k-1;
        flr=floor(log2(k+1));
        ops = pow(2,flr)-1;

        rs = n-ops;
        cr = k+1-ops;

        if((rs%(ops+1))==0)
        {
            sp1=(rs/(ops+1));

            if(sp1%2)
            {
                mx = floor((sp1/2));
                mn = mx;
            }
            else
            {
                mx = (sp1/2);
                mn = mx-1;
            }

            fout<<"Case #"<<j<<": "<<mx<<" "<<mn<<"\n";
        }
        else
        {
            sp1 = floor((rs/(ops+1)));
            sp2 = sp1+1;

            np2 = rs - ((ops+1)*sp1);
            np1 = ops+1-np2;

            if(sp2==1)
            {
                fout<<"Case #"<<j<<": "<<0<<" "<<0<<"\n";
            }
            else if(sp2==2)
            {
                if(cr<=np2)
                {
                    fout<<"Case #"<<j<<": "<<1<<" "<<0<<"\n";;
                }
                else
                {
                    fout<<"Case #"<<j<<": "<<0<<" "<<0<<"\n";
                }
            }
            else
            {
                if(cr>np2)
                {
                    if(sp1%2)
                    {
                        mx = floor((sp1/2));
                        mn = mx;
                    }
                    else
                    {
                        mx = (sp1/2);
                        mn = mx-1;
                    }
                }
                else
                {
                    if(sp2%2)
                    {
                        mx = floor((sp2/2));
                        mn = mx;
                    }
                    else
                    {
                        mx = (sp2/2);
                        mn = mx-1;
                    }

                }

                fout<<"Case #"<<j<<": "<<mx<<" "<<mn<<"\n";
            }


        }
    }

    return 0;
}
