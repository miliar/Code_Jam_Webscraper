
#include<bits/stdc++.h>
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define N 2000
#define inf 1e9
#define F first
#define S second
#define mod 1000000007
#define ll long long
#define CLEAR(a) memset(a,0,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define fr freopen("input.in", "r", stdin);
#define fw freopen("output.txt", "w", stdout);
using namespace std;

//bool cmp(const pair<int,pii>& lhs, const pair<int,pii>& rhs)
//    return lhs.first < rhs.first;

main(){
    fr;fw;
    int t,cnt=1;
    ll i,k,n,lev,l,r,a,b;
    string s="";
    ios::sync_with_stdio(0);
    cin>>t;
    bool leftf=0;
    while(t--){
        s="";
        cin>>n>>k;
        lev=log2(k);
        while(lev>1){
            r=1<<lev;
            l=r+(r/2);
            if(k%2==0){//even
                if(k>=r && k<l)
                    leftf=0;
                else
                    leftf=1;
            }
            else{
                if(k>=r+1 && k<l+1)
                    leftf=0;
                else
                    leftf=1;
            }
            if(leftf){
                k-=r;
                s += '0';
            }
            else{
                k-=(r/2);
                s += '1';
            }
            lev--;
        }
        if(lev>=1){
            if(k==2)
                s += '1';
            else
                s += '0';
        }
        reverse(s.begin(),s.end());
        //cout<<s;
        n-=1;
        if(n%2){
            a=n/2;b=a+1;
        }
        else{
            a=n/2;b=a;
        }
        ////////

        for(i=0;i<s.length();i++){
            if(s[i]=='1'){//analyse b
                if(b%2==0){
                    b-=1;
                    a=b/2;b=a+1;
                }
                else{
                    b-=1;
                    a=b/2;b=a;
                }
            }
            else{//analyse a
                if(a%2==0){
                    a-=1;
                    a=a/2;b=a+1;
                }
                else{
                    a-=1;
                    a=a/2;b=a;
                }
            }
            //cout<<a<<" "<<b<<"\n";
        }
        cout<<"Case #"<<cnt<<": "<<b<<" "<<a<<"\n";
        cnt++;
    }
    return 0;
}



