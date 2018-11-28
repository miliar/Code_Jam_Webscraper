#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <cstdlib>

using namespace std;

fstream f("D-small-attempt0.in", ios_base::in);
fstream g("output.txt", iostream::out);
int t;

int n, m, r, c;
char type;

int pos=0;
bool isO=false;
int count=0;

int main()
{
    f>>t;
    for(int i=1; i<t+1; ++i)
    {
        f>>n; f>>m;
        bool* arr=new bool[n] {};
        for(int j=0; j<m; ++j)
        {
            f>>type; f>>r; f>>c;
            if(type=='o') {pos=c; isO=true;}
            else if(type=='x') pos=c;
            arr[c-1]=1;
            ++count;
        }
        if(n==1)
        {
            if(isO) g<<"Case #"<<i<<": "<<2<<" "<<0<<endl;
            else g<<"Case #"<<i<<": "<<2<<" "<<1<<endl<<"o 1 1"<<endl;
        }
        else
        {
            g<<"Case #"<<i<<": "<<3*n-2<<" ";
            if(isO || (!pos && !arr[0])) g<<3*n-3-count<<endl; else g<<3*n-3-count+1<<endl;

            if(!pos) {pos=1; arr[0]=true; g<<"o 1 1"<<endl;}
            else if(!isO) g<<"o 1 "<<pos<<endl;

            for(int j=0; j<n; ++j) {if(!arr[j]) g<<"+ 1 "<<j+1<<endl;}

            if(pos!=n)
            {
                int k=1;
                for(int j=2; j<=n; ++j) {if(k==pos) ++k; g<<"x "<<j<<" "<<k<<endl; ++k;}
            }
            else
            {
                for(int j=n; j>=2; --j) {g<<"x "<<j<<" "<<n-j+1<<endl;}
            }

            if(n!=2) for(int j=2; j<n; ++j) g<<"+ "<<n<<" "<<j<<endl;
        }
        pos=0;
        count=0;
        isO=false;
        delete [] arr;
    }

    return 0;
}
