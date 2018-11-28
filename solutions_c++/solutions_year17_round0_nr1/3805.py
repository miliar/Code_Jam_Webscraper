#include <iostream>
#include <string>

using namespace std;

int main(){
    int tatti,poop=0;
    cin>>tatti;
    while(tatti--){
            poop++;
        string s;
        int k,ans=0;
        cin>>s>>k;
        bool a[s.size()],po = true;

        for(int i=0;i<s.size();i++){
            if(s[i]=='-')
                a[i] = false;
            else
                a[i] = true;}
        for( int i=0;i<s.size()-k+1;i++){
                if(a[i])
                    continue;
        else{ans++;
            for(int j = i;j<=i+k-1;j++){
                 if(a[j])
                    a[j]=false;
                 else
                    a[j]=true;
            }}}


        for( int i=0;i<s.size();i++){
             if(!a[i])
             {po = false; break;}
             }
           if(po)
             cout<<"Case #"<<poop<<": "<<ans<<endl;
             else
             cout<<"Case #"<<poop<<": "<<"IMPOSSIBLE\n";

    }
    return 0;
}
