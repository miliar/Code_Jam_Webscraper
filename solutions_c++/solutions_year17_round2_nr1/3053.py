#include<bits/stdc++.h>

using namespace std;

int main()
{
    int T, test=1;

    ifstream fin;
    ofstream fout;
    fin.open("1B-A-Large.in",ios::in);
    fout.open("1B-A-Large-out.txt",ios::out);
    fin>>T;

    while(T--)
    {
        cout<<test<<endl;
        long long int n,d,k,s;

        fin>>d>>n;

        long double t, maxi=0;
        for(int i=0;i<n;i++)
        {
            fin>>k>>s;
            t = (long double) (d-k) / (long double) s;
            maxi = t>maxi?t:maxi;
        }

        fout<<"Case #"<<test++<<": "<<fixed<<setprecision(6)<<(long double)d/maxi;
        fout<<endl;
    }
    return 0;
}
