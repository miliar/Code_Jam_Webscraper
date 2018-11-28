#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
{
    FILE *fin = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/0B/B-large.in", "r", stdin);
	FILE *fout = freopen("C:/Users/trigfan/Desktop/GoogleCodeJam/0B/B-large.out", "w", stdout);
    long long p[20];
    p[0]=1;
    for(int i=1; i<20; i++)
        p[i]=10*p[i-1];
    int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
    long long N;
    cin>>N;
    long long M=N;
    int dig[20];
    int L=0;
    for(int i=0; i<20; i++)
    {
        dig[i]=N%10;
        if (dig[i]>0)
            L=i+1;
        N=N-dig[i];
        N=N/10;
    }
    int l=L-1,r=-1;
    long long ans=0;
    for(int i=L-1; i>=0; i--)
    {
        if(i>0)
        {
            if(dig[i]>dig[i-1])
            {
                r=i;
                break;
            }
            if(dig[i]<dig[i-1])
                l=i-1;
        }
    }
    for(int i=l+1; i<L; i++)
        ans+=dig[i]*p[i];
    for(int i=0; i<l; i++)
        ans+=9*p[i];
    ans+=(dig[l]-1)*p[l];
    if(r==-1)
        ans=M;
    cout << "Case #" << t << ": ";
    cout<<ans<<endl;
	}
    return 0;
}
