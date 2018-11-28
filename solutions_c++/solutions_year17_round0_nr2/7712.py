#include <iostream>
#include <cstdio>

using namespace std;

int tam,i,j,n,c;
string s;

int main()
{
    freopen("i.in","r",stdin);
    freopen("o.on","w",stdout);
    cin>>n;
    while (n--)
    {
        cout<<"Case #"<<++c<<": ";
        cin>>s;
        tam=s.size();
        if (tam==1) cout<<s<<endl;
        else
        {
            for (i=tam-1;i>0;i--)
            {
                if (s[i]<s[i-1])
                {
                    for (j=i;j<tam;j++) s[j]='9';
                    s[i-1]--;
                }
            }
            if (s[0]<='0')
            {
                for (i=1;i<tam;i++) cout<<s[i];
                cout<<endl;
            }
            else cout<<s<<endl;
        }
    }
    fclose(stdin);
    fclose(stdout);
}
