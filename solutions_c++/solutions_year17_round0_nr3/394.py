 
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

long long int max(long long int a,long long int b){return a>b?a:b;};
long long int min(long long int a,long long int b){return a<b?a:b;};

int main()
{
    int t;
    vector<long long int> v;
    scanf("%d",&t);
    
    for(int _=1;_<=t;_++)
    {
        long long int n,k;
        scanf("%lld %lld",&n,&k);
        
        v.clear();
        v.push_back(1); v.push_back(n+2);
        
        long long int num;
        pair<long long int,long long int> dist;
        
        for(long long int j=1;j<=k;j++)
        {
            num = -1;
            for(int i=1;i<v.size();i++)
            {
                if(v.at(i)-v.at(i-1) == 1) continue;
                
                long long int tmpnum = (v.at(i-1)+v.at(i))/2;;
                pair<long long int,long long int> tmpdist = make_pair(tmpnum-v.at(i-1)-1,v.at(i)-tmpnum-1);
                
                if(num == -1)
                {
                    num = tmpnum;
                    dist = tmpdist;
                }
                
                if(v.at(i-1)%2 == v.at(i)%2)
                {
                    if( min(dist.first,dist.second) < min(tmpdist.first,tmpdist.second) )
                    {
                        num = tmpnum;
                        dist = tmpdist;
                    }
                    else if( min(dist.first,dist.second) == min(tmpdist.first,tmpdist.second) )
                    {
                        if( max(dist.first,dist.second) < max(tmpdist.first,tmpdist.second) )
                        {
                            num = tmpnum;
                            dist = tmpdist;
                        }
                    }
                }
                else
                {
                    if( min(dist.first,dist.second) < min(tmpdist.first,tmpdist.second) )
                    {
                        num = tmpnum;
                        dist = tmpdist;
                    }
                    else if( min(dist.first,dist.second) == min(tmpdist.first,tmpdist.second) )
                    {
                        if( max(dist.first,dist.second) < max(tmpdist.first,tmpdist.second) )
                        {
                            num = tmpnum;
                            dist = tmpdist;
                        }
                    }
                    
                    tmpnum++;
                    tmpdist = make_pair(tmpdist.first+1, tmpdist.second-1);
                    
                    if( min(dist.first,dist.second) < min(tmpdist.first,tmpdist.second) )
                    {
                        num = tmpnum;
                        dist = tmpdist;
                    }
                    else if( min(dist.first,dist.second) == min(tmpdist.first,tmpdist.second) )
                    {
                        if( max(dist.first,dist.second) < max(tmpdist.first,tmpdist.second) )
                        {
                            num = tmpnum;
                            dist = tmpdist;
                        }
                    }
                }
            }
            v.push_back(num);
            sort(v.begin(),v.end());
        }
        printf("Case #%d: %lld %lld\n",_,dist.second,dist.first);
    }
}
 
