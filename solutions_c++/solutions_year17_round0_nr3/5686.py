#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
typedef long long int lld;
int main()
{
    freopen("inp1.in","r",stdin);
    freopen("outp1.txt","w",stdout);
    lld t,tno=1;
    cin>>t;
    while(t--)
    {
        lld n,k;
        cin>>n>>k;
        vector<lld> a;
        a.push_back(n);
        /*
        for(vector<lld> :: iterator it=a.begin();it!=a.end();it++)
                cout<<(*it)<<" ";
        cout<<endl;*/
        k--;
        while(k--)
        {
            lld b=(*(a.end()-1));
            a.pop_back();
            lld c=b/2;
            lld j=b-c;
            if(j>c)
                j--;
            else
                c--;
            a.push_back(j);
            a.push_back(c);
            sort(a.begin(),a.end());
            /*for(vector<lld> :: iterator it=a.begin();it!=a.end();it++)
                cout<<(*it)<<" ";
            cout<<endl;*/
        }
        lld b=(*(a.end()-1));
        a.pop_back();
        cout<<"Case #"<<tno<<": ";
        lld c=b/2;
        lld j=b-c;
        if(j>c)
            j--;
        else
            c--;
        cout<<max(j,c)<<" "<<min(j,c)<<endl;
        tno++;
    }
    return 0;
}
