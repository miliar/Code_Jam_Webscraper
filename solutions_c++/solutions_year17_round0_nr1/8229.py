#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#define INF 0x3ffffff

char cake[1005];
bool tt[1005];
int maxm,tot;
int K;
using namespace std;

void op(int p){
    for(int i=0;i<K;i++){
        tt[i+p] ^= 1;
    }
}

int solve(int fi,string c)
{
    for(int i=1;i<=c.length();i++)
        if(c[i-1]=='-')
            tt[i] = 1;
        else
            tt[i] = 0;

    if(fi) op(1);
    tot = fi;
    for(int i=2;i<=c.length()-K+1;i++)
        if(tt[i]){
            op(i);  tot++;
        }
    for(int i=1;i<=c.length();i++)
        if(tt[i])  return INF;
    return tot;
}

int main()
{
	//freopen("in","r",stdin);
	//freopen("result","w",stdout);
    string c;
    int cases;
    cin>>cases;
    for(int i=1;i<=cases;i++)
    {
        cin>>c>>K;
        int minum = min(solve(1,c),solve(0,c));
        cout<<"Case #"<<i<<": ";
        if(minum==INF)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<minum<<endl;
    }
}
