#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define pp pair<int,int>
using namespace std;


int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-output.txt","w",stdout);

    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        int n;
        cin>>n;
        int ans=0;
        for(int i=1;i<=n;i++){
            int x=i,last=9,ok=1;
            while(x>0){
                if(x%10>last){
                    ok=0;
                    break;
                }
                last=x%10;
                x/=10;
            }
            if(ok)ans=i;
        }

        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}
