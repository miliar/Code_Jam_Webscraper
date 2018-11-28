#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream f("p1.in");
    ofstream g("p1.out");
    int t;
    f>>t;
    int cel, db;
    double maxim=0;
    double tav, seb;
    double ered;
    //cout<<setprecision(8)<<(float)1000/3<<endl;
    for(int k=1; k<=t; k++)
    {
        cout<<k<<endl;
        f>>cel>>db;
        maxim=0;
        if(k==29) cout<<db<<endl;
        for(int i=1; i<=db; i++)
        {
            f>>tav>>seb;
            if(cel>tav)
            {
                if(k==29) cout<<"benne"<<endl;
                if((cel-tav)/seb>maxim) maxim=(double)(cel-tav)/seb;
            //cout<<db<<" "<<(float)(cel-tav)/seb<<endl;
                if(k==3) cout<<maxim<<endl;
            }
            if(k==29) cout<<maxim<<endl;
        }
        if(maxim>0)
        {
            ered=(double)cel/maxim;
            int szj=0;
            while(ered>1)
            {
                ered/=10;
                szj++;
            }
            //cout<<"szj="<<szj<<endl;
            g<<"Case #"<<k<<": "<<fixed<<setprecision(6)<<cel/maxim<<endl;
        }
        else g<<"Case #"<<k<<": 10000.000000"<<endl;
    }
    return 0;
}
