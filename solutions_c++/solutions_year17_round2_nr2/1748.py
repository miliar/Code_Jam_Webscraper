#include <bits/stdc++.h>
using namespace std;

ifstream be ("Stable Neigh-borsin.txt");
ofstream ki ("Stable Neigh-borsout.txt");

long long t;
vector<string> megoldas;

void process()
{
    int n;
    int r,o,y,g,b,v;
    be>>n>>r>>o>>y>>g>>b>>v;
    int db=n;
    bool mehetmeg=true;
    char akt;
    string order="";
    if(v!=0) akt='V';
    else if(g!=0) akt='G';
    else if(o!=0) akt='O';
    else if(y!=0) akt='Y';
    else if(b!=0) akt='B';
    else akt='R';
    char start=akt;
    while(db>0 && mehetmeg)
    {
        //cout<<akt<<" ";
        order+=akt;
        if(akt=='R')
        {
            r-=1;
            if(g==0 && y==0 && b==0) mehetmeg=false;
            else if(g>0) akt='G';
            else if(y>b || (y==b && start=='Y')) akt='Y';
            else akt='B';

        }
        else if(akt=='B')
        {
            b-=1;
            if(o==0 && y==0 && r==0) mehetmeg=false;
            else if(o>0) akt='O';
            else if(y>r || (y==r && start=='Y')) akt='Y';
            else akt='R';
        }
        else if(akt=='Y')
        {
            y-=1;
            if(v==0 && r==0 && b==0) mehetmeg=false;
            else if(v>0) akt='V';
            else if(r>b || (r==b && start=='R')) akt='R';
            else akt='B';
        }
        else if(akt=='O')
        {
            o-=1;
            if(b>0) akt='B';
            else mehetmeg=false;
        }
        else if(akt=='G')
        {
            g-=1;
            if(r>0) akt='R';
            else mehetmeg=false;
        }
        else //if(akt=='v')
        {
            v-=1;
            if(y>0) akt='Y';
            else mehetmeg=false;
        }
        db-=1;
    }
    if(db==0 && order[0]!=order[order.length()-1]) megoldas.push_back(order);
    else megoldas.push_back("IMPOSSIBLE");
    //cout<<endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    be>>t;
    for(long long i=1;i<=t;i++) process();
    for(long long i=0;i<megoldas.size();i++)
    {
        ki<<setprecision(7)<<fixed<<"Case #"<<i+1<<": "<<megoldas[i]<<endl;
    }
    return 0;
}
