#include<set>
#include<map>
#include<unordered_set>
#include<vector>
#include<array>
#include<string>
#include<iostream>
#include<queue>
#include<algorithm>
#include<string.h>
#include<math.h>
using namespace std;
typedef long long ll;
typedef long double ld;

#define FOR(i,n) for(int i=0;i<n;i++)

int main(){
    freopen("/Users/shitian/Desktop/gcj/gcj/C-small-1-attempt4.in","r",stdin);
    freopen("/Users/shitian/Desktop/gcj/gcj/C-small-1-attempt4.txt","w",stdout);
    
    int tcase;
    cin>>tcase;
    for(int tc=1;tc<=tcase;tc++){
        cout<<"Case #"<<tc<<": ";
        
        int n,k;
        cin>>n>>k;
        double u;
        cin>>u;
        vector<double>p(n);
        for(int i=0;i<n;i++){
            cin>>p[i];
        }
        sort(p.begin(),p.end());
        double need=0,need_i=0,tot=0;
        for(int i=1;i<n;i++){
            double all_p=0;
            tot=0;
            for(int j=0;j<i;j++){
                all_p+=p[i]-p[j];
                tot+=p[j];
            }
            if(all_p>u){
                need=u,need_i=i;
                break;
            }
            need=all_p,need_i=i;
        }
        u-=need;
        for(int i=0;i<need_i;i++){
            p[i]=(tot+need)/need_i;
        }
        u/=n;
        for(int i=0;i<n;i++){
            p[i]+=u;
        }
        double ans=1;
        for(int i=0;i<n;i++){
            ans*=p[i];
        }
        printf("%.10lf\n",ans);
    }
}
