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
        int k;
        cin>>s>>k;
        int len=s.length(),count=0;
        for(int i=0 ; i<len ; i++){
            if(s[i]=='-'){
                count++;
                for(int j=i ; j<i+k && (i+k)<=len ; j++){
                    if(s[j]=='-'){
                        s[j]='+';
                    }
                    else{
                        s[j]='-';
                    }
                }
            }
        }
        cout<<"Case #"<<x<<": ";
        for(int i=0 ; i<len ; i++){
            if(s[i]=='-'){
                cout<<"IMPOSSIBLE\n";
                x++;
                break;
            }
            else if(i==len-1){
                cout<<count<<"\n";
                x++;
            }
        }
    }
    band;
}
