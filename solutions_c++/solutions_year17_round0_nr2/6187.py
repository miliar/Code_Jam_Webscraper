#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <ctype.h>

using namespace std;

#define ll long long
#define fo(n) for(int i=0;i<n;i++)
#define pb push_back
#define be v.begin()
#define en v.end()
#define mt make_tuple
#define fot(n,k) for(int k=0;k<n;k++)

int main()
{
    int t;
    cin >> t;
    fo(t)
    {
        string a,b="";
        int pr=0,gr=0,pot=0;
        cin >> a;
       // cout << a <<'\n';
        //cout << "es";
        for(int j=0;j<a.size();j++)
        {
            if(j<a.size()-1)
            {
                if(pot==1)
                {
                    //b.pb(9);
                    break;
                }
                
                if((int)(a[j]-'0')<=(int)(a[j+1]-'0'))
                    b.pb(a[j]);
                else if(a[j]!='1')
                {
                    if(j!=0)
                    {
                        if(a[j]-'0'==a[j-1]-'0')
                        {a[j]=a[j]-1;
                        j=-1;
                        b="";
                        continue;}
                    }
                    b.pb(a[j]-1);
                    gr=j;
                    pot=1;
                    
                }
                else
                {
                    b[j]=9;pr=1;break;
                    
                }
            }
            else if(pot==1)
            {
               // b[j]=9;
               break;
            }
            else
            {
                b.pb(a[j]);
            }
        }
        cout <<"Case #"<< i+1<<": ";
        if(pr==1)
        {
            fot(a.size()-1,k)
            {
                cout << "9";
            }
            cout <<"\n";
        }
        else
        {
            cout << b ;
            if(pot)
            {
                for(int ke=0;ke<a.size()-gr-1;ke++)
                cout << "9";
            }
            cout << '\n';
        }
    }
    return 0;
}