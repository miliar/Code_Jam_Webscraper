#include <bits/stdc++.h>
using namespace std;
#define ll long long
ll comp(int size,int y)
{
    ll ans=0;
    for(int i=0;i<size;i++)
    {
        ans+=pow(10,i)*y;
    }
    return ans;
}
ll comp2(int a,int arr1[],int size)
{
    ll ans=0;
    int beg=size-a;
    int j=a-1;
    for(int i=beg;i<size;i++)
    {
        ans+=pow(10,j)*arr1[i];
        j--;
    }
    return ans;
}
int main() {
    ll t;
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("out.txt","w",stdout);
    cin>>t;
    int h=1;
    while(t--)
    {
        ll n;
        cin>>n;
        int i=0;
        int arr[19]={-1};
        while(n)
        {
            arr[i]=n%10;
            n=n/10;
            i++;
        }
        int size=i;
        int act[size];
        for(i=size-1;i>=0;i--)
        {
            act[size-i-1]=arr[i];
        }
        //for(i=0;i<size;i++)
        //cout<<act[i]<<endl;
        vector<int> res;
        int j=0;
        int str=0;
        for(i=size;i>=1;i--)
        {//cout<<comp2(i,act,size)<<endl;

            if(comp2(i,act,size)>=comp(i,act[j]))
            {
                res.push_back(act[j]);
                j++;
            }
            else
            {
                if(act[j]!=1)
                res.push_back(act[j]-1);
                str=i-1;
                break;
            }
        }
        for(i=0;i<str;i++)
        res.push_back(9);
        ll ans=0;
        for(i=0;i<res.size();i++)
        {
            ans+=pow(10,res.size()-i-1)*res[i];
        }
	cout<<"Case #"<<h<<": "<<ans<<endl;
        h++;
    }
	// your code goes here
	return 0;
}


