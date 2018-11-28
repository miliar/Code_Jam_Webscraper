#include <iostream>
#include <cstdio>

using namespace std;

bool wii;
int c,n,k,i,tam,R,sum[1010];
string s;

int main()
{
    freopen("i.in","r",stdin);
    freopen("o.on","w",stdout);
    cin>>n;
    while (n--)
    {
        cin>>s>>k;
        s=" "+s;
        tam=s.size();
        R=0;
        for (i=0;i<=tam;i++) sum[i]=0;
        wii=true;
        for (i=1;i<tam;i++)
        {
            sum[i]+=sum[i-1];
            if (i+k<=tam)
            {
                if (s[i]=='-' && !(sum[i]&1))
                {
                    sum[i]++;
                    sum[i+k]--;
                    R++;
                }
                else if (s[i]=='+' && (sum[i]&1))
                {
                    sum[i]++;
                    sum[i+k]--;
                    R++;
                }
            }
        }
        for (i=1;i<tam;i++)
        {
            if (s[i]=='-' && !(sum[i]&1)) wii=false;
            else if (s[i]=='+' && (sum[i]&1)) wii=false;
        }
        cout<<"Case #"<<++c<<": ";
        if (wii) cout<<R<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
