#include<fstream>
#include<cstring>
using namespace std;
ifstream f("in");
ofstream g("out");
int t,T,i,j,n,k,m;
char s[1001];
bool a[1001];
int main()
{
    f>>T;
    for(t=1;t<=T;++t) {
    f.getline(s,1001,' ');
    n=strlen(s)-1;
    for(i=1;i<=n;++i) { if(s[i]=='+') a[i]=1;
                       else a[i]=0;
                       }
    f>>k;
    m=0;
    for(i=1;i<=n-k+1;++i) if(!a[i]) { for(j=i;j<=i+k-1;++j) a[j]=1-a[j];
                                      ++m;
                                      }
    for(i=n-k+2;i<=n;++i) if(!a[i]) m=-1;
    g<<"Case #"<<t<<": ";
    if(m==-1) g<<"IMPOSSIBLE";
    else g<<m;
    g<<'\n';
    for(i=0;i<=1000;++i) s[i]=0;
    }
    return 0;
}
