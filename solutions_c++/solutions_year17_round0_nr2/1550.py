#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<set>
using namespace std;
//int m[6];
//int ma[6];
bool final = false;
long long getans(long long N){
    final = true;
    long long s = 1;
    while (true) {
        if (N/s/10==0) {
            break;
        }
        s*=10;
    }
    //        cout << s;
    long long l = N/s;
    long long ans = 0;
    long long c = l;
    while (s/10) {
        s = s/10;
        c = N/s%10;
//        cout << c <<l<<endl;
        if (c<l) {
            final = false;
            ans = ans *10+l-1;
            break;
        }
        ans = ans *10+l;
        l = c;
    }
    if (final) {
        ans = ans *10+c;
    }
    else{
        while (s) {
            s = s/10;
            ans = ans*10+9;
        }
    }
    return ans;
}

int main()
{
    freopen ("/Users/Victor/Desktop/myfile.txt","w",stdout);
    freopen ("/Users/Victor/Desktop/B-large.in","r",stdin);
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        
        long long N;
        cin >> N;
        long long ans = N;
        final = false;
        while (!final) {
            ans = getans(ans);
        }
        
        
        cout << "Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
}

