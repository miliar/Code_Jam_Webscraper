#include <bits/stdc++.h>
using namespace std;

int main () {
    int T,k;
    string s;
    cin>>T;
    //cout<<T<<endl;
    for (int i=1;i<=T;i++) {
        cin>>s;
        cin>>k;
        int si=s.size();
        vector<int> st;
        for (int i=0;i<si;i++) {
            if (s[i]=='-')
                st.push_back(0);
            if (s[i]=='+')
                st.push_back(1);
        }
        int count=0;
        for (int j=0;j<=(si-k);j++) {
            if (st[j]==0) {
                for (int l=j;l<(k+j);l++) {
                    if (st[l]==0)
                        st[l]=1;
                    else if (st[l]==1)
                        st[l]=0;
                }
                count++;
            }
        }
        int flag=0;
        for (int j=0;j<si;j++) {
            if (st[j]==0) {
                flag=1;
                break;
            }
        }
        if (flag==1)
            printf("Case #%d: IMPOSSIBLE\n",i);
        else
            printf("Case #%d: %d\n",i,count);
    }
    return 0;
}
