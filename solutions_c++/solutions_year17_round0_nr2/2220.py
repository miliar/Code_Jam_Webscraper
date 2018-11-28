#include <bits/stdc++.h>
#define INF 1000000009
#define mod 1000000007
#define PI 3.14159
#define vi vector<int>
#define ll long long
#define ii pair<int, int>
#define pll pair<ll, ll>
#define vii vector<ii>
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define mt make_tuple
#define eb emplace_back
#define CLR(arr) memset(arr, 0, sizeof(arr))
#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int ctr=1; ctr<=T; ++ctr)
    {
        vi num;
        ll N;
        cin>>N;
        while(N)
        {
            num.pb(N%10);
            N /= 10;
        }
        for(int i=1; i<(int)num.size(); ++i)
        {
            if(num[i] > num[i-1])
            {
                num[i]--;
                for(int j=0; j<i; ++j)
                    num[j] = 9;
            }
        }

        cout<<"Case #"<<ctr<<": ";
        int i = num.size()-1;
        while(num[i]==0)
            --i;
        while(i>=0)
            cout<<num[i--];
        cout<<endl;
    }
    return 0;
}
