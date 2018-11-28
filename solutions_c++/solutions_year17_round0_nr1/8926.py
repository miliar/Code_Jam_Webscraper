#include <bits/stdc++.h>
using namespace std;

//--------------------------------------------------------------------//
#define ll long long int
#define ull unsigned long long int
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define fr(t,i,x) for(int i=t; i<x; ++i) // t = start index
#define mod 1000000007
#define endl "\n"
#define output freopen("output.txt","w", stdout)
#define input freopen("input.txt","r", stdin)
//--------------------------------------------------------------------//

int main() 
{
    //clock_t tstart = clock();
    //output;
    //input;
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int test;
    cin>>test;
    fr(0,t,test)
    {
        bool pos=true;
        ll k, tally=0;
        string s;
        cin>>s;
        cin>>k; 
        fr(0,i,s.length())
        {
            if(s[i]=='-')
            {
                tally++;
                if((i+k) > s.length()){
                    pos=false;
                    break;
                }
                for(int j=i; j<(i+k); j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
            //cout<<s<<endl;
        }
        if(pos==true)
            cout<<"Case #"<<t+1<<": "<<tally<<endl;
        else
            cout<<"Case #"<<t+1<<": IMPOSSIBLE"<<endl;
        //cout<<s<<endl;
    }

    //cout<<"\nTotal Time Taken : "<<(double)(-tstart + clock())/CLOCKS_PER_SEC<<"sec\n";
    return 0;
}