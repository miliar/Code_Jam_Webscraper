#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.ans","w",stdout);
    int t, cs = 1;
    char s[25];
    long long n;
    cin>>t;
    while(t--){
        cin>>n;
        sprintf(s,"%lld",n);
        printf("Case #%d: ",cs++);
        int l = strlen(s);
        if(l==1){
            printf("%lld\n",n);
            continue;
        }
        for(int i = 1;i<l;i++){
            if(s[i]<s[i-1]){
                for(int j = i;j<l;j++){
                    s[j] = '9';
                }
                for(int j = i-1;j>=0;j--){
                    s[j]--;
                    if(j>0 && s[j-1]>s[j]){
                        s[j]='9';
                    }
                    else break;
                }
                break;
            }
        }
        sscanf(s,"%lld",&n);

        cout<<n<<endl;
    }
    return 0;
}
