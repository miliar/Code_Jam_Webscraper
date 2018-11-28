#include<fstream>
#include<iomanip>
using namespace std;
ifstream f("in");
ofstream g("out");
int t,T,i,n;
double k,s,d,h;
int main()
{
    f>>T;
    for(t=1;t<=T;++t){
        f>>d>>n;
        h=0;
        for(i=1;i<=n;++i) { f>>k>>s;
                            if((d-k)/s>h) h=(d-k)/s;
                            }
        g<<"Case #"<<t<<": "<<setprecision(6)<<fixed<<d/h<<'\n';
    }
}
