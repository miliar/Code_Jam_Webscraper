#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream inp;
    ofstream out;
    inp.open("input.txt");
    out.open("output.txt");
    int t,sz;
    string n;
    inp>>t;
    for(int T=1;T<=t;T++)
    {
        inp>>n;
        out<<"Case #"<<T<<": ";
        int i=0;
        sz = n.size();
        while(i<sz-1 && n[i]<=n[i+1])
        {
            i++;
        }
        if(i==sz-1)
        {
            out<<n<<endl;
            continue;
        }
        while(i>0 && n[i]==n[i-1])
            i--;
        if(sz>1)
            n[i]=n[i]-1;
        for(int j=i+1;j<sz;j++)
            n[j]='9';
        if(sz>1 && n[0]=='0')
        {
            n = n.substr(1);
        }
        out<<n<<endl;
    }
    return 0;
}
