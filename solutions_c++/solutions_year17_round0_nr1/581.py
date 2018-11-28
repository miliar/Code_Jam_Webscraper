#include<bits/stdc++.h>
#define P(x,y) make_pair(x,y)
using namespace std;
int T , n , K , Tn;
string str;
int main(){
    //freopen("in.in","r",stdin);
    //freopen("codejam.out","w",stdout);
    cin>>T;
    while(T--){
        cin>>str>>K;
        int ans = 0;
        n = str.size();
        str = "#" + str;
        for(int j = 1 ; j + K - 1 <= n ; j++){
            if(str[j] == '+') continue;
            for(int i = j ; i < j + K ; i++)
                if(str[i] == '+') str[i] = '-';
                else str[i] = '+';
            ++ans;
        }
        for(int j = 1 ; j <= n ; j++) if(str[j] == '-') ans = -1;
        printf("Case #%d: ",++Tn);
        if(ans == -1) puts("IMPOSSIBLE");
        else cout<<ans<<endl;

    }
}

