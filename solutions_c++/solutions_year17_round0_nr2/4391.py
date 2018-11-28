#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> tidy;
    for(int i=1;i<=9;i++) {
        tidy.push_back(i);
        for(int j=i;j<=9;j++) {
            tidy.push_back(10*i+j);
            for(int k=j;k<=9;k++) {
                tidy.push_back(100*i+10*j+k);
            }
        }
    }
    sort(tidy.begin(),tidy.end());
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++) {
        int t;
        scanf("%d",&t);
        for(int j=tidy.size()-1;j>=0;j--) {
            if(tidy[j] <= t) {
                printf("Case #%d: %d\n",i,tidy[j]);
                break;
            }
        }
    }
}