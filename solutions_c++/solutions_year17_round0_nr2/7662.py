#include <cstdio>
#include <string>
#include <cstring>
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
using namespace std;
string convert(long long int n){
    if(n == 0)  return "";
    char t=(n%10)+48;
    string x=convert(n/10);
    x=x+t;
    return x;
}
int main()
{
    FILEIOS
    int tc,cas=1;
    scanf("%d",&tc);
    while(tc--){
        long long int n;
        scanf("%lld",&n);
        string h=convert(n);
        int sz=h.size();sz--;
        int cnt=0;
        while(cnt!=sz){
            for(int i=1;i<h.size();i++){
                if(h[i] >= h[i-1]){
                    cnt++;
                    continue;
                }
                else{
                    cnt=0;
                    h[i-1]=h[i-1]-1;
                    for(int j=i;j<h.size();j++) h[j]=57;
                    break;
                }
            }
        }
        string ans="";
        for(int i=0;i<h.size();i++){
            if(h[i]!='0')   ans+=h[i];
        }
        printf("Case #%d: %s\n",cas++,ans.c_str());
    }
    return 0;
}
