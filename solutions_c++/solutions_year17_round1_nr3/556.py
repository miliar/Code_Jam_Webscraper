#include <bits/stdc++.h>

using namespace std;

typedef pair<int, pair<int, pair<int, pair<int, pair<int, int> > > > > p;
#define mp(a,b,c,d, e, f) make_pair(a, make_pair(b, make_pair(c,make_pair(d, make_pair(e, f)))))

int mem[101][101][101][101][2];

void solve()
{
    int hd, ad, hk, ak, b, d, ch, f = 0, turn = 0, last;
    cin>>hd>>ad>>hk>>ak>>b>>d;
    ch = hd;
    queue<p> fila;
    fila.push(mp(-hk, 0, ad, hd, ak, 0));
    memset(mem, 0, sizeof(mem));
    while(!fila.empty())
    {
        p atual = fila.front();
        fila.pop();
        hk = -atual.first;
        turn = -atual.second.first;
        ad = atual.second.second.first;
        ch = atual.second.second.second.first;
        ak = atual.second.second.second.second.first;
        last = atual.second.second.second.second.second;
        if(hk<=0)
        {
            //cout<<"T:"<<turn<<" HK:"<<hk<<" CH:"<<ch<<" AD:"<<ad<<" AK:"<<ak<<" L:"<<last<<endl;
            f = 1;
            break;
        }
        if(mem[hk][ad][ch][ak][last]==1)
            continue;
        mem[hk][ad][ch][ak][last]=1;
        //cout<<"T:"<<turn<<" HK:"<<hk<<" CH:"<<ch<<" AD:"<<ad<<" AK:"<<ak<<" L:"<<last<<endl;
        if(ch-ak>0 || hk-ad<=0)
        {
            //ataque
            fila.push(mp(-hk+ad, -turn-1, ad, ch-ak, ak, 0));
        }
        if(ch-ak>0 && b>0)
        {
            //buff
            fila.push(mp(-hk, -turn-1, ad+b, ch-ak, ak, 0));
        }
        if(ch-ak+d>0 && d>0)
        {
            //debuff
            fila.push(mp(-hk, -turn-1, ad, ch-ak+d, ak-d, 0));
        }
        if(last!=4 && hd-ak>0)
        {
            //heal
            fila.push(mp(-hk, -turn-1, ad, hd-ak, ak, 1));
        }
    }
    if(f==0)
        cout<<"IMPOSSIBLE";
    else
        cout<<turn;
}

int main()
{
    int t, i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }
    return 0;
}
