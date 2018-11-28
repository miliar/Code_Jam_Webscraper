#include <bits/stdc++.h>
using namespace std;
#define file_input freopen("in.txt","r",stdin)
#define file_output freopen("op.txt","w",stdout)
int main() {
    file_input;
    file_output;
    int test_case;
    cin>>test_case;
    for(int t=1;t<=test_case;t++){
        string st;
        int k;
        cin>>st>>k;
        int l=st.length();
        int ans=0;
        for(int i=0;i<=l-k;i++){
            if(st[i]=='-'){
                ans++;
                for(int j=i;j<i+k;j++){
                    if(st[j]=='-')
                        st[j]='+';
                    else
                        st[j]='-';
                }
            }
        }
        int flag=0;
        for(int i=0;i<l;i++){
            if(st[i]=='-'){
                flag=1;
                break;
            }
        }
        if(flag==1)
            cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<t<<": "<<ans<<endl;
    }
	return 0;
}
