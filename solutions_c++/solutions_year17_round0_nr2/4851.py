#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;
ll arr[100100],t,k,n,ans,indexi;
/*bool check(ll num)
{
    vector<ll> v;
    v.clear();
    ll temp=num;
    while(temp>=0)
    {
        v.pb(temp%10);
        temp/=10;
    }
    for(int i=0;i<v.size()-1;i++)
    {
        if(v[i]>=v[i+1]){}
        else
            return false;
    }
    return true;
}*/
string str;
int main()
{
    freopen("input1codejam.in","r",stdin);
    freopen("output1codejam.out","w",stdout);
    cin>>t;
    for(int j=1;j<=t;j++){
        cin>>str;
        n=str.length();
        while(1){
            indexi=INT_MIN;
            for(int i=0;i<n-1;i++){
                if(str[i]>str[i+1]){
                    str[i]--;
                    indexi=i+1;
                    break;
                }
            }
            if(indexi==INT_MIN)//This means that the string is already in its right phase
                break;
            while(indexi<n)//for some particular cases
				str[indexi++]='9';
        }
        ans=upper_bound(str.begin(),str.end(),'0')-str.begin();
		cout<<"Case #"<<j<<": ";
		while(ans<str.size()){
            cout<<str[ans];
            ans++;
        }
		cout<<endl;
    }
return 0;
}
