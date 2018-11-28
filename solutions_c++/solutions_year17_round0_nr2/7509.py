#include <bits/stdc++.h>
#include <string>
using namespace std;

unsigned long long int t,x,sum,tam,atual;
bool ok=true;
string number;


int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin>>t;

    for(int z=1;z<=t;++z)
    {

        cin>>number;
        tam=number.size();  ok=true;


        for(int i=tam-1;i>0;--i)
        {

             for(int j=i;j>0;j--)
                if(number[i]<number[i-1])
                {
                    number[i-1]-=1;
                    for(int k=j;k<tam;++k)
                        number[k]='9';
                    //break;
                }

        }

        cout<<"Case #"<<z<<": ";

        bool ini=true;
        for(int i=0;i<tam;++i)
        {

            if(number[i]!='0')
             ini=false;

            if(!ini)
            {
                cout<<number[i];
            }


        }

        cout<<"\n";

    }

    return 0;
}
