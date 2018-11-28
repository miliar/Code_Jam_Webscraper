/*
	Gobind_Architect034
*/
#include<bits/stdc++.h>
using namespace std;
#define lli                 long long int
#define ll                  long long
#define ulli		    unsigned long long int
#define fast		    ios_base::sync_with_stdio(0)
#define loop(i,n)           for(int i=0 ; i<n ; i++)
#define pb                  push_back
#define gcd(a,b)            __gcd(a,b)
#define popb                pop_back
#define sortv(v)            sort(v.begin(),v.end())
#define reverse(v)	    reverse(v.begin(),v.end())
#define vec(v,n)	    vector<int> v(n)
#define vpp(v,n)	    vector<pair<int,int> > v(n)
#define band		    return 0
int main(){
    fast;
    int t;
    cin>>t;
    int x=1;
    while(t--){
        string s;
        cin>>s;
        int len=s.size(),flag=0,same=0;
        loop(i,len-1){
            if(s[i]<=s[i+1]){
                flag=1;
            }
            else if(s[i]>s[i+1]){
                flag=0;
                break;
            }
        }
        if(len==1){
            cout<<"Case #"<<x<<": "<<s;
        }
        else if(same==0){
            loop(i,len-1){
                if(s[i]>=s[i+1] && flag==0){
                    int daal=s[i]-1;
                    s[i]=char(daal);
                    s[i+1]='9';
                    flag=1;
                }
                else if(s[i]>s[i+1]){
                    s[i+1]='9';
                    flag=1;
                }
            }
            cout<<"Case #"<<x<<": ";
            loop(i,len){
                if(i==0 && s[i]=='0'){
                    continue;
                }
                else{
                    cout<<s[i];
                }
            }
        }
        else if(same==1){
            loop(i,len-1){
                if(s[i]>s[i+1] && flag==0){
                    int daal=s[i]-1;
                    s[i]=char(daal);
                    s[i+1]='9';
                    flag=1;
                }
                else if(s[i]>s[i+1]){
                    s[i+1]='9';
                    flag=1;
                }
            }
            cout<<"Case #"<<x<<": ";
            loop(i,len){
                if(i==0 && s[i]=='0'){
                    continue;
                }
                else{
                    cout<<s[i];
                }
            }
        }
        cout<<endl;
        x++;
    }
    band;
}
