#include<iostream>
#include<string>
#include<vector>
using namespace std;

vector<int> separate(long long n) {
    vector <int> res;
    while(n!=0) {
        res.push_back(n%10);
        n/=10;
    }
    for (int i=0;i<res.size()/2;i++) {
        int tmp = res[i];
        res[i]=res[res.size()-i-1];
        res[res.size()-i-1] = tmp;
    }
    return res;
}

int main(){
    int T;
    long long n,ans;
    cin>>T;
    for (int t=1;t<=T;t++) {
        cin>>n;
        vector<int>a;
        if (n>=10) {
            a = separate(n);
            /*
            for (int i=0;i<a.size();i++) {
                cout<<a[i]<<" ";
            }
            cout<<endl;
            */
            for (int j=0; j<a.size(); j++) {
                int idx=-1;
                for (int i=a.size()-1; i>=1;i--) {
                    if (a[i]<a[i-1]) {
                        idx = i-1;
                    }
                }
                if (idx!=-1) {
                    for (int i=a.size()-1;i>idx;i--) {
                        a[i] = 9;
                    }
                    a[idx]--;
                }
            }
            ans=0;
            for (int i=0;i<a.size();i++) {
                ans*=10;
                ans+=a[i];
            }
        }
        else {
            ans = n;
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
