#include<bits/stdc++.h>
using namespace std;
long long int Pow[20];
long long int f(long long int n)
{
    if(n==0) return 0;
    int l=0;
    long long int m=n;
    while(m>=10)
    {
        m=m/10 ;
        l++;
    }
    if(m*((Pow[l+1]-1)/9) > n)
    {
        return m*Pow[l]-1;
    }
    else return m*Pow[l] + f(n-m*Pow[l]);
}
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;
    Pow[0]=1;
    for(int u=1 ; u<=18 ; u++) Pow[u]=10*Pow[u-1];
    for(int i=1 ; i<=T ; i++)
    {
        fout << "Case #" << i << ": " ;
        long long int n;
        fin >> n;
        fout << f(n) << "\n";
    }
}
