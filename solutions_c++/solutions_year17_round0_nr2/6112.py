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

char a[22];
int main() {
    
    ios:: sync_with_stdio(0);
    cin.tie(NULL),cout.tie(NULL);
    int T,t;
    cin>>T;
    for(t=1;t<=T;t++){
        int i,d;
        string num;
        cin>>num;
        d=num.size();
        
        
        a[0]=num[0];
        for(i=1;i<d;i++){
            if(num[i]>=num[i-1])
                a[i]=num[i];
            else    
                break;    
        }
        int idx=i-1;
        
        if(i!=d){
            i=idx;
            while(i>=0 && num[i]==num[idx]){
                a[i]=num[idx]-1;
                i--;
            }
            int ind2=i+1;
            a[ind2]=num[idx]-1;
            for(i=ind2+1;i<d;i++){
                a[i]='9';
            }
            if(a[0]=='0'){
                d--;
                for(i=0;i<d;i++)
                    a[i]='9';
            }
        }
        cout<<"Case #"<<t<<": ";
        for(i=0;i<d;i++){
            
            cout<<a[i];
        }
        cout<<endl;
        
    }
    
	return 0;
}
