#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("inp.txt","r",stdin);
	freopen("outs.txt","w",stdout);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++)
    {
        //cout<<"\n\nTest 1:\n";
        string arr;
        
        int m,n;
        cin>>arr>>m;
       string gg=arr;
       // cout<<m<<endl;
        n=arr.length();
        int i=0;
        int ans=INT_MAX;
        int ct=0;
        int f;
        i=0;
        ct=0;
        arr=gg;
        while(i<n) {
           // cout<<"Current index: "<<i<<endl;
            if(arr[i]=='+') {
                i++;
            }
            else {
                int fl=0;
                int kk=i;
                if(kk+m>n) break;
                for(;kk<i+m;kk++) {
                  //  cout<<"fhfgh\n";
                    if(arr[kk]=='-')
                        arr[kk]='+';
                    else arr[kk]='-';
                    if(kk>=n) { fl=1; break; }
                }
                while(arr[i]=='+') {
                    i++;
                }
                
                if(fl==1) break;
                else ct++;
                
             //cout<<"New arr: "<<arr<<endl;          
                   
            }
            
            
            
            
        }
        //cout<<arr<<endl;
        f=0;
        for(int i=0;i<n;i++) 
            if(arr[i]=='-')
                {f=1; break; }
        if(f==0)
        ans=min(ct,ans);
        cout<<"Case #"<<z<<": ";
        if(ans==INT_MAX) cout<<"IMPOSSIBLE\n";
        else cout<<ans<<endl;
        
    }
	return 0;
}
