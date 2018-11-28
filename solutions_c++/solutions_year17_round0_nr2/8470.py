#include<fstream>
#include<string>
using namespace std;
ifstream f("in");
ofstream g("out1");
int t,T,a[20],i,j,p,b[20];
string n;
bool check()
{
    for(i=2;i<=p;++i) if(a[i-1]>a[i]) return 0;
    return 1;
}
int main()
{
    f>>T;
    for(t=1;t<=T;++t) {
    g<<"Case #"<<t<<": ";
    f>>n;
    p=n.size();
    for(i=0;i<p;++i) a[i+1]=n[i]-48;
    for(i=1;i<=p;++i) b[i]=a[i];
    while(!check()) {
    for(i=2;i<=p;++i) if(a[i-1]<=a[i]) { b[i-1]=a[i-1];
                                         b[i]=a[i];
                                         }
                      else { if(a[i-1]!=1) b[i-1]=a[i-1]-1;
                             else { for(j=1;j<=i-1;++j) b[j]=9;
                                    --p;
                                    }
                             for(;i<=p;++i) b[i]=9;
                             }
    for(i=1;i<=p;++i) a[i]=b[i];
    }
    for(i=1;i<=p;++i) g<<b[i];
    g<<'\n';
    }
    return 0;
}
