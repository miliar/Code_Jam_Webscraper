#include <bits/stdc++.h>

using namespace std;

int main(){
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        string n;
        cin>>n;
        reverse(n.begin(),n.end());
        for(int cnt=1;cnt<n.size();cnt++){
            if(n[cnt]=='0')continue;
            if(n[cnt]>n[cnt-1]){
                n[cnt]--;
                for(int cnt2=cnt-1;cnt2>=0;cnt2--)
                    n[cnt2]='9';
            }
        }
        while(n.back()=='0')
            n.pop_back();
        reverse(n.begin(),n.end());
        printf("Case #%d: ",t);
        if(n.empty()) printf("0\n");
        else cout<<n<<"\n";
    }



    return 0;
}
