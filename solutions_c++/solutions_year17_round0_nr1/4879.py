#include<bits/stdc++.h>
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define N 200000
#define inf 2000000000
#define F first
#define S second
#define mod 1000000007
#define ll long long int
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
    int t,i,k,j,g,flag,ptr,cnt,cntr=1;
    string s;
    ios::sync_with_stdio(0);
    cin>>t;
    while(t--){
        cnt=0,g=0;
        cin>>s>>k;
        i=0;
        while(i<s.length() && s[i]=='+')i++;

        while(i<s.length()){
            flag=0;
            if(s.length()-i<k){
                g=1;
                break;
            }

            for(j=i;j<k+i && j<s.length();j++){
                if(s[j]=='+' && flag==0)
                    ptr=j,flag=1;
                if(s[j]=='-')s[j]='+';
                else if(s[j]=='+')s[j]='-';

            }
            if(flag==0){
                i=i+k;
                while(i<s.length() && s[i]=='+')i++;
            }
            else
                i=ptr;
            cnt++;
        }
        if(g)
            cout<<"Case #"<<cntr<<": IMPOSSIBLE\n";
        else
            cout<<"Case #"<<cntr<<": "<<cnt<<"\n";
        cntr++;

    }

    return 0;
}
