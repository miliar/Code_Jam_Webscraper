#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<ll,ll> lll;
lll f(long long int n , long long int k)
{
    if(k==1)
    {
        lll x;
        if((n%2)==1)
        {
            x.first = n/2;
            x.second = n/2;
        }
        else
        {
            x.first = (n-1)/2;
            x.second = n/2;
        }
        return x;
    }
    if(n==1 || (n==2 && k==2)){
        lll x;
        x.first=0;
        x.second=0;
        return x;
    }
    if((n%2)==1) return f(n/2 , k/2);
    else
    {
        if((k%2)==0) return f(n/2 , k/2);
        else return f((n-1)/2 , (k-1)/2);
    }
}
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    for(int i=1 ; i<=T ; i++)
    {
        fout << "Case #" << i << ": " ;
        long long int n,k;
        fin >> n >> k;
        lll x = f(n,k);
        fout << x.second << " " << x.first << "\n";
    }
}
