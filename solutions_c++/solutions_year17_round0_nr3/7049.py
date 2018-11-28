#include <iostream>
#include <fstream>
#include <deque>

#define ull long long
#define inf 99999999999999999
using namespace std;

ifstream fin("file.in");
ofstream fout("file.out");

int t;
ull n,k;
ull ls,rs,minVal,maxVal,pos;

deque<ull>q;

ull minimum(ull a, ull b)
{
    if(a<b)
        return a;
    return b;
}

ull mmaximum(ull a, ull b)
{
    if(a<b)
        return b;
    return a;
}

ull bin_search(ull pos, ull f, ull l)
{
    while(f<=l)
    {
        ull m=(f+l)/2;

        if(pos<q[m])
        {
            l=m-1;
        }
        else if(pos>q[m])
        {
            f=m+1;
        }
        else
            return m;
    }
    return f;
}


void computeStall(ull i)
{
    ull l,r,mini,maxi;
    ull mid=(q[i+1]+q[i])/2;
   // cout<<q[i]<<' '<<q[i+1]<<endl;
    ls=mid-q[i]-1;
    rs=q[i+1]-mid-1;

    if(ls<rs)
    {
        mini=ls;
        maxi=rs;
    }
    else
    {
        mini=rs;
        maxi=ls;
    }

    if(mini>minVal)
    {
        minVal=mini;
        maxVal=maxi;

        pos=mid;
    }
    else if(mini==minVal)
    {
        if(maxi>maxVal)
        {
            maxVal=maxi;
            pos=mid;
        }
    }
}

void getBest()
{
    ull stop=q.size()-2;

    for(ull i=0; i<=stop; i++)
    {
        computeStall(i);
    }

    ull qPos=bin_search(pos,0, q.size()-1);
    q.insert(q.begin()+qPos, pos);
}

void display(ull minVal, ull maxVal, int caseN)
{
    cout<<"Case #"<<caseN<<": "<<maxVal<<' '<<minVal<<'\n';
}

void solve(int caseN)
{
    q.clear();
    q.push_front(0);
    q.push_back(n+1);

    while(k>=1)
    {
        minVal=-1;
        maxVal=-1;

        getBest();

        k--;
    }

    display(minVal, maxVal, caseN);

}

void read()
{
    cin>>t;

    for(int i=1; i<=t; i++)
    {
        cin>>n>>k;

        solve(i);
    }
}

int main()
{
    read();

    return 0;
}
