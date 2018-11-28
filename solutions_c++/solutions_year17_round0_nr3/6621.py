/*
deepansh_946
*/
#include<bits/stdc++.h>
#define gc getchar
#define pc putchar
#define lli long long int
#define MOD 1000000007
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define pd(x) printf("%d",x)
#define plld(x) printf("%lld",x)
#define ss(x) scanf("%s",&x)
#define ps(x) printf("%s",x)
#define code int t; cin>>t; while(t--)
#define gcd __gcd
#define INF LLONG_MAX
using namespace std;

/*
bool ans(string s,int n,int l,int j1)
{
    int i=0 , j , k , temp , temp1=0;
    int count1 = 0;
    while(i<n)
    {
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                if( i >=(n-l+1) )
                {
                    cout<<"Case #"<<j1<<": "<<"IMPOSSIBLE"<<endl;
                    temp1 = 1;
                    break;
                }
                j = i;
                while(j<i+l)
                {
                    if(s[j]=='+')
                    {
                        s[j]='-';
                    }
                    else
                    {
                        s[j]='+';
                    }
                    j++;
                }
                count1++;
            }
        }
        if(temp1==1)
        {
            break;
        }
    }
    if(temp1!=1)
    {
        cout<<"Case #"<<j1<<": "<<count1<<endl;
    }
    return false;
}
*/

int main()
{
    freopen("in.in" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int t; cin >> t;
    for(int i=1;i<=t;i++)
    {
        lli n , k;
        slld(n); slld(k);
        vector<lli> v;
        v.push_back(1);
        v.push_back(n+2);
        lli no;
        pair<lli , lli> dis;
        for(lli j=1;j<=k;j++)
        {
            no = -1;
            for(int i=1;i<v.size();i++)
            {
                if(v.at(i)-v.at(i-1) == 1)
                    continue;
                lli tmp = (v.at(i)+v.at(i-1))/2;
                pair<lli , lli> tmp1 = make_pair(tmp-v.at(i-1)-1 , v.at(i)-tmp-1);

                if(no == -1)
                {
                    no = tmp;
                    dis = tmp1;
                }
                if(v.at(i-1)%2 == v.at(i)%2)
                {
                    if( min(dis.first,dis.second) < min(tmp1.first,tmp1.second) )
                    {
                        no = tmp;
                        dis = tmp1;
                    }
                    else
                    if( min(dis.first,dis.second) == min(tmp1.first,tmp1.second) )
                    {
                        if( max(dis.first,dis.second) < max(tmp1.first,tmp1.second) )
                        {
                            no = tmp;
                            dis = tmp1;
                        }
                    }
                }
                else
                {
                    if( min(dis.first,dis.second) < min(tmp1.first,tmp1.second) )
                    {
                        no = tmp;
                        dis = tmp1;
                    }
                    else if( min(dis.first,dis.second) == min(tmp1.first,tmp1.second) )
                    {
                        if( max(dis.first,dis.second) < max(tmp1.first,tmp1.second) )
                        {
                            no = tmp;
                            dis = tmp1;
                        }
                    }
                    tmp++;
                    tmp1 = make_pair(tmp1.first+1, tmp1.second-1);
                    if( min(dis.first,dis.second) < min(tmp1.first,tmp1.second) )
                    {
                        no = tmp;
                        dis = tmp1;
                    }
                    else
                    if( min(dis.first,dis.second) == min(tmp1.first,tmp1.second) )
                    {
                        if( max(dis.first,dis.second) < max(tmp1.first,tmp1.second) )
                        {
                            no = tmp;
                            dis = tmp1;
                        }
                    }
                }
            }
            v.push_back(no);
            sort(v.begin(),v.end());
        }
        printf("Case #%d: %lld %lld\n",i,dis.second,dis.first);
    }
}
