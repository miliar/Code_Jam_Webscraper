
#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
using namespace std;

typedef vector<int> vi;
typedef long long int lli;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef pair<int, char> pic;

//small test case
void foo()
{
    int n;
    cin>>n;

    int f[6];
    int i;
    
    for(i=0;i<6;i++)
      cin>>f[i];


    vector<pic> tmp;
    tmp.pb(mp(f[0],'R'));
    tmp.pb(mp(f[2],'Y'));
    tmp.pb(mp(f[4],'B'));

    sort(tmp.rbegin(),tmp.rend());
    if(tmp[0].first>(tmp[1].first  + tmp[2].first))
    {
        cout<<"IMPOSSIBLE"<<endl;
        return;
    }
    int len=3*(tmp[0].first);
    vector<char> v(len, 'x');

    ///first fill the biggest one
    int pos =0;
    for(i=0;i<tmp[0].first;i++)
    {
        v[pos]=tmp[0].second;
        pos+=3;
    }


    //second largest
    pos = 1;
    for(i=0;i<tmp[1].first;i++)
    {
        v[pos]=tmp[1].second;
        pos+=3;
    }


    //smallest
    pos = len-1;
    for(i=0;i<tmp[2].first;i++)
    {
        v[pos]=tmp[2].second;
        pos-=3;
    }

    for(i=0;i<len;i++)
    {
        if(v[i]!='x')
          cout<<v[i];
    }

    cout<<endl;


}


int main()
{
    int t;
    cin>>t;
    int i;
    for(i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        foo();
    }

}
