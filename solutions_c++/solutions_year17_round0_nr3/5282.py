// ... copyright @ASHISH JHA ... _/\_******
/*Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
  Ashish_Jha wrote this file. As long as you retain this notice you
  can do whatever you want with this stuff. If we meet some day, and you think
  this stuff is worth it, you can buy me a beer or coffee in return
*/
#include<bits/stdc++.h>
#include<fstream>
using namespace std;
typedef long long int ll;
#define MOD 1000000007
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<ll,pair<ll,ll>>
#define psi pair<string,ll>
#define INF 1000000000

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

    ll t;
    cin>>t;
    for(ll i=1;i<=t;++i)
    {
        ll n, k;
        cin>>n>>k;
        cout<<"Case #"<<i<<": ";


            priority_queue<ll>queu;
            queu.push(n);
            ll c=0,p=0;
            while(!queu.empty())
            {
                ll rep=queu.top();
                if(rep<=1)
            break;
                queu.pop();
                c++;
                if(c==k)
                {
                    ll w=(rep-1)/2;
    ll e=rep-w-1;
                    cout<<max(w,e)<<" "<<min(w,e);
                    p++;
            break;
                }
                else
                {
                    ll w=(rep-1)/2;
                    ll e=rep-w-1;
        queu.push(w);
                    queu.push(e);

                }
    }
            if(p==0)
                cout<<"0 0";
             if(i!=t)
        cout<<endl;
    }

    exit(0);
}
