
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#define pb push_back
#define mk make_pair
#define F first
#define S second
#define pi 3.1415926535

#define MOD (1000000007)
using namespace std;
vector<pair <long long,long long> > v;
vector<long long> rs;
int main(void)
{
    ifstream infile;
    infile.open("in.txt");
    
    ofstream outfile;
    outfile.open("out.txt");
    
    int t,n,k,cnt,cc=1;
    long long h,r,ans,tmp;
    infile >> t;
    bool flag;
    double d;
    //cout<<t<<endl;
    while(t--)
    {
        infile>>n>>k;
       // cout<<n<<" "<<k<<endl;
        v.clear();
        rs.clear();
        ans=0;
        for(int i=0;i<n;i++)
        {
            infile>>r>>h;
            v.pb(mk(r*h,r));
           // cout<<r<<" "<<h<<endl;
            rs.pb(r);
        }
        sort(v.rbegin(),v.rend());
        sort(rs.begin(),rs.end());
        //int i;
        for(int j=k-1;j<n;j++)
        {
            tmp=0;
            cnt=0;
            flag=false;
            for(int i=0;i<n;i++)
            {
                if(v[i].S<=rs[j])
                {
                    if(cnt==k-1 && !flag)
                        break;
                    if(cnt==k)
                        break;
                    tmp+=v[i].F;
                    cnt++;
                    if(v[i].S==rs[j])
                        flag=true;
                }
            }
            //cout<<tmp<<endl;
                if(!flag)
                {
                    for(int i=0;i<n;i++)
                    {
                        if(v[i].S==rs[j])
                        {  tmp+=v[i].F;
                            break;
                        }
                    }
                }
                
                tmp*=2;
                //cout<<tmp<<endl;
                tmp+=rs[j]*rs[j];
               // cout<<tmp<<" r="<<rs[j]<<endl;
                ans=max(ans,tmp);
                
            }
        
            d=pi*ans;
        //outfile<<"Case #"<<cc++<<": "<<d<<endl;
        //cout<<"Case #"<<cc<<": "<<d<<endl;
        printf("Case #%d: %.8lf\n",cc++,d);
    }

    
    outfile.close();
    infile.close();
}