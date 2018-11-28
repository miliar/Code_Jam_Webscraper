#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#include<map>
#define cin ifile
#define cout ofile

using namespace std;


int main()
{
    ifstream ifile("C-large.in");
    ofstream ofile("out1.txt");
    int t;
    cin>>t;

    for(int fff=1;fff<=t;fff++)
    {
            long long n,k,ans1=0,ans2=0;
            cin>>n>>k;
            map<long long ,long long > mp;
            mp[n]=1;
            k--;
            while(!mp.empty())
            {
                long long a=(mp.rbegin())->first;
                //cout<<a<<" "<<mp[a]<<"\n";
                if(mp[a]<=k)
                {
                    long long b=a/2;
                    long long c=a-b-1;
                    if(b>0)
                    {
                        mp[b]+=mp[a];
                    }
                    if(c>0)
                    {
                        mp[c]+=mp[a];
                    }
                    k-=mp[a];
                    mp.erase(a);
                }
                else
                {
                   // cout<<"&&";
                    long long b=(mp.begin())->first;
                    ans1=max(a/2,a-a/2-1);
                    ans2=min(a/2,a-a/2-1);
                    break;
                }
               // cout<<k<<"\n";
            }
             cout<<"Case #"<<fff<<": "<<ans1<<" "<<ans2<<"\n";
    }
    return 0;
}
