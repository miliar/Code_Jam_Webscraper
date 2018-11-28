#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define PI 3.14159265359
#define ff first
#define ss second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi > vpi;
int cnt[1002];
int flip[1002];
int main() {
    
    ios:: sync_with_stdio(0);
    cin.tie(NULL),cout.tie(NULL);
    int T,t;
    cin>>T;
    for(t=1;t<=T;t++){
        int i,k,c=0,n,f=0;
        string s;
        cin>>s>>k;
        n=s.size();
        
        if(s[0]=='+'){
            cnt[0]=0;
        }
        else{
            flip[0]=1;
            cnt[0]=1;
            c=1;
        }
            
        for(i=1;i<k;i++){
            if((s[i]=='+' && c%2==0) || (s[i]=='-' && c%2==1)){
                cnt[i]=cnt[i-1];
                continue;
            }
            if(i>n-k){
                f=1;
                break;
            }
            flip[i]=1;
            cnt[i]=cnt[i-1]+1;
            c++;
        }
        
        for(i=k;i<n && f==0;i++){
            cnt[i]=cnt[i-1]-flip[i-k];
            if(s[i]=='+' && cnt[i]%2==0)
                continue;
            if(s[i]=='-' && cnt[i]%2==1)
                continue;
            if(i>n-k){
                f=1;
            }    
            flip[i]=1;
            c++;
            cnt[i]++;
        }
        cout<<"Case #"<<t<<": ";
        if(f==0){
            cout<<c<<endl;
        }
        else{
            cout<<"IMPOSSIBLE"<<endl;
        }
        for(i=0;i<n;i++){
            flip[i]=0;
            cnt[i]=0;
        }
    }
    
	return 0;
}
