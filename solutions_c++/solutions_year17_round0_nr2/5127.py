#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
unsigned long long getNum(vector<int>&ans,int l)
{
    unsigned long long p=1,r=0;
    for(int i=l-1;i>=0;i--)
    {
        r+=p*ans[i];
        p*=10;
    }
    return r;
}

bool recAns(vector<int>&ans, vector<int> &num,int pos,int prev)
{
    //printf("pos==%d prev==%d ans==%I64d, num==%I64d\n",pos,prev,getNum(ans,pos),getNum(num,pos));
    if(getNum(ans,pos)>getNum(num,pos)){return false;}
    if(pos==num.size())
    {
        //printf("hhpos==%d prev==%d ans==%I64d, num==%I64d\n",pos,prev,getNum(ans,pos),getNum(num,pos));
        if(getNum(ans,ans.size())<=getNum(num,ans.size()))return true;
        return false;
    }
    //printf("max=%d\n",max(num[pos],prev));
    for(int i=9;i>=prev;i--)
    {
        ans[pos]=i;
        if(recAns(ans,num,pos+1,i))
        {
            return true;
        }
    }
    return false;
}

bool isTidy(unsigned long long n)
{
    unsigned long long _n=n;
    int dig=10;
    while(dig>=_n%10&&_n>0)
    {
                dig=_n%10;
                _n/=10;
    }
    return(_n==0);
}
vector<int> rev(vector<int>&num)
{
    vector<int>ans;
    for(int i=0;i<num.size();i++)
    {
        ans.push_back(num[num.size()-i-1]);
    }
    return ans;
}

unsigned long long getRes(unsigned long long n)
{
    if(isTidy(n))return n;
    vector<int>ans;
    vector<int>num;
    unsigned long long _n=n;
    while(_n>0)
    {
        num.push_back(_n%10);
        ans.push_back(0);
        _n/=10;
    }
    num=rev(num);
    //printf("num.size()=%d ans.size()=%d num=%I64d\n",num.size(),ans.size(),getNum(num,num.size()));
    recAns(ans,num,0,0);
    return getNum(ans,ans.size());
}

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    int t;
    cin>>t;
    int j=1;
    while(t)
    {
        unsigned long long n;
        cin>>n;
        unsigned long long p=1,r=0;
        unsigned long long _n=n,tRes=0,res;
        /*if(n/10==0)
        {
            printf("Case %d: %I64d\n",j,n);
            t--;
            j++;
            continue;
        }*/
        while(_n)
        {
            _n/=10;
            r+=p;
            tRes+=p*9;
            p*=10;
        }
        //printf("p==%I64d\n",r);
        if(r<n)
        {
            res=getRes(n);
        }
        else
        {
            if(r==n)
            {
                res=n;
            }
            else
            {
                res=tRes/10;
            }
        }
        printf("Case #%d: %I64d\n",j,res);
        t--;
        j++;
    }
    return 0;
}
