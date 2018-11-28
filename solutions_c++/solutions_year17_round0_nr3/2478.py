#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#define clr(x) memset(x,0,sizeof(x))
#define LL long long
using namespace std;
vector<LL> deal[2],num[2],cd,cn;
LL log2(LL a);
LL pow2(LL a);
LL max(LL a,LL b)
{
	return a>b?a:b;
}
LL min(LL a,LL b)
{
	return a<b?a:b;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c.out","w",stdout);
	int T;
	LL n,m,k,l,ct,maxn,minn;
	int p,q,size;
	scanf("%d",&T);
	for(int kase=1;kase<=T;kase++)
	{
		scanf("%lld%lld",&n,&k);
		l=log2(k+1);
		deal[l%2].erase(deal[l%2].begin(),deal[l%2].end());
		num[l%2].erase(num[l%2].begin(),num[l%2].end());
		deal[l%2].push_back(n);
		num[l%2].push_back(1);
		ct=k+1-pow2(l);
		maxn=0;
		minn=n;
		while(l)
		{
			p=l%2;
			q=1-p;
			deal[q].erase(deal[q].begin(),deal[q].end());
			num[q].erase(num[q].begin(),num[q].end());
			cd.erase(cd.begin(),cd.end());
			cn.erase(cn.begin(),cn.end());
			for(int i=0;i<deal[p].size();i++)
			{
				if(deal[p][i]%2==0)
				{
					cd.push_back(deal[p][i]/2-1);
					cd.push_back(deal[p][i]/2);
					cn.push_back(num[p][i]);
					cn.push_back(num[p][i]);
				}
				else
				{
					cd.push_back(deal[p][i]/2);
					cn.push_back(2*num[p][i]);
				}
			}
			size=1;
			deal[q].push_back(cd[0]);
			num[q].push_back(cn[0]);
			for(int i=1;i<cd.size();i++)
				if(cd[i]!=cd[i-1])
				{
					deal[q].push_back(cd[i]);
					num[q].push_back(cn[i]);
					size++;
				}
				else
				{
					num[q][size-1]+=cn[i];
				}
//			for(int i=0;i<cd.size();i++)
//				 cout<<cd[i]<<" "<<cn[i]<<" "<<endl;
//            cout<<endl;
			l--;
		}
		if(ct>0)
            for(int i=deal[0].size()-1;i>=0;i--)
            {
 //       		    cout<<deal[0][i]<<" "<<num[0][i]<<" "<<ct<<" "<<endl;
                ct=ct-num[0][i];
//                cout<<ct<<endl;
                if(ct<=0)
                {
                    if(deal[0][i]%2==0)
                    {
                        maxn=deal[0][i]/2;
                        minn=deal[0][i]/2-1;
                    }
                    else
                    {
                        maxn=minn=deal[0][i]/2;
                    }
                    break;
                }
            }
		else
        {
                if(deal[1][0]%2==0)
                {
                    maxn=deal[1][0]/2;
                    minn=deal[1][0]/2-1;
                }
                else
                {
                    maxn=minn=deal[1][0]/2;
                }
        }
		printf("Case #%d: %lld %lld\n",kase,maxn,minn);
	}
	return 0;
}
LL log2(LL a)
{
	LL ans=-1;
	while(a)
	{
		a/=2;
		ans++;
	}
	return ans;
}
LL pow2(LL a)
{
    LL ans=1;
    while(a--)
    {
        ans*=2;
    }
    return ans;
}
