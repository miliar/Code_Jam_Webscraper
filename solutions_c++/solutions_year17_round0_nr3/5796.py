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

#define CTC(i) SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), i);
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

int t,t1,n,k,i,j,l,r,al,ar,ai,a[1010];

int main()
{
    IO
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t1;
    for (t=1;t<=t1;t++)
    {
        cin>>n>>k;
        for (i=1;i<=n;i++) a[i]=0;
        a[0]=1;
        a[n+1]=1;
        while (k--)
        {
            al=-1;
            ar=-1;
            for (i=1;i<=n;i++)
            {
                if (a[i]==1) continue;
                l=0;
                r=0;
                j=i-1;
                while (a[j]==0 && j>0)
                {
                    l++;
                    j--;
                }
                j=i+1;
                while (a[j]==0 && j<=n)
                {
                    r++;
                    j++;
                }
                if (min(l,r)>min(al,ar))
                {
                    al=l;
                    ar=r;
                    ai=i;
                }
                else
                if (min(l,r)==min(al,ar))
                {
                    if (max(l,r)>max(al,ar))
                    {
                        al=l;
                        ar=r;
                        ai=i;
                    }
                }
            }
            a[ai]=1;
        }
        cout<<"Case #"<<t<<": "<<max(al,ar)<<" "<<min(al,ar)<<endl;
    }
    return 0;
}
