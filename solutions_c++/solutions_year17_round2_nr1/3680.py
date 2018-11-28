#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    FILE *fp;
    fp=freopen("A-large.in","r",stdin);
    fp=freopen("output.txt","w",stdout);
    cin >> t;
    for(int i=1;i<=t;i++){
        int d,n;
        float temp,minum;
        cin >> d >> n;
        int k[n];
        int s[n];
        for(int j=0;j<n;j++)
            cin >> k[j] >> s[j];
        minum=(float)(d-k[0])/s[0];
        for(int j=1;j<n;j++){
            temp=(float)(d-k[j])/s[j];
            if(temp>minum)
                minum=temp;
        }
        minum=(float)d/minum;
        printf("Case #%d: %f\n",i,minum);
    }
    fclose(fp);
    fclose(fp);
    return 0;
}
