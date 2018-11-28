#include <iostream>
#include <cstdio>
using namespace std;
long long int t,k,nr,flips,lungime;
string s;
bool V[10000],ok;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for (long long int  test=1;test<=t;test++)
    {
        cin>>s;
        cin>>k;
        lungime = s.length();
        for (int q=0;q<lungime;q++)
        {
            V[q]=false;
        }
        if (s[0]=='-')
        {
            V[0]=true;
            flips=1;
            nr = 1;
        }
        else
        {
            V[0]=false;
            flips=0;
            nr = 0;
        }
        long long int  i=1,j=0;
        for (i=1,j=0;i<lungime-k+1;i++)
        {
            if (i-j>=k)
            {
                if (V[j]==true)
                    flips--;
                j++;
            }
            if (s[i]=='-'&&flips%2==0)
            {
                V[i]=true;
                nr++;
                flips++;
            }
            if (s[i]=='+'&&flips%2==1)
            {
                V[i]=true;
                nr++;
                flips++;
            }
        }
        ok = true;
        for ( i = lungime-k+1;i<lungime;i++)
        {
            if (i-j>=k)
            {
                if (V[j]==true)
                    flips--;
                j++;
            }
            if (s[i]=='-'&&flips%2==0)
                ok = false;
            if (s[i]=='+'&&flips%2==1)
                ok = false;
        }
     /*   for ( i = 0;i<lungime;i++)
        {
            cout<<V[i];
        }*/
        if (ok)
            cout<<"case #"<<test<<": "<<nr<<'\n';
        else
            cout<<"case #"<<test<<": "<<"IMPOSSIBLE\n";
    }
}
