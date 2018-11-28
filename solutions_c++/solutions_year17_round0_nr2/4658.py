#include <bits/stdc++.h>

using namespace std;

string solve(string x) {
    int st=0;
    string y="";
    while (x[st] == '0') st++;
    while (st < x.size()) y+=x[st],st++;
    x=y;
    sort(y.begin(),y.end());
    if (x == y) return x;
    for (int i=0;i<x.size();i++)
        if (x[i] > x[i+1]) {
                x[i]--;
                for (int j=i+1;j<x.size();j++)
                    x[j]='9';
                return solve(x);
    }
    return "12";
}

string n;
int t;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("Blarge.out","w",stdout);
    cin>>t;
    for (int t1=1;t1<=t;t1++) {
        cin>>n;
        cout<<"Case #"<<t1<<": ";
        cout<<solve(n)<<endl;
    }
}
