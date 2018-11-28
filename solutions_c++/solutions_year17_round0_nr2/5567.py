#include <iostream>
#include <fstream>
#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <cmath>

#define MN 1000010
#define INF 2147483647
#define PI 3.14159265359
#define pairr pair<int, int>
#define pairrr pair<int, pairr>
#define f first
#define s second
#define pb push_back
#define ll long long
#define MOD 10000007
#define IO ios_base::sync_with_stdio(false); cin.tie();
#define PQT pairr
#define PQL priority_queue<PQT, vector<PQT>, less<PQT> >
#define PQG priority_queue<PQT, vector<PQT>, greater<PQT> >

using namespace std;

string s;
int t,k,i,j,t1,ans;

int ch(string s)
{
    for (i=1;i<s.length();i++)
    {
        if (s[i]<s[i-1])
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    IO
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t1;
    for (t=1;t<=t1;t++)
    {
        cin>>s;
        k=ch(s);
        j=s.length()-1;
        while (!k)
        {
            s[j]='9';
            j--;
            if (s[j]==0) continue;
            s[j]--;
            k=ch(s);
        }
        cout<<"Case #"<<t<<": ";
        i=0;
        while (s[i]=='0') i++;
        for (;i<s.length();i++) cout<<s[i];cout<<endl;
    }
    return 0;
}
