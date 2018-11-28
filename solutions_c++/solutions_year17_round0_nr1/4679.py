#include <bits/stdc++.h>
#define vi vector <int>
using namespace std;

int displayvi(vi a){for(int i=0;i<a.size();i++) cout<<a[i]<<"-"; cout<<endl;}

int q1(string s, int k)
{
    vi l; int ans; ans=0;
    int n=s.size();
    
    for(int i=n-1;i>=0;i--)
    {
        //cout<<i<<endl;
        int temp;
        if(s[i]=='+')
        {temp=1;} else {temp=0;}
        
        if((temp+l.size())%2==1) {}
        else
        {
            if(i<k-1){
                //cout<<i<<temp<<l.size()<<endl;
                l.clear(); return -1;
            }
            else
            {
                l.push_back(i-k+1);
                sort(l.begin(),l.end());
                //displayvi(l);
                //cout<<i-k+1<<endl;
                ans++;
            }
        }
        
        if(l.size()>0 && i<=l[l.size()-1]) l.erase(l.begin()+l.size()-1);
        
        
    }
    l.clear();
    return ans;
}

int main() {
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string s; int k;
        cin>>s;
        cin>>k;

        int a=q1(s,k);
        if(a==-1) cout<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<tt<<": "<<a<<endl;
    }
	// your code goes here
	return 0;
}
