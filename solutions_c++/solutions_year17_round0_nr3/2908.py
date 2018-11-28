#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    fstream plik1, plik2;
    plik1.open( "C:\\Users\\G500\\Desktop\\plik\\inputc.txt",ios::in );
    plik2.open( "C:\\Users\\G500\\Desktop\\plik\\outputc.txt",ios::out ); //| ios::app );
    int T,n,p,x1,x2,xp,xl,lp,ln,llp,lln,pp,nn,x,k,pot;
    plik1>>T;
    for(int t=1;t<=T;t++)
    {
        plik1>>x>>k;
        if(k==1)
        {
            if(x%2==0)
            {
                xp=x/2;
                xl=xp-1;
            }
            else
            {
                xp=x/2;
                xl=xp;
            }
            plik2<<"Case #"<<t<<": "<<xp<<" "<<xl<<"\n";
            continue;
        }
        pot=4;
        if(n%2)
        {
            n=x;
            p=0;
            ln=1;
            lp=0;
        }
        else
        {
            n=0;
            p=x;
            ln=0;
            lp=1;
        }
        while(true)
        {
            //cout<<"dupa";
            pp=0;
            nn=0;
            llp=0;
            lln=0;
            if(lp!=0)  //parzysta
            {
                x1=p/2;
                x2=x1-1;
                if(x1%2==0)
                {
                    pp=x1;
                    nn=x2;
                }
                else
                {
                    pp=x2;
                    nn=x1;

                }
                llp+=lp;
                lln+=lp;
            }
            if(ln!=0)  //nieparzysta
            {
                x1=n/2;
                if(x1%2==0)
                {
                    pp=x1;
                    llp+=(ln*2);
                }
                else
                {
                    nn=x1;
                    lln+=(ln*2);
                }
            }
            p=pp;
            n=nn;
            lp=llp;
            ln=lln;
            //cout<<p<<" "<<n<<" "<<lp<<" "<<ln<<"\n";
            if((pot-1)>=k)
            {
                k=k-(pot/2)+1;
                //cout<<"k = "<<k<<"\n";
                if(p<n)
                {
                    if(k<=ln)
                    {
                        xp=n/2;
                        xl=xp;
                    }
                    else
                    {
                        xp=p/2;
                        xl=xp-1;
                    }
                }
                else
                {
                    if(k<=lp)
                    {
                        xp=p/2;
                        xl=xp-1;
                    }
                    else
                    {
                        xp=n/2;
                        xl=xp;
                    }
                }
                break;
            }
            pot*=2;
        }
        plik2<<"Case #"<<t<<": "<<xp<<" "<<xl<<"\n";
    }
    plik1.close();
    plik2.close();
    return 0;
}
