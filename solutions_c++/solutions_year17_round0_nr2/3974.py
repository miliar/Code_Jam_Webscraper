#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
vector<long long> List;
int main()
{
    freopen("data.out","w",stdout);
    long long N=1e+18;
    for(int i=1;i<=9;i++) List.push_back(i);
    for(int i=0;i<List.size();i++){
        if(List[i]>=N) break;
        for(int j=List[i]%10;j<=9;j++){
            List.push_back(List[i]*10+j);
        }
    }
    int T;
    scanf("%d",&T);
    long long n;
    for(int kase=1;kase<=T;kase++){
        scanf("%lld",&n);
        auto iter=lower_bound(List.begin(),List.end(),n);
        if(*iter != n) --iter;
        cout<<"Case #"<<kase<<": "<<*iter<<endl;
    }
    return 0;
}
