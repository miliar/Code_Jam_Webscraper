#include <bits/stdc++.h>
using namespace std;

string pancake;
int n,k,cont;
bool impossible;

void trade(int i)
{

    if(pancake[i]=='+') pancake[i]='-';
    else pancake[i]='+';

    return ;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin>>n;

    for(int z=1;z<=n;++z)
    {
        impossible=false; cont=0;
        cin>>pancake>>k;

        for(int i=0;i<pancake.size()-k+1;++i)
        {
            if(pancake[i]=='-' )
            {
                for(int j=0;j<k;++j)
                    trade(i+j);
                cont++;
            }

        }

        for(int i=pancake.size()-k;i<pancake.size();++i)
        {
            if(pancake[i]=='-'){impossible=true; break;}
        }

        if(!impossible)
            cout<<"Case #"<<z<<": "<<cont<<'\n';
        else
            cout<<"Case #"<<z<<": IMPOSSIBLE\n";

    }

    return 0;
}
