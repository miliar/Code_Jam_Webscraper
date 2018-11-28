#include <iostream>
#include <deque>
using namespace std;
int64_t tidy (int64_t n)
{
    int64_t num=n;
    deque<int> digits={};
    while (num>0) {
        digits.push_front(num%10);
        num/=10;
    }
    if (digits.size()==1) {
        return n;
    }
    // for (auto&i:digits) cout<<i<<" ";cout<<endl;
    for (int i=1;i<digits.size();++i) {
        if (digits[i]<digits[i-1]) {
            int64_t newnum=0;
            for (int k=0;k<i;++k) {
                newnum+=digits[k];
                newnum*=10;
            }
            for (int k=0;k<digits.size()-i-1;++k) {
                newnum*=10;
            }
            newnum--;
            // cout<<newnum<<endl;
            return tidy(newnum);
        }
    }
    return n;
}
int main()
{
    int t;cin>>t;
    for (int i=1;i<=t;++i) {
        int64_t n;cin>>n;
        cout<<"Case #"<<i<<": "<<tidy(n)<<endl;
    }
}